from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type, validate_price
from bot.logging_config import get_logger

logger = get_logger()

def run_ui():
    print("""
============================
   BINANCE TRADING BOT UI
============================
""")

    while True:
        print("\nChoose option:")
        print("1. Market Order")
        print("2. Limit Order")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "3":
            print("Exiting...")
            break

        try:
            symbol = input("Symbol (e.g., BTCUSDT): ").upper()
            side = input("Side (BUY/SELL): ").upper()
            quantity = float(input("Quantity: "))

            validate_side(side)

            if choice == "1":
                response = place_market_order(symbol, side, quantity)

            elif choice == "2":
                price = float(input("Price: "))
                validate_price("LIMIT", price)
                response = place_limit_order(symbol, side, quantity, price)

            else:
                print("Invalid choice")
                continue

            logger.info(response)

            print("\n=== ORDER RESULT ===")
            print("Order ID:", response.get("orderId"))
            print("Status:", response.get("status"))
            print("Executed Qty:", response.get("executedQty"))

        except Exception as e:
            logger.error(str(e))
            print("\n ERROR:", e)


if __name__ == "__main__":
    run_ui()