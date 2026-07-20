import time

from db import employees, products
from csv_reader import read_csv
from doc_reader import read_docx
from pdf_reader import read_pdf
from web_reader import read_webpage

from reader_json import reader_json
from html_reader import read_html
from css_reader import read_css
from txt_reader import read_txt
from excel_reader import read_excel


def fetch_all():
    data = {
        # Database
        "employees": employees(),
        "products": products(),

        # CSV
        "sales_csv": read_csv("../data/csv/sales.csv"),
        "customers_csv": read_csv("../data/csv/customers.csv"),

        # DOCX
        "report_doc": read_docx("../data/docx/report.docx"),
        "meeting_doc": read_docx("../data/docx/meeting.docx"),

        # PDF
        "invoice_pdf": read_pdf("../data/pdf/invoice.pdf"),
        "manual_pdf": read_pdf("../data/pdf/manual.pdf"),

        # Web
        "example_page": read_webpage("https://example.com"),
        "python_page": read_webpage("https://www.python.org"),

        # JSON
        "employees_json": reader_json("../data/json/employees.json"),

        # HTML
        "html_page": read_html("../data/html/index.html"),

        # CSS
        "css_file": read_css("../data/css/style.css"),

        # TXT
        "notes_txt": read_txt("../data/txt/project_objectives.txt"),

        # Excel
        "employees_excel": read_excel("../data/excel/employees.xlsx"),
    }

    return data


if __name__ == "__main__":

    start_time = time.perf_counter()

    all_data = fetch_all()

    end_time = time.perf_counter()

    for source, content in all_data.items():
        print(f"\n===== {source.upper()} =====")
        print(content)

    print(f"\nSequential Fetch Time: {end_time - start_time:.4f} seconds") 