import json
import time


def reader_json(file_path):
    time.sleep(1)

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


if __name__ == "__main__":
    json_data = reader_json("../data/json/employees.json")

    print("===== JSON FILE =====")

    for employee in json_data:
        print(employee)