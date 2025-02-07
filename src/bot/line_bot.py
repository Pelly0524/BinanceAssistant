import json
from linebot import LineBotApi
from linebot.models import MessageEvent, TextSendMessage
from utils.config import Config

# 從 agent_manager 匯入我們的建構函式
# Import the function to create our Agent
from services.agent_manager import create_binance_agent

line_bot_api = LineBotApi(Config.LINE_CHANNEL_ACCESS_TOKEN)

# 在這裡建一個全域的 Agent，可重複使用
# Create a global Agent instance for reuse
BINANCE_AGENT = create_binance_agent()


def handle_message(event: MessageEvent):
    """
    When the Line Bot receives a message, pass it to the AI Agent and return the response.
    """
    user_message = event.message.text.strip()

    try:
        # Agent.run() 會分析 user_message 並自行決定要用哪個 Tool
        # Agent.run() analyzes the user_message and decides which Tool to use
        response = BINANCE_AGENT.run(user_message)
    except Exception as e:
        response = f"[Error] {str(e)}"

    # 將 Agent 的回覆透過 Line Bot 回傳給使用者
    # Send the Agent's response back to the user via Line Bot
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=response))
