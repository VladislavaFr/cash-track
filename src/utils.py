import json
import logging

def get_user_settings() -> dict:
    """
    Возвращает настройки пользователя из user_settings.json
    """
    # TODO: считать из user_settings.json
    return {
        "user_currencies": ["USD", "EUR"],
        "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    }

def get_exchange_rates(currencies):
    """
    Возвращает текущие курсы валют
    """
    # TODO: запрос к API курсов валют
    return [{"currency": c, "rate": 0} for c in currencies]

def get_stock_prices(stocks):
    """
    Возвращает текущие цены акций
    """
    # TODO: запрос к API акций
    return [{"stock": s, "price": 0} for s in stocks]
