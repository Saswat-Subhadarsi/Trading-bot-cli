# Trading Bot CLI

A modular command-line trading bot for placing orders on Binance Futures Testnet (USDT-M).  
The application supports MARKET and LIMIT orders with proper validation, structured logging, and real API integration.

---

## Features

- CLI-based order execution (MARKET & LIMIT)
- Supports BUY and SELL orders
- Input validation (side, order type, price rules)
- Real order execution using Binance Futures Testnet (REST API)
- Direct REST API integration with HMAC-SHA256 signing
- Structured logging to file
- Modular design (separation of CLI, validation, execution, logging)

---

## Demo Logs

Sample logs are available at:

logs/sample.log

---

## Example Commands

### Market Order

python cli.py BTCUSDT BUY MARKET 0.001


### Limit Order

python cli.py BTCUSDT SELL LIMIT 0.001 --price 72500


- For LIMIT orders, the price must fall within the valid range defined by Binance.
- If an invalid price is provided (too high or too low), the Binance API returns an error response, which is handled and logged by the application.
- Example: A limit price of 60000 may be rejected if it is outside the allowed trading range; adjusting to a valid price such as 72500 resolves the issue.

---

## Project Structure

trading_bot/
│
├── bot/
│ ├── client.py # Placeholder for future API abstraction
│ ├── orders.py # Order execution logic (REST API)
│ ├── validators.py # Input validation
│ ├── logging_config.py # Logging setup
│
├── logs/
├── cli.py # Entry point
├── requirements.txt
├── README.md

## Setup

Install dependencies:

pip install -r requirements.txt

Create a `.env` file in the root directory:
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key

## 🧠 Design Decisions

- Implemented direct REST API integration with HMAC-SHA256 signing for Binance Futures Testnet.
- Chose REST over third-party libraries to improve reliability and transparency during order execution.
- Designed modular architecture separating CLI, validation, execution, and logging layers for maintainability and extensibility.

---

## Future Improvements

- Add position tracking and balance queries
- Support additional order types (Stop-Limit, OCO, etc.)
- Improve CLI experience with interactive prompts
- Add retry logic and better error recovery