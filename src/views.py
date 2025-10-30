from datetime import datetime
from typing import Dict, Any
from src.utils import load_user_settings, greeting_by_time
from src.services import get_currency_rates, get_stock_prices
from src.reports import summarize_transactions, format_transaction_report
import pandas as pd

def generate_transaction_report(file_path: str) -> str:
    transactions = pd.read_excel(file_path).to_dict(orient="records")
    summary = summarize_transactions(transactions)
    return format_transaction_report(summary)

def main_page_response(date_str: str) -> Dict[str, Any]:
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    greeting = greeting_by_time(dt)
    settings = load_user_settings()
    currencies = settings.get("user_currencies", [])
    stocks = settings.get("user_stocks", [])

    currency_rates = get_currency_rates(currencies)
    stock_prices = get_stock_prices(stocks)

    cards = [{"last_digits": "5814", "total_spent": 1262.0, "cashback": 12.62}]
    top_transactions = [
        {
            "date": "21.12.2021",
            "amount": 1198.23,
            "category": "Переводы",
            "description": "Перевод Кредитная карта. ТП 10.2 RUR",
        }
    ]

    return {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }
