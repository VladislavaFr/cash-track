import unittest
from unittest.mock import patch
from datetime import datetime
from src.views import main_page_response


class TestMainPageResponse(unittest.TestCase):
    @patch("src.views.load_user_settings")
    @patch("src.views.get_currency_rates")
    @patch("src.views.get_stock_prices")
    def test_main_page_response(
        self, mock_get_stocks, mock_get_currencies, mock_load_settings
    ):
        mock_load_settings.return_value = {
            "user_currencies": ["USD"],
            "user_stocks": ["AAPL"],
        }
        mock_get_currencies.return_value = [{"currency": "USD", "rate": 70.0}]
        mock_get_stocks.return_value = [{"stock": "AAPL", "price": 150.0}]

        response = main_page_response("2025-10-23 12:00:00")
        self.assertEqual(response["greeting"], "Добрый день")
        self.assertEqual(response["currency_rates"][0]["currency"], "USD")
        self.assertEqual(response["stock_prices"][0]["stock"], "AAPL")


if __name__ == "__main__":
    unittest.main()
