import asyncio
import time

from db import employees, products
from csv_reader import read_csv
from doc_reader import read_docx
from pdf_reader import read_pdf
from web_reader import read_webpage


async def fetch_all():
    tasks = [
        # PostgreSQL
        asyncio.to_thread(employees),
        asyncio.to_thread(products),

        # CSV Files
        asyncio.to_thread(read_csv, "data/csv/sales.csv"),
        asyncio.to_thread(read_csv, "data/csv/customers.csv"),

        # DOCX Files
        asyncio.to_thread(read_docx, "data/docx/report.docx"),
        asyncio.to_thread(read_docx, "data/docx/meeting.docx"),

        # PDF Files
        asyncio.to_thread(read_pdf, "data/pdf/invoice.pdf"),
        asyncio.to_thread(read_pdf, "data/pdf/manual.pdf"),

        # Web Pages
        asyncio.to_thread(read_webpage, "https://example.com"),
        asyncio.to_thread(read_webpage, "https://www.python.org"),
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
    }


async def main():
    start = time.perf_counter()

    all_data = await fetch_all()

    end = time.perf_counter()

    print("\n" + "=" * 70)
    print("ALL DATA LOADED")
    print("=" * 70)

    for key, value in all_data.items():
        print(f"\n========== {key.upper()} ==========")

        if isinstance(value, list):
            for row in value:
                print(row)
        else:
            print(value)

    print("\n" + "=" * 70)
    print(f"Execution Time: {end - start:.2f} seconds")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())