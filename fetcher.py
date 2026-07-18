from db import employees, products
from csv_reader import read_csv
from doc_reader import read_docx
from pdf_reader import read_pdf
from web_reader import read_webpage


def fetch_all():
    data = {
        "employees": employees,
        "products": products,

        "sales_csv": read_csv("data/csv/sales.csv"),
        "customers_csv": read_csv("data/csv/customers.csv"),

        "report_doc": read_docx("data/docx/report.docx"),
        "meeting_doc": read_docx("data/docx/meeting.docx"),

        "invoice_pdf": read_pdf("data/pdf/invoice.pdf"),
        "manual_pdf": read_pdf("data/pdf/manual.pdf"),

        "example_page": read_webpage("https://example.com"),
        "python_page": read_webpage("https://www.python.org")
    }

    return data


if __name__ == "__main__":
    all_data = fetch_all()

    for source, content in all_data.items():
        print(f"\n========== {source.upper()} ==========")
        print(content)