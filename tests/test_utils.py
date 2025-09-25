import pytest
from src.utils import get_greeting

def test_get_greeting():
    from datetime import datetime
    assert get_greeting(datetime.strptime("2025-09-25 08:00:00", "%Y-%m-%d %H:%M:%S")) == "Доброе утро"
    assert get_greeting(datetime.strptime("2025-09-25 14:00:00", "%Y-%m-%d %H:%M:%S")) == "Добрый день"
