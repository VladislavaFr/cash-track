from datetime import datetime
from .utils import get_greeting, read_excel, fetch_currency_rates, fetch_stock_prices

def main_page_view(date_str: str, excel_file: str) -> dict:
    """
    Функция для страницы 'Главная'.
    """
    current_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    greeting = get_greeting(current_time)

    df = read_excel(excel_file)
    cards = []
    for card_number, group in df.groupby("Номер карты"):
        total_spent = group["Сумма платежа"].sum()
        cashback = total_spent / 100
        cards.append({
            "last_digits": str(card_number)[-4:],
            "total_spent": round(total_spent, 2),
            "cashback": round(cashback, 2)
        })

    top_transactions = df.sort_values("Сумма платежа", ascending=False).head(5).to_dict(orient="records")

    currency_rates = [{"currency": k, "rate": v} for k, v in fetch_currency_rates(["USD", "EUR"]).items()]
    stock_prices = [{"stock": k, "price": v} for k, v in fetch_stock_prices(["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]).items()]

    return {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices
    }
