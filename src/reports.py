import logging
import pandas as pd
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)

def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """
    Отчёт: траты по категории за последние три месяца.
    """
    if date:
        end_date = datetime.strptime(date, "%Y-%m-%d")
    else:
        end_date = datetime.now()
    start_date = end_date - pd.DateOffset(months=3)
    filtered = transactions[
        (transactions["Дата операции"] >= start_date) &
        (transactions["Дата операции"] <= end_date) &
        (transactions["Категория"] == category)
    ]
    logger.info(f"Report generated for category {category}")
    return filtered
