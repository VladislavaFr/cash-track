from datetime import datetime
from typing import List, Dict


def summarize_transactions(transactions: List[Dict]) -> Dict[str, float]:
    summary = {}
    for transaction in transactions:
        currency = transaction.get("currency", "RUB")
        amount = transaction.get("amount", 0)
        summary[currency] = summary.get(currency, 0) + amount
    return summary


def format_transaction_report(summary: Dict[str, float]) -> str:
    report_lines = [f"{currency}: {amount:.2f}" for currency, amount in summary.items()]
    return "\n".join(report_lines)


def transactions_by_date(transactions: List[Dict], date: str) -> List[Dict]:
    return [t for t in transactions if t.get("date", "").startswith(date)]
