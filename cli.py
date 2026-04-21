import typer
from bot.validators import validate_side, validate_order_type, validate_price
from bot.orders import place_market_order, place_limit_order
from bot.logging_config import get_logger

app = typer.Typer()
logger = get_logger()

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = typer.Option(None)
):
    try:
        #Validation
        validate_side(side)
        validate_order_type(order_type)
        validate_price(order_type, price)

        #Execution
        if order_type == "MARKET":
            response = place_market_order(symbol, side, quantity)
        else:
            response = place_limit_order(symbol, side, quantity, price)

        #Logging
        logger.info(response)

        #Output
        print("\n=== ORDER REQUEST ===")
        print(f"Symbol       : {symbol}")
        print(f"Side         : {side}")
        print(f"Order Type   : {order_type}")
        print(f"Quantity     : {quantity}")
        if price:
            print(f"Price        : {price}")

        print("\n=== ORDER RESPONSE ===")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

        print("\nSUCCESS" if response.get("orderId") else "\nFAILED")
    except Exception as e:
        logger.error(str(e))
        print("\nERROR:", e)

if __name__ == "__main__":
    app()