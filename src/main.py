from src.services import cashback_analysis
from src.views import display_cashback
from src.reports import save_report_json

def main():
    file_path = "data/operations.xlsx"
    year = 2025
    month = 9

    result = cashback_analysis(file_path, year, month)
    display_cashback(result)
    save_report_json(result, f"reports/cashback_{year}_{month}.json")

if __name__ == "__main__":
    main()