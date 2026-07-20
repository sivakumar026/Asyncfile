import time


def read_txt(file_path):
    time.sleep(1)

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


notes = read_txt("../data/txt/project_objectives.txt")

print("===== TEXT FILE =====")
print(notes)