import pytest
from unittest.mock import patch
from src.views import main_page_response

def test_main_page_response(sample_settings):
    with patch("src.views.load_user_settings", return_value=sample_settings):
        with patch("src.views.get_currency_rates", return_value=[{"currency": "USD", "rate": 70.0}]):
            with patch("src.views.get_stock_prices", return_value=[{"stock": "AAPL", "price": 150.0}]):
                response = main_page_response("2025-10-23 12:00:00")
                assert response["greeting"] == "Добрый день"
                assert response["currency_rates"][0]["currency"] == "USD"
                assert response["stock_prices"][0]["stock"] == "AAPL"
