import json
import logging
import requests
from typing import List, Dict

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def get_currency_rates(currencies: list[str]) -> list[dict]:
    """#json #requests #logging
    Получает курсы валют из API.
    """
    url = "https://open.er-api.com/v6/latest/USD"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        rates = data.get("rates", {})
        return [{"currency": c, "rate": rates.get(c)} for c in currencies]
    except Exception as e:
        logging.error(f"Ошибка при получении курсов валют: {e}")
        return [{"currency": c, "rate": None} for c in currencies]


def get_stock_prices(stocks: list[str]) -> list[dict]:
    """#json #requests #logging
    Возвращает фиктивные данные по акциям (можно заменить API).
    """
    logging.info("Получение цен акций (демо)...")
    return [{"stock": s, "price": 100 + i * 5} for i, s in enumerate(stocks)]


def simple_search(query: str, transactions: List[Dict[str, str]]) -> str:
    """#json #logging
    Простой поиск транзакций по строке в описании.
    """
    logging.info(f"Выполняется поиск по запросу: {query}")
    try:
        result = [t for t in transactions if query.lower() in t.get("Описание", "").lower()]
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        logging.error(f"Ошибка при поиске: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False, indent=2)
