import pytest
import pandas as pd
from src.services import cashback_analysis
from src.utils import sum_cashback, filter_transactions

@pytest.fixture
def sample_df():
    data = {
        "Дата операции": ["2025-09-01", "2025-09-05", "2025-08-20", "2025-09-10"],
        "Категория": ["Супермаркеты", "Кафе", "Супермаркеты", "Супермаркеты"],
        "Кешбэк": [12.5, 5, 8, 3.5]
    }
    return pd.DataFrame(data)

def test_filter_transactions(sample_df):
    filtered = filter_transactions(sample_df, 2025, 9)
    assert len(filtered) == 3

def test_sum_cashback(sample_df):
    filtered = filter_transactions(sample_df, 2025, 9)
    result = sum_cashback(filtered)
    assert result["Супермаркеты"] == 16.0
    assert result["Кафе"] == 5
