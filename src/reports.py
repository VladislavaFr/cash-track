from typing import List, Dict
import pandas as pd

def summarize_transactions(transactions: List[Dict]) -> Dict[str, float]:
    summary = {}
    for transaction in transactions:
        currency = transaction.get("currency", "RUB")
        amount = transaction.get("amount", 0)
        summary[currency] = summary.get(currency, 0) + amount
    return summary

def format_transaction_report(summary: Dict[str, float]) -> str:
    return "\n".join(f"{currency}: {amount:.2f}" for currency, amount in summary.items())

def spending_by_category(df: pd.DataFrame, category: str, date: str) -> pd.DataFrame:
    filtered = df[(df["Категория"] == category) & (df["Дата операции"] == date)]
    return filtered

def spending_by_weekday(df: pd.DataFrame, date: str) -> pd.DataFrame:
    df["weekday"] = pd.to_datetime(df["Дата операции"]).dt.day_name()
    return df[df["Дата операции"] == date]

def spending_by_workday(df: pd.DataFrame, date: str) -> pd.DataFrame:
    df["weekday"] = pd.to_datetime(df["Дата операции"]).dt.day_name()
    return df[(df["weekday"].isin(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])) & (df["Дата операции"] == date)]
