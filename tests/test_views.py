import pytest
import pandas as pd
from src.views import main_page


def test_main_page_structure():
    df = pd.DataFrame()  # пустой DataFrame для теста
    result = main_page("2025-09-25 12:00:00", df)

    assert "greeting" in result
    assert "cards" in result
    assert "top_transactions" in result
    assert "currency_rates" in result
    assert "stock_prices" in result
