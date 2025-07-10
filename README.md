# 💹 Crypto Trading Bot for Binance Futures (Testnet)

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)](https://www.python.org/downloads/)

A Python trading bot for Binance Futures Testnet with both command-line and interactive menu interfaces. Execute trades, manage positions, and monitor your test portfolio with ease.


## ✨ Key Features

### Trading Capabilities
- ✅ Market & Limit orders (BUY/SELL)
- 📊 Position tracking with PnL calculation
- ✖️ Order cancellation functionality
- 🔄 Real-time execution feedback

### Technical Features
- 🔒 Secure Binance Testnet API integration
- 📝 Comprehensive logging (`bot.log`)
- 🛡️ Robust error handling
- ♻️ Reusable `BasicBot` core class

### User Interface
- ⌨️ Traditional command-line interface (`main.py`)
- 🖱️ Interactive menu-driven CLI (`ui_main.py`)

## 🛠️ Technology Stack

| Component     | Technology           |
|---------------|----------------------|
| Language      | Python 3.13          |
| Binance API   | python-binance v1.0+ |
| CLI Framework | questionary          |
| Logging       | Python logging       |
| Virtual Env   | venv                 |

```
Trading_Bot/
├── basic_bot.py        # Core bot logic and API handler
├── main.py             # CLI interface (argparse)
├── ui_main.py          # Interactive menu interface
├── bot.log             # Logs: activity, errors, API responses
├── requirements.txt    # Dependencies
├── README.md           # You're reading it
└── .gitignore          # Excludes venv, cache, log from Git
```

## 🚀 Quick Start

### Prerequisites
- Python 3.13
- Binance Futures Testnet account ([sign up](https://testnet.binancefuture.com/en/futures/BTCUSDT))
- Testnet API keys

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/trading-bot.git
   cd trading-bot
   ```

2. Set up virtual environment:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Binance Testnet API credentials:  
   Edit `main.py` and `ui_main.py`, and replace:
   ```python
   api_key = "your_api_key"
   api_secret = "your_api_secret"
   ```

## 💻 CLI Usage

### ▶️ Command-Line Interface (`main.py`)

Market Order:
```bash
python main.py --action trade --type market --side BUY --symbol BTCUSDT --quantity 0.01
```

Limit Order:
```bash
python main.py --action trade --type limit --side SELL --symbol BTCUSDT --quantity 0.01 --price 60000
```

Check Balance:
```bash
python main.py --action balance
```

View Positions:
```bash
python main.py --action positions
```

Cancel Order:
```bash
python main.py --action cancel --symbol BTCUSDT --order_id 123456
```

### ▶️ Interactive CLI (`ui_main.py`)

```bash
python ui_main.py
```

Navigate using arrow keys and follow interactive prompts.

![WhatsApp Image 2025-07-10 at 09 35 03_1fbd0637](https://github.com/user-attachments/assets/a4a11822-57ff-49c8-971d-a764bfca1feb)

![WhatsApp Image 2025-07-10 at 09 33 19_d595a966](https://github.com/user-attachments/assets/b09d85af-314a-4426-96c2-3351f8428ff3)

![WhatsApp Image 2025-07-10 at 09 37 32_b692c2e9](https://github.com/user-attachments/assets/4f4cf14d-7016-43f4-b52a-fc1f60c61c88)

## 📊 Logging System

All activity (orders, errors, API calls) is logged in `bot.log`, e.g.:

```log
2025-07-09 09:12:45 - INFO - Placing MARKET order: BUY 0.01 BTCUSDT
2025-07-09 09:12:46 - ERROR - Market Order Error: API-key format invalid
2025-07-09 14:22:46,124 - INFO - Order executed: ID 123456
2025-07-09 14:23:10,002 - ERROR - API Connection timeout
