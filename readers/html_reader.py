import time
from bs4 import BeautifulSoup


def read_html(file_path):
    time.sleep(1)

    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.string if soup.title else "No Title"

    paragraphs = soup.find_all("p")

    text = ""

    for p in paragraphs:
        text += p.get_text() + "\n"

    return {
        "title": title,
        "content": text
    }


page = read_html("../data/html/index.html")

print("===== HTML FILE =====")
print(page)