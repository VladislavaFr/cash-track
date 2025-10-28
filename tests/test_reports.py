import pytest
from src.reports import spending_by_category, spending_by_weekday, spending_by_workday

def test_spending_by_category(sample_dataframe):
    df = spending_by_category(sample_dataframe, category="Покупки", date="2025-10-03")
    assert not df.empty
    assert "Сумма операции" in df.columns

def test_spending_by_weekday(sample_dataframe):
    df = spending_by_weekday(sample_dataframe, date="2025-10-03")
    assert "weekday" in df.columns

def test_spending_by_workday(sample_dataframe):
    df = spending_by_workday(sample_dataframe, date="2025-10-03")
    assert not df.empty
