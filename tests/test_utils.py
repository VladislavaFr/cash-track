from datetime import datetime
import pytest
from src.utils import greeting_by_time, load_user_settings
import json
from pathlib import Path

def test_greeting_by_time():
    assert greeting_by_time(datetime.strptime("2025-09-27 08:00:00", "%Y-%m-%d %H:%M:%S")) == "Доброе утро"
    assert greeting_by_time(datetime.strptime("2025-09-27 15:00:00", "%Y-%m-%d %H:%M:%S")) == "Добрый день"
    assert greeting_by_time(datetime.strptime("2025-09-27 20:00:00", "%Y-%m-%d %H:%M:%S")) == "Добрый вечер"
    assert greeting_by_time(datetime.strptime("2025-09-27 02:00:00", "%Y-%m-%d %H:%M:%S")) == "Доброй ночи"

def test_load_user_settings(tmp_path):
    file = tmp_path / "settings.json"
    data = {"user_currencies": ["USD"]}
    file.write_text(json.dumps(data), encoding="utf-8")
    settings = load_user_settings(str(file))
    assert settings["user_currencies"] == ["USD"]

def test_load_user_settings_nonexistent():
    result = load_user_settings("nonexistent.json")
    assert result == {}
