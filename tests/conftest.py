import pytest
import pandas as pd
from datetime import datetime
from src.services import get_currency_rates, get_stock_prices

@pytest.fixture
def sample_transactions():
    return [
        {"currency": "USD", "amount": 100, "category": "Переводы", "description": "Перевод +7 999 123-45-67", "Дата операции": "2025-10-01", "Сумма операции": 1000, "Категория": "Покупки"},
        {"currency": "USD", "amount": 50, "category": "Питание", "description": "Кафе", "Дата операции": "2025-10-02", "Сумма операции": 500, "Категория": "Питание"},
        {"currency": "EUR", "amount": 200, "category": "Покупки", "description": "Магазин", "Дата операции": "2025-10-03", "Сумма операции": 1500, "Категория": "Покупки"},
    ]

@pytest.fixture
def sample_dataframe(sample_transactions):
    df = pd.DataFrame(sample_transactions)
    return df

@pytest.fixture
def sample_settings():
    return {"user_currencies": ["USD", "EUR"], "user_stocks": ["AAPL", "GOOG"]}
