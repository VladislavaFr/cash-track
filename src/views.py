from src.utils import load_excel, greeting_by_time
from src.reports import summarize_transactions, format_transaction_report


def generate_transaction_report(file_path: str) -> str:
    transactions = load_excel(file_path).to_dict(orient="records")
    summary = summarize_transactions(transactions)
    report = format_transaction_report(summary)
    return report
