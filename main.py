import argparse
from basic_bot import BasicBot

api_key = "api_key_here"  # Replace with your actual API key
api_secret = "api_secret_here"  # Replace with your actual API secret

bot = BasicBot(api_key, api_secret)

parser = argparse.ArgumentParser()
parser.add_argument('--action', choices=['trade', 'balance', 'info', 'open_orders', 'cancel', 'positions'], required=True)
parser.add_argument('--type', choices=['market', 'limit'], help="Required for trade action")
parser.add_argument('--side', choices=['BUY', 'SELL'], help="Required for trade action")
parser.add_argument('--symbol', help="e.g., BTCUSDT")
parser.add_argument('--quantity', type=float, help="Required for trade action")
parser.add_argument('--price', type=float, help="Required for limit orders")
parser.add_argument('--order_id', type=int, help="Required for cancel action")

args = parser.parse_args()

if args.action == 'trade':
    if not all([args.type, args.side, args.symbol, args.quantity]):
        raise ValueError("Missing trade parameters. --type, --side, --symbol, and --quantity are required.")
    
    if args.type == "market":
        order = bot.place_market_order(args.symbol, args.side, args.quantity)
    elif args.type == "limit":
        if not args.price:
            raise ValueError("Price is required for limit orders")
        order = bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)
    print("Order Result:")
    print(order)

elif args.action == 'balance':
    print("Balance:")
    print(bot.get_balance())

elif args.action == 'info':
    print("Account Info:")
    print(bot.get_account_info())

elif args.action == 'open_orders':
    if not args.symbol:
        raise ValueError("Please provide --symbol to fetch open orders.")
    print("Open Orders:")
    print(bot.get_open_orders(args.symbol))

elif args.action == 'cancel':
    if not all([args.symbol, args.order_id]):
        raise ValueError("Please provide --symbol and --order_id to cancel an order.")
    print("Cancel Result:")
    print(bot.cancel_order(args.symbol, args.order_id))

positions = bot.get_positions(args.symbol) if args.symbol else bot.get_positions()
print("Open Positions:\n")

total_pnl = 0.0
active_positions_found = False

for pos in positions:
    try:
        amount = float(pos.get('positionAmt', 0))
        if amount == 0:
            continue

        active_positions_found = True
        symbol = pos.get('symbol', 'N/A')
        entry_price = pos.get('entryPrice', '0')
        pnl = float(pos.get('unrealizedProfit', '0'))

        total_pnl += pnl

        print(f"Symbol: {symbol}, Amount: {amount}, Entry Price: {entry_price}, Unrealized PnL: {pnl:.4f}")
    except Exception as e:
        print(f"Error parsing position: {e}")

if active_positions_found:
    print(f"\nTotal Unrealized PnL Across Positions: {total_pnl:.4f} USDT")
else:
    print(" No active positions found.")


