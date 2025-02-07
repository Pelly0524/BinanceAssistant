import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from utils.config import Config

from services.binance_tools import (
    tool_get_current_price,
    tool_place_order,
    tool_get_holdings,
    tool_get_min_order_quantity,
)


def create_binance_agent():
    """
    Create and return a LangChain Agent that handles Binance functionalities.
    """

    openai_api_key = Config.OPENAI_API_KEY

    # Initialize the LLM using OpenAI
    llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key, model="gpt-4o")

    # Wrap the tool functions into LangChain Tool objects
    tools = [
        Tool(
            name="get_current_price",
            func=tool_get_current_price.run,
            description=(
                "Retrieve the current price for a specific trading pair.\n"
                "Must pass a single string with the trading pair.\n"
                "Example:\n"
                '  get_current_price("BTCUSDT")'
            ),
        ),
        Tool(
            name="place_order",
            func=tool_place_order.run,
            description=(
                "Place a market order on Binance.\n"
                "Must pass a single string with 'symbol, side, quantity'.\n"
                "Example:\n"
                '  place_order("BTCUSDT, buy, 0.001")'
            ),
        ),
        Tool(
            name="get_holdings",
            func=tool_get_holdings.run,
            description=("Retrieve current account holdings."),
        ),
        Tool(
            name="get_min_order_quantity",
            func=tool_get_min_order_quantity.run,
            description=(
                "Retrieve the minimum order quantity for a specific trading pair.\n"
                "Must pass a single string with the trading pair.\n"
                "Example:\n"
                '  get_min_order_quantity("BTCUSDT")'
            ),
        ),
    ]

    # Initialize the Agent with the ZERO_SHOT_REACT_DESCRIPTION approach
    agent = initialize_agent(
        tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    return agent
