from src.utils import load_excel, load_user_settings, greeting_by_time
from src.services import get_currency_rates, get_stock_prices


def main():
    # Пример использования функций
    settings = load_user_settings()
    currencies = settings.get("currencies", [])
    stocks = settings.get("stocks", [])

    currency_rates = get_currency_rates(currencies)
    stock_prices = get_stock_prices(stocks)

    print("Курсы валют:", currency_rates)
    print("Цены акций:", stock_prices)


if __name__ == "__main__":
    main()
