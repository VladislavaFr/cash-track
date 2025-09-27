from src.reports import summarize_transactions, format_transaction_report


def test_summarize_transactions():
    transactions = [
        {"currency": "USD", "amount": 100},
        {"currency": "USD", "amount": 50},
        {"currency": "EUR", "amount": 200},
    ]
    summary = summarize_transactions(transactions)
    assert summary == {"USD": 150, "EUR": 200}


def test_format_transaction_report():
    summary = {"USD": 150, "EUR": 200}
    report = format_transaction_report(summary)
    assert "USD: 150.00" in report
    assert "EUR: 200.00" in report
