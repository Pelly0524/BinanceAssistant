from openai import OpenAI
import json
from utils.config import Config

client = OpenAI()
client.api_key = Config.OPENAI_API_KEY


# Here we define two functions: price check and market order placement
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_price",
            "description": "Retrieve the real-time market price",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading pair, e.g., BTCUSDT or BTC/USDT",
                    }
                },
                "required": ["symbol"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "place_order",
            "description": "Place an order on Binance (market order)",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading pair, e.g., BTCUSDT or BTC/USDT",
                    },
                    "side": {
                        "type": "string",
                        "description": "Buy or sell, e.g., buy or sell",
                    },
                    "quantity": {
                        "type": "number",
                        "description": "Trade quantity (float)",
                    },
                },
                "required": ["symbol", "side", "quantity"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_holdings",
            "description": "Check the current account spot holdings.",
            "parameters": {
                # No parameters needed as this simply retrieves information
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
]


def call_llm(messages):
    """
    Call OpenAI ChatCompletion with predefined tools.
    Returns a complete response containing tool_calls, text responses, and more.
    """
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        store=True,
    )
    return completion
