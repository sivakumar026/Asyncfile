import asyncio
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


async def fetch_all():

    tasks = [

        # Database
        asyncio.to_thread(employees),
        asyncio.to_thread(products),

        # CSV
        asyncio.to_thread(read_csv, "../data/csv/sales.csv"),
        asyncio.to_thread(read_csv, "../data/csv/customers.csv"),

        # DOCX
        asyncio.to_thread(read_docx, "../data/docx/report.docx"),
        asyncio.to_thread(read_docx, "../data/docx/meeting.docx"),

        # PDF
        asyncio.to_thread(read_pdf, "../data/pdf/invoice.pdf"),
        asyncio.to_thread(read_pdf, "../data/pdf/manual.pdf"),

        # Web
        asyncio.to_thread(read_webpage, "https://example.com"),
        asyncio.to_thread(read_webpage, "https://www.python.org"),

        # JSON
        asyncio.to_thread(reader_json, "../data/json/employees.json"),

        # HTML
        asyncio.to_thread(read_html, "../data/html/index.html"),

        # CSS
        asyncio.to_thread(read_css, "../data/css/style.css"),

        # TXT
        asyncio.to_thread(read_txt, "../data/txt/project_objectives.txt"),

        # Excel
        asyncio.to_thread(read_excel, "../data/excel/employees.xlsx"),
    ]

    results = await asyncio.gather(*tasks)

    return {

        "employees": results[0],
        "products": results[1],

        "sales_csv": results[2],
        "customers_csv": results[3],

        "report_doc": results[4],
        "meeting_doc": results[5],

        "invoice_pdf": results[6],
        "manual_pdf": results[7],

        "example_page": results[8],
        "python_page": results[9],

        "employees_json": results[10],

        "html_page": results[11],

        "css_file": results[12],

        "notes_txt": results[13],

        "employees_excel": results[14],
    }


async def main():

    start = time.perf_counter()

    all_data = await fetch_all()

    end = time.perf_counter()

    print("\n" + "=" * 70)
    print("ALL DATA LOADED")
    print("=" * 70)

    for key, value in all_data.items():

        print(f"\n===== {key.upper()} =====")

        if isinstance(value, list):
            for row in value:
                print(row)
        else:
            print(value)

    print("\n" + "=" * 70)
    print(f"Concurrent Fetch Time: {end - start:.4f} seconds")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())