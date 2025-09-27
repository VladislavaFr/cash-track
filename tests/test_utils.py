import pytest
import pandas as pd
from src.utils import read_transactions_from_excel

def test_read_transactions(tmp_path):
    file = tmp_path / "test.xlsx"
    df = pd.DataFrame({
        "Дата операции": ["2025-09-01"],
        "Категория": ["Супермаркеты"],
        "Кешбэк": [10]
    })
    df.to_excel(file, index=False)
    read_df = read_transactions_from_excel(str(file))
    assert not read_df.empty
    assert read_df.iloc[0]["Кешбэк"] == 10
