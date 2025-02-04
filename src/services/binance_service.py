from binance.client import Client
from utils.config import Config

api_key = Config.BINANCE_API_KEY
api_secret = Config.BINANCE_API_SECRET

binance_client = Client(api_key, api_secret)
binance_client.API_URL = "https://testnet.binance.vision/api"


def get_current_price(symbol: str):
    """
    Get the real-time price for a specific trading pair (e.g., 'BTCUSDT' or 'BTC/USDT')
    """
    normalized_symbol = symbol.replace("/", "")  # Remove slashes if present
    try:
        ticker = binance_client.get_symbol_ticker(symbol=normalized_symbol)
        return float(ticker["price"])
    except Exception as e:
        return f"Price retrieval failed: {str(e)}"


def place_order(symbol: str, side: str, quantity: float):
    """
    Place a market order on Binance
    :param symbol: 'BTCUSDT' or 'BTC/USDT'
    :param side: 'buy' or 'sell'
    :param quantity: The amount to be traded
    """
    normalized_symbol = symbol.replace("/", "")
    side_upper = side.upper()  # Convert 'buy' -> 'BUY', 'sell' -> 'SELL'

    try:
        order = binance_client.create_order(
            symbol=normalized_symbol, side=side_upper, type="MARKET", quantity=quantity
        )
        return (
            f"Order placed successfully: {normalized_symbol} {side_upper} {quantity}, "
            f"Order status: {order.get('status')}"
        )
    except Exception as e:
        return f"Order placement failed: {str(e)}"


def get_holdings():
    """
    Retrieve the current spot holdings of the account
    Returns: Holdings information as a string, e.g.,
    'Holdings: BTC=0.005, ETH=1.0, USDT=50.0'
    """
    try:
        # Retrieve complete account information
        account_info = binance_client.get_account()
        balances = account_info.get("balances", [])

        # Filter assets with non-zero balance
        holdings = []
        for asset_info in balances:
            asset = asset_info["asset"]
            free = float(asset_info["free"])
            locked = float(asset_info["locked"])
            total = free + locked
            if total > 0:
                holdings.append(f"{asset}={total}")

        if not holdings:
            return "No holdings currently (balance is 0)"

        return "Holdings: " + ", ".join(holdings)

    except Exception as e:
        return f"Holdings retrieval failed: {str(e)}"
