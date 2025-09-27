import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional

def read_transactions_from_excel(file_path: str) -> pd.DataFrame:
    """
    Чтение Excel файла с транзакциями.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        df.fillna(0, inplace=True)
        return df
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return pd.DataFrame()

def filter_transactions(df: pd.DataFrame, year: Optional[int]=None, month: Optional[int]=None) -> pd.DataFrame:
    """
    Фильтрует транзакции по году и месяцу.
    """
    if 'Дата операции' not in df.columns:
        raise ValueError("В таблице нет колонки 'Дата операции'")
    df['Дата операции'] = pd.to_datetime(df['Дата операции'])
    if year:
        df = df[df['Дата операции'].dt.year == year]
    if month:
        df = df[df['Дата операции'].dt.month == month]
    return df

def sum_cashback(df: pd.DataFrame) -> Dict[str, float]:
    """
    Суммирует кешбэк по категориям.
    """
    if 'Категория' not in df.columns or 'Кешбэк' not in df.columns:
        raise ValueError("В таблице нет колонки 'Категория' или 'Кешбэк'")
    grouped = df.groupby('Категория')['Кешбэк'].sum()
    return grouped.to_dict()
