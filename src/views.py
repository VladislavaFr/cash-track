import json
import logging
from datetime import datetime
import pandas as pd
from src.utils import load_excel, greeting_by_time, load_user_settings
from src.services import get_currency_rates, get_stock_prices

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def get_main_page_data(date_str: str) -> str:
    """#json #datetime #pandas #logging
    Возвращает JSON-ответ для страницы «Главная» с основными показателями за месяц.
    """
    logging.info("Формирование данных для главной страницы...")
    try:
        df = load_excel("data/operations.xlsx")
        if df.empty:
            raise ValueError("Файл operations.xlsx пуст или не найден")

        current_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        month_start = current_date.replace(day=1)

        df["Дата операции"] = pd.to_datetime(df["Дата операции"])
        df_month = df[(df["Дата операции"] >= month_start) & (df["Дата операции"] <= current_date)]

        total_sum = float(df_month["Сумма операции"].sum())
        avg_amount = float(df_month["Сумма операции"].mean())
        cashback = float(df_month.get("Кешбэк", pd.Series(0)).sum())

        top_categories = (
            df_month["Категория"].value_counts().head(3).to_dict()
            if "Категория" in df_month
            else {}
        )

        settings = load_user_settings()
        currencies = settings.get("user_currencies", [])
        stocks = settings.get("user_stocks", [])

        result = {
            "greeting": greeting_by_time(date_str),
            "total_sum": round(total_sum, 2),
            "average_amount": round(avg_amount, 2),
            "cashback": round(cashback, 2),
            "top_categories": top_categories,
            "currency_rates": get_currency_rates(currencies),
            "stock_prices": get_stock_prices(stocks),
        }

        logging.info("Главная страница успешно собрана.")
        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        logging.error(f"Ошибка при формировании данных для главной страницы: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False, indent=2)
