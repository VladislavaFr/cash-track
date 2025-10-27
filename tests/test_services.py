import pytest
from src.services import get_currency_rates, get_stock_prices, simple_search, investment_bank

@pytest.fixture
def sample_transactions():
    return [
        {"date": "2025-10-01", "amount": 100, "currency": "USD", "category": "Переводы", "description": "Перевод +7 999 123-45-67"},
        {"date": "2025-10-05", "amount": 50, "currency": "USD", "category": "Покупки", "description": "Кафе"},
        {"date": "2025-10-10", "amount": 200, "currency": "EUR", "category": "Покупки", "description": "Магазин"},
        {"date": "2025-10-15", "amount": 300, "currency": "RUB", "category": "Развлечения", "description": "Кино"},
    ]

def test_get_currency_rates():
    result = get_currency_rates(["USD"])
    assert isinstance(result, list)
    assert "currency" in result[0]
    assert "rate" in result[0]

def test_get_stock_prices():
    result = get_stock_prices(["AAPL"])
    assert isinstance(result, list)
    assert "stock" in result[0]
    assert "price" in result[0]

def test_simple_search(sample_transactions):
    results = simple_search("кафе", sample_transactions)
    assert len(results) == 1
    assert results[0]["description"] == "Кафе"

def test_investment_bank(sample_transactions):
    total_usd = investment_bank("2025-10", sample_transactions, currency="USD")
    assert isinstance(total_usd, float)
    assert total_usd == 150.0  # 100 + 50
