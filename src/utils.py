import json
import logging
import os
from datetime import datetime
from typing import Any, Dict, List

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def load_excel(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        logging.error(f"Файл {path} не найден")
        raise FileNotFoundError(f"Файл {path} не найден")
    return pd.read_excel(path)


def load_user_settings(path: str = "user_settings.json") -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def greeting_by_time(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    hour = dt.hour
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 24:
        return "Добрый вечер"
    return "Доброй ночи"
