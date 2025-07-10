import questionary
from basic_bot import BasicBot

api_key = "api_key_here"  # Replace with your actual API key
api_secret = "api_secret_here"  # Replace with your actual API secret
bot = BasicBot(api_key, api_secret)

def trade_menu():
    order_type = questionary.select("Select order type:", choices=["market", "limit"]).ask()
    side = questionary.select("Buy or Sell?", choices=["BUY", "SELL"]).ask()
    symbol = questionary.text("Enter symbol (e.g. BTCUSDT):").ask()
    quantity = float(questionary.text("Enter quantity:").ask())
    price = None
    if order_type == "limit":
        price = float(questionary.text("Enter price:").ask())

    if order_type == "market":
        response = bot.place_market_order(symbol, side, quantity)
    else:
        response = bot.place_limit_order(symbol, side, quantity, price)

    print("\nOrder Result:")
    print(response)

def cancel_order_menu():
    symbol = questionary.text("Enter symbol:").ask()
    order_id = int(questionary.text("Enter order ID to cancel:").ask())
    response = bot.cancel_order(symbol, order_id)
    print("\nCancel Result:")
    print(response)

def main_menu():
    while True:
        action = questionary.select(
            "Choose an action:",
            choices=[
                "Place Order",
                "Check Balance",
                "Check Account Info",
                "View Open Orders",
                "Cancel Order",
                "Check Positions",
                "Exit"
            ]
        ).ask()

        if action == "Place Order":
            trade_menu()

        elif action == "Check Balance":
            print(bot.get_balance())

        elif action == "Check Account Info":
            print(bot.get_account_info())

        elif action == "View Open Orders":
            symbol = questionary.text("Enter symbol:").ask()
            print(bot.get_open_orders(symbol))

        elif action == "Cancel Order":
            cancel_order_menu()

        elif action == "Check Positions":
            positions = bot.get_positions()
            active_found = False
            total_pnl = 0.0

            for pos in positions:
                try:
                    amount = float(pos.get('positionAmt', 0))
                    if amount == 0:
                        continue  # Skip inactive positions

                    symbol = pos.get('symbol', 'N/A')
                    entry_price = pos.get('entryPrice', '0')
                    pnl = float(pos.get('unrealizedProfit', '0'))

                    total_pnl += pnl
                    active_found = True

                    print(f"{symbol:<10} | Amt: {amount:>7} | Entry: {entry_price:>8} | PnL: {pnl:>8.2f}")
                except Exception as e:
                    print(f"Error reading position data: {e}")

            if active_found:
                print(f"\n Total Unrealized PnL: {total_pnl:.4f} USDT")
            else:
                print("No active positions found.")

        elif action == "Exit":
            break

if __name__ == "__main__":
    main_menu()
