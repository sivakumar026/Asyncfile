import requests
from bs4 import BeautifulSoup


def read_webpage(url):
    response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No Title"

    paragraphs = soup.find_all("p")

    text = ""

    for p in paragraphs[:3]:  # First 3 paragraphs
        text += p.get_text() + "\n"

    return {
        "title": title,
        "content": text
    }


page1 = read_webpage("https://www.indmoney.com/")
page2 = read_webpage("https://www.indmoney.com/")

print("===== EXAMPLE =====")
print(page1)

print("\n===== Example =====")
print(page2)