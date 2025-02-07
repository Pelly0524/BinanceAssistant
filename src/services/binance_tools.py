from langchain.tools import tool
from services.binance_service import (
    get_current_price,
    place_order,
    get_holdings,
    get_min_order_quantity,
)
import re


@tool("get_current_price", return_direct=True)
def tool_get_current_price(symbol: str = "BTCUSDT") -> str:
    """
    Retrieve the current price for the specified trading pair, default 'BTCUSDT'.

    The agent may pass something like "BTCUSDT" or a JSON-like string with "symbol".
    We'll parse out the actual symbol.
    """

    symbol = symbol.strip()
    symbol_cleaned = re.sub(r"[^A-Z0-9_.-]", "", symbol.upper())

    price = get_current_price(symbol_cleaned)
    return f"[{symbol_cleaned}] current price: {price}"


@tool("place_order", return_direct=True)
def tool_place_order(symbol_side_quantity: str) -> str:
    """
    Place a market order. Accepts a single string in the format: 'symbol, side, quantity'.
    """
    try:
        parts = [p.strip() for p in symbol_side_quantity.split(",")]
        if len(parts) != 3:
            raise ValueError("Invalid input format. Expected 'symbol, side, quantity'.")

        symbol, side, quantity = parts

        result = place_order(symbol, side, quantity)
        return result
    except Exception as e:
        return str(e)


@tool("get_min_order_quantity", return_direct=True)
def tool_get_min_order_quantity(symbol: str) -> str:
    """
    Retrieve the minimum order quantity for the specified trading pair.
    """
    return get_min_order_quantity(symbol)


@tool("get_holdings", return_direct=True)
def tool_get_holdings() -> str:
    """
    Retrieve current account holdings (balances).
    """
    return get_holdings()
