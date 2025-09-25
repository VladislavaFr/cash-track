import logging
from datetime import datetime
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

def cashback_analysis(year: int, month: int, transactions: List[Dict[str, Any]]) -> dict:
    """
    Анализ выгодных категорий повышенного кешбэка.
    """
    result = {}
    for tx in transactions:
        date = datetime.strptime(tx["Дата операции"], "%Y-%m-%d")
        if date.year == year and date.month == month:
            category = tx.get("Категория", "Прочее")
            result[category] = result.get(category, 0) + tx.get("Сумма платежа", 0) / 100
    logger.info("Cashback analysis done")
    return result
