import pandas as pd
import time

def read_csv(file_path):
    time.sleep(1)
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    sales = read_csv("data/csv/sales.csv")
    customers = read_csv("data/csv/customers.csv")

    print("===== SALES =====")
    print(sales)

    print("\n===== CUSTOMERS =====")
    print(customers)