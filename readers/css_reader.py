import time


def read_css(file_path):
    time.sleep(1)

    with open(file_path, "r", encoding="utf-8") as file:
        css = file.read()

    return css


if __name__ == "__main__":
    style = read_css("../data/css/style.css")

    print("===== CSS FILE =====")
    print(style)