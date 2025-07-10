# 💹 Crypto Trading Bot for Binance Futures (Testnet) 

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A Python trading bot for Binance Futures Testnet with both command-line and interactive menu interfaces. Execute trades, manage positions, and monitor your test portfolio with ease.

![Bot Demo](https://via.placeholder.com/800x400.png?text=CLI+Interface+Demo) 
*(Consider adding actual screenshot later)*

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
- � Reusable `BasicBot` core class

### User Interface
- ⌨️ Traditional command-line interface (`main.py`)
- 🖱️ Interactive menu-driven CLI (`ui_main.py`)

## 🛠️ Technology Stack

| Component        | Technology           |
|------------------|----------------------|
| Language         | Python 3.13          |
| Binance API      | python-binance v1.0+ |
| CLI Framework    | questionary          |
| Logging          | Python logging       |
| Virtual Env      | venv                 |


## 📁 Project Structure
Trading_Bot/
├── basic_bot.py # Core bot logic and API handler
├── main.py # Command-line interface (argparse)
├── ui_main.py # Interactive menu interface
├── bot.log # Activity and error logs
├── requirements.txt # Dependencies
├── README.md # Documentation
└── .env.example # Environment template


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
---
2. Set up virtual environment:

    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate