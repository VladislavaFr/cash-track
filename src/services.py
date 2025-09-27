import logging
from typing import Any, Dict, List

import requests


def get_currency_rates(currencies):
    result = []
    for currency in currencies:
        try:
            resp = requests.get(
                f"https://api.exchangerate.host/latest?base=RUB&symbols={currency}", timeout=10
            )
            resp.raise_for_status()
            data = resp.json()
            rate = data.get("rates", {}).get(currency, None)
            if rate is None:
                logging.warning(f"Не удалось получить курс для {currency}")
                rate = 0
            result.append({"currency": currency, "rate": round(rate, 2)})
        except Exception as e:
            logging.error(f"Ошибка при получении курсов валют: {e}")
            result.append({"currency": currency, "rate": 0})
    return result


def get_stock_prices(stocks: List[str]) -> List[Dict[str, Any]]:
    result = []
    for stock in stocks:
        # Фиктивные данные
        result.append({"stock": stock, "price": round(100 + hash(stock) % 500, 2)})
    return result
