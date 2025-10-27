import json
from datetime import datetime
from pathlib import Path

def load_user_settings(file_path: str = "user_settings.json") -> dict:
    """
    Загружает пользовательские настройки из JSON файла.

    Args:
        file_path (str): путь к файлу настроек.

    Returns:
        dict: словарь с настройками пользователя.
    """
    path = Path(file_path)
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def greeting_by_time(dt: datetime) -> str:
    """
    Возвращает приветствие в зависимости от времени суток.

    Args:
        dt (datetime): текущее время.

    Returns:
        str: приветствие ("Доброе утро", "Добрый день", "Добрый вечер", "Доброй ночи").
    """
    hour = dt.hour
    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"
