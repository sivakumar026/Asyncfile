import pandas as pd
import time


def read_excel(file_path):
    time.sleep(1)

    df = pd.read_excel(file_path)

    return df.to_dict(orient="records")


if __name__ == "__main__":
    excel_data = read_excel("../data/excel/employees.xlsx")

    print("===== EXCEL FILE =====")

    for row in excel_data:
        print(row)