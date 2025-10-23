from src.services import get_currency_rates, get_stock_prices


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
