import pandas as pd
import pytest
from src.views import generate_transaction_report


@pytest.fixture
def sample_excel(tmp_path):
    data = pd.DataFrame(
        [
            {"currency": "USD", "amount": 100, "date": "2025-09-27"},
            {"currency": "EUR", "amount": 200, "date": "2025-09-27"},
        ]
    )
    file = tmp_path / "transactions.xlsx"
    data.to_excel(file, index=False)
    return file


def test_generate_transaction_report(sample_excel):
    report = generate_transaction_report(str(sample_excel))
    assert "USD: 100.00" in report
    assert "EUR: 200.00" in report
