import json

def save_report_json(result: dict, filename: str):
    """
    Сохраняет отчет в JSON.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print(f"Отчет сохранен в {filename}")
