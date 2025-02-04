import json
from linebot import LineBotApi
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from utils.config import Config
from services.llm_service import call_llm
from services.binance_service import get_current_price, place_order, get_holdings

line_bot_api = LineBotApi(Config.LINE_CHANNEL_ACCESS_TOKEN)


def handle_message(event: MessageEvent):
    user_message = event.message.text.strip()

    messages = [
        {
            "role": "system",
            "content": "You are an assistant that helps users manage Binance trading, supporting price inquiries and order placement.",
        },
        {"role": "user", "content": user_message},
    ]

    while True:
        # First or subsequent call to the LLM
        completion = call_llm(messages)
        assistant_message = completion.choices[0].message
        tool_calls = assistant_message.tool_calls

        # If no function call is present, the model response is the final textual reply
        if not tool_calls:
            final_reply = assistant_message.content
            break

        # 1) Add the current assistant message to messages
        messages.append(assistant_message)

        # 2) Handle all tool calls within the assistant message
        tool_responses = []
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            arguments_str = tool_call.function.arguments

            try:
                args = json.loads(arguments_str)
            except json.JSONDecodeError:
                args = {}

            # Execute the corresponding function
            if function_name == "get_current_price":
                result = get_current_price(args.get("symbol", "BTCUSDT"))
            elif function_name == "place_order":
                result = place_order(
                    args.get("symbol", "BTCUSDT"),
                    args.get("side", "buy"),
                    args.get("quantity", 0.001),
                )
            elif function_name == "get_holdings":
                result = get_holdings()
            else:
                result = f"Unsupported function: {function_name}"

            # Return the tool result with role="tool"
            tool_responses.append(
                {"role": "tool", "tool_call_id": tool_call.id, "content": str(result)}
            )

        # 3) Add all tool responses to messages at once
        messages.extend(tool_responses)
        # Continue to the next iteration of while True to call the LLM again

    # Exit the while True loop once the final reply is determined
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text=final_reply.replace("**", ""))
    )
