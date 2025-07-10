from binance.client import Client 
from binance.enums import *
import logging

# Setup logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_event(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com'

    def place_market_order(self, symbol, side, quantity):
        try:
            log_event(f"Placing MARKET order: {side} {quantity} {symbol}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            log_event(f"Market Order Response: {order}")
            return order
        except Exception as e:
            log_error(f"Market Order Error: {e}")
            print(f"Market order error: {e}")

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            log_event(f"Placing LIMIT order: {side} {quantity} {symbol} at {price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            log_event(f"Limit Order Response: {order}")
            return order
        except Exception as e:
            log_error(f"Limit Order Error: {e}")
            print(f"Limit order error: {e}")
    def get_account_info(self):
        try:
            account_info = self.client.futures_account()
            log_event(f"Account Info: {account_info}")
            return account_info
        except Exception as e:
            log_error(f"Get Account Info Error: {e}")
            print(f"Get account info error: {e}")
    def get_balance(self):
        try:
            balance = self.client.futures_account_balance()
            log_event(f"Balance: {balance}")
            return balance
        except Exception as e:
            log_error(f"Get Balance Error: {e}")
            print(f"Get balance error: {e}")
    def get_open_orders(self, symbol):
        try:
            open_orders = self.client.futures_get_open_orders(symbol=symbol)
            log_event(f"Open Orders for {symbol}: {open_orders}")
            return open_orders
        except Exception as e:
            log_error(f"Get Open Orders Error: {e}")
            print(f"Get open orders error: {e}")
    def cancel_order(self, symbol, order_id):
        try:
            log_event(f"Cancelling order {order_id} for {symbol}")
            response = self.client.futures_cancel_order(symbol=symbol, orderId=order_id)
            log_event(f"Cancel Order Response: {response}")
            return response
        except Exception as e:
            log_error(f"Cancel Order Error: {e}")
            print(f"Cancel order error: {e}")
    def get_positions(self, symbol=None):
        try:
            positions = self.client.futures_position_information()
            if symbol:
                positions = [p for p in positions if p['symbol'] == symbol.upper()]
            log_event(f"Positions: {positions}")
            return positions
        except Exception as e:
            log_error(f"Get Positions Error: {e}")
            print(f"Get positions error: {e}")
