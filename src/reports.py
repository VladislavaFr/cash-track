import json
import logging
from datetime import datetime
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def spending_by_weekday(df: pd.DataFrame, date: str | None = None) -> str:
    """#json #datetime #pandas #logging
    Генерирует отчёт о тратах по дням недели.
    """
    logging.info("Создание отчёта по тратам по дням недели...")
    try:
        df["Дата операции"] = pd.to_datetime(df["Дата операции"])

        if date:
            end_date = datetime.strptime(date, "%Y-%m-%d")
            df = df[df["Дата операции"] <= end_date]

        df["weekday"] = df["Дата операции"].dt.day_name(locale="ru")
        report = df.groupby("weekday")["Сумма операции"].sum().to_dict()

        logging.info("Отчёт по дням недели создан успешно.")
        return json.dumps(report, ensure_ascii=False, indent=2)

    except Exception as e:
        logging.error(f"Ошибка при создании отчёта по дням недели: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False, indent=2)
