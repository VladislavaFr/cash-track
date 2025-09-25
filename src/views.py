import json
import logging
from datetime import datetime
import pandas as pd
import requests
from .utils import get_user_settings, get_exchange_rates, get_stock_prices

logging.basicConfig(level=logging.INFO)

def get_greeting(current_time: datetime) -> str:
    """
    Возвращает приветствие в зависимости от времени суток.
    """
    hour = current_time.hour
    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

def main_page(date_str: str, transactions: pd.DataFrame) -> dict:
    """
    Генерирует JSON-ответ для страницы 'Главная'.

    Параметры:
    date_str: str — дата и время в формате 'YYYY-MM-DD HH:MM:SS'
    transactions: pd.DataFrame — данные транзакций

    Возвращает:
    dict — JSON с приветствием, данными по картам, топ-5 транзакций, курсами валют и ценами акций
    """
    try:
        current_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        logging.error("Неверный формат даты")
        raise

    greeting = get_greeting(current_time)

    # TODO: здесь добавим расчет сумм по картам, кешбэка, топ транзакций
    cards_data = []
    top_transactions = []

    # Загружаем настройки пользователя
    user_settings = get_user_settings()

    # Получаем курсы валют и акции
    currency_rates = get_exchange_rates(user_settings["user_currencies"])
    stock_prices = get_stock_prices(user_settings["user_stocks"])

    response = {
        "greeting": greeting,
        "cards": cards_data,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices
    }

    return response
