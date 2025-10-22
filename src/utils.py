import json
import logging
from datetime import datetime
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def load_excel(path: str) -> pd.DataFrame:
    """#pandas #logging
    Загружает данные из Excel.
    """
    logging.info(f"Загрузка Excel-файла: {path}")
    try:
        df = pd.read_excel(path)
        return df
    except FileNotFoundError:
        logging.warning(f"Файл {path} не найден, возвращаю пустой DataFrame.")
        return pd.DataFrame()
    except Exception as e:
        logging.error(f"Ошибка при загрузке Excel: {e}")
        return pd.DataFrame()


def load_user_settings(path: str = "data/user_settings.json") -> dict:
    """#json #logging
    Загружает пользовательские настройки.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("Файл user_settings.json не найден, возвращаю пустой словарь.")
        return {}
    except json.JSONDecodeError:
        logging.error("Ошибка декодирования JSON в user_settings.json")
        return {}


def greeting_by_time(date_str: str) -> str:
    """#datetime #logging
    Возвращает приветствие по времени суток.
    """
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        hour = dt.hour
        if 5 <= hour < 12:
            return "Доброе утро!"
        elif 12 <= hour < 18:
            return "Добрый день!"
        elif 18 <= hour < 23:
            return "Добрый вечер!"
        else:
            return "Доброй ночи!"
    except Exception as e:
        logging.error(f"Ошибка при обработке времени: {e}")
        return "Здравствуйте!"
