def display_cashback(result: dict):
    """
    Выводит результат анализа в консоль.
    """
    if not result:
        print("Нет данных для отображения.")
        return
    print("\n=== Отчет по кешбэку ===")
    for category, cashback in result.items():
        print(f"{category}: {cashback:.2f} руб.")
