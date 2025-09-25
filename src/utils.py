import json
import logging
from datetime import datetime
import pandas as pd
import requests

logger = logging.getLogger(__name__)

def read_excel(file_path: str) -> pd.DataFrame:
    """
    Считывает Excel-файл и возвращает DataFrame.
    """
    try:
        df = pd.read_excel(file_path)
        logger.info(f"Excel file {file_path} read successfully")
        return df
    except Exception as e:
        logger.error(f"Error reading Excel file {file_path}: {e}")
        raise

def format_json(data: dict) -> str:
    """
    Преобразует словарь в JSON строку.
    """
    return json.dumps(data, ensure_ascii=False, indent=2)

def get_greeting(current_time: datetime) -> str:
    """
    Возвращает приветствие в зависимости от времени суток.
    """
    hour = current_time.hour
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

def fetch_currency_rates(currencies: list) -> dict:
    """
    Заглушка для получения курса валют через API.
    """
    # Здесь можно подключить любой API
    rates = {currency: 70.0 + i for i, currency in enumerate(currencies)}
    return rates

def fetch_stock_prices(stocks: list) -> dict:
    """
    Заглушка для получения цен на акции через API.
    """
    prices = {stock: 100.0 + i * 10 for i, stock in enumerate(stocks)}
    return prices
