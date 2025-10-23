import logging
import re
from typing import Any, Dict, List
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def get_currency_rates(currencies: List[str]) -> List[Dict[str, Any]]:
    """
    Получает курсы валют через API.

    Args:
        currencies (List[str]): Список валют.

    Returns:
        List[Dict[str, Any]]: Курсы валют.
    """
    result = []
    for currency in currencies:
        try:
            resp = requests.get(
                f"https://api.exchangerate.host/latest?base=RUB&symbols={currency}", timeout=10
            )
            resp.raise_for_status()
            data = resp.json()
            rate = data.get("rates", {}).get(currency, 0)
            result.append({"currency": currency, "rate": round(rate, 2)})
        except Exception as e:
            logging.error(f"Ошибка при получении курсов валют: {e}")
            result.append({"currency": currency, "rate": 0})
    return result


def get_stock_prices(stocks: List[str]) -> List[Dict[str, Any]]:
    """
    Получает цены акций (здесь фиктивные данные).

    Args:
        stocks (List[str]): Список акций.

    Returns:
        List[Dict[str, Any]]: Список с ценами акций.
    """
    return [{"stock": stock, "price": round(100 + hash(stock) % 500, 2)} for stock in stocks]


def simple_search(query: str, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Ищет транзакции по категории или описанию.

    Args:
        query (str): Строка поиска.
        transactions (List[Dict[str, Any]]): Список транзакций.

    Returns:
        List[Dict[str, Any]]: Список найденных транзакций.
    """
    return [
        t
        for t in transactions
        if query.lower() in str(t.get("category", "")).lower()
        or query.lower() in str(t.get("description", "")).lower()
    ]
