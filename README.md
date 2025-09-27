# Cash Track

**Cash Track** — приложение для анализа транзакций и кешбэка на Python с использованием pandas и pytest.  
Проект позволяет загружать данные из Excel, фильтровать по дате и категории, суммировать кешбэк, выводить результаты в консоль и сохранять отчёты в JSON.

---

## 📁 Структура проекта

```
cash-track/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   ├── views.py
│   ├── services.py
│   └── reports.py
├── data/
│   └── operations.xlsx
├── tests/
│   ├── __init__.py
│   ├── test_utils.py
│   ├── test_views.py
│   ├── test_services.py
│   └── test_reports.py
├── .gitignore
├── .env
├── .env_template
├── .flake8
├── pyproject.toml
├── poetry.lock
├── README.md
└── user_settings.json
```

---

## 🛠 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/VladislavaFr/cash-track.git
cd cash-track
```

2. Установите Python 3.13+.

3. Установите Poetry (если не установлен):

```bash
pip install poetry
```

4. Установите зависимости и активируйте виртуальное окружение:

```bash
poetry install
poetry shell
```

---

## 💻 Запуск проекта

```bash
python src/main.py
```

---

## 🧪 Тестирование

```bash
pytest tests/
```

---

## 🔧 Настройка

- `user_settings.json` — пользовательские настройки фильтрации  
- `.env` / `.env_template` — переменные окружения  

---

## 📄 Лицензия

Проект не имеет лицензии.

---

## ✅ Особенности проекта

- Фильтрация по году и месяцу  
- Суммирование кешбэка по категориям  
- Консольный вывод и отчёты в JSON  
- Лёгкая расширяемость под веб-интерфейс и Telegram-бот
