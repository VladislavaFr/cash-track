import pytest
from src.utils import greeting_by_time


def test_greeting_morning():
    assert greeting_by_time("2025-09-27 08:00:00") == "Доброе утро"


def test_greeting_afternoon():
    assert greeting_by_time("2025-09-27 15:00:00") == "Добрый день"


def test_greeting_evening():
    assert greeting_by_time("2025-09-27 20:00:00") == "Добрый вечер"


def test_greeting_night():
    assert greeting_by_time("2025-09-27 02:00:00") == "Доброй ночи"
