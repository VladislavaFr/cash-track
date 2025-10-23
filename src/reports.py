from typing import List, Dict


def summarize_transactions(transactions: List[Dict]) -> Dict[str, float]:
    """
    Суммирует транзакции по валютам.

    Args:
        transactions (List[Dict]): Список транзакций.

    Returns:
        Dict[str, float]: Сумма по каждой валюте.
    """
    summary = {}
    for transaction in transactions:
        currency = transaction.get("currency", "RUB")
        amount = transaction.get("amount", 0)
        summary[currency] = summary.get(currency, 0) + amount
    return summary


def format_transaction_report(summary: Dict[str, float]) -> str:
    """
    Форматирует отчет по транзакциям.

    Args:
        summary (Dict[str, float]): Суммы транзакций по валютам.

    Returns:
        str: Текст отчета.
    """
    return "\n".join(f"{currency}: {amount:.2f}" for currency, amount in summary.items())
