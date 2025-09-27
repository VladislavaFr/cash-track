import logging
from typing import Dict
from .utils import read_transactions_from_excel, filter_transactions, sum_cashback

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def cashback_analysis(file_path: str, year: int, month: int) -> Dict[str, float]:
    """
    Полный анализ кешбэка с чтением Excel.
    Возвращает словарь {категория: сумма кешбэка}.
    """
    logger.info("Чтение транзакций...")
    df = read_transactions_from_excel(file_path)
    if df.empty:
        logger.warning("Нет транзакций для анализа.")
        return {}

    logger.info(f"Фильтрация транзакций за {year}-{month}...")
    df_filtered = filter_transactions(df, year, month)

    logger.info("Суммирование кешбэка по категориям...")
    result = sum_cashback(df_filtered)

    logger.info("Анализ кешбэка завершен.")
    return result
