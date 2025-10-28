import logging
from datetime import datetime
from typing import Any, Dict, List
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def get_currency_rates(currencies: List[str]) -> List[Dict[str, Any]]:
    """
    Получает курсы валют через API.

    Args:
        currencies (List[str]): Список валют (например, ["USD", "EUR"]).

    Returns:
        List[Dict[str, Any]]: Курсы валют [{"currency": "USD", "rate": 70.0}, ...]
    """
    result = []
    for currency in currencies:
        try:
            resp = requests.get(
                f"https://api.exchangerate.host/latest?base=RUB&symbols={currency}",
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()
            rate = data.get("rates", {}).get(currency, 0)
            result.append({"currency": currency, "rate": round(rate, 2)})
        except Exception as e:
            logging.error(f"Ошибка при получении курса валют {currency}: {e}")
            result.append({"currency": currency, "rate": 0})
    return result


def get_stock_prices(stocks: List[str]) -> List[Dict[str, Any]]:
    """
    Получает цены акций (здесь фиктивные данные для теста).

    Args:
        stocks (List[str]): Список тикеров акций.

    Returns:
        List[Dict[str, Any]]: [{"stock": "AAPL", "price": 123.45}, ...]
    """
    return [{"stock": stock, "price": round(100 + hash(stock) % 500, 2)} for stock in stocks]


def simple_search(query: str, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Ищет транзакции по категории или описанию.

    Args:
        query (str): Строка поиска.
        transactions (List[Dict]): Список транзакций.

    Returns:
        List[Dict]: Найденные транзакции.
    """
    return [
        t
        for t in transactions
        if query.lower() in str(t.get("category", "")).lower()
        or query.lower() in str(t.get("description", "")).lower()
    ]


def investment_bank(month: str, transactions: List[Dict[str, Any]], currency: str = "USD") -> float:
    """
    Считает сумму расходов по заданной валюте за конкретный месяц.

    Args:
        month (str): месяц в формате 'YYYY-MM'.
        transactions (List[Dict]): список транзакций.
        currency (str): валюта для подсчета (по умолчанию USD).

    Returns:
        float: сумма расходов.
    """
    total = 0.0
    for t in transactions:
        t_date_str = t.get("date")
        t_currency = t.get("currency", "RUB")
        t_amount = t.get("amount", 0)

        if not t_date_str or t_currency != currency:
            continue

        # Преобразуем дату транзакции
        try:
            t_date = datetime.strptime(t_date_str, "%Y-%m-%d")
        except ValueError:
            continue

        if t_date.strftime("%Y-%m") == month:
            total += t_amount

    return total
