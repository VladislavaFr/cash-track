from datetime import datetime
from src.utils import load_user_settings, greeting_by_time
from src.services import get_currency_rates, get_stock_prices

def main():
    """
    Главная функция приложения.

    Загружает пользовательские настройки, получает курсы валют и акции,
    выводит приветствие и результаты.
    """
    settings = load_user_settings()
    currencies = settings.get("user_currencies", [])
    stocks = settings.get("user_stocks", [])

    currency_rates = get_currency_rates(currencies)
    stock_prices = get_stock_prices(stocks)

    current_time = datetime.now()
    greeting = greeting_by_time(current_time)

    print(greeting)
    print("Курсы валют:", currency_rates)
    print("Цены акций:", stock_prices)


if __name__ == "__main__":
    main()
