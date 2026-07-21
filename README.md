# ⚡ Concurrent Data Fetcher

A Python project that demonstrates the **performance difference between sequential and concurrent I/O** by fetching data from multiple heterogeneous sources — files, databases, and the web — and comparing execution times side by side in an interactive Streamlit dashboard.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)

---

## 📖 Overview

Real-world applications often need to pull data from many sources: databases, CSV files, PDFs, web pages, and more. Doing this **sequentially** means each source blocks the next, leading to long wait times. This project showcases how Python's `asyncio` (with `asyncio.to_thread` for blocking I/O) can run all fetches **concurrently**, dramatically reducing total execution time.

### Key Highlights

- **Side-by-side comparison** — Sequential vs. Concurrent fetch with live timing metrics.
- **9 different reader modules** — Covering databases, files, and web scraping.
- **Interactive Streamlit UI** — One-click fetch with expandable result panels and a performance summary.
- **CI/CD pipeline** — Automated linting and import verification via GitHub Actions.

---

## 🗂️ Project Structure

```
Async/
├── .github/
│   └── workflows/
│       └── python-ci.yml        # GitHub Actions CI pipeline
├── data/                        # Sample data files organized by format
│   ├── css/                     #   └── style.css
│   ├── csv/                     #   └── sales.csv, customers.csv
│   ├── docx/                    #   └── report.docx, meeting.docx
│   ├── excel/                   #   └── employees.xlsx
│   ├── html/                    #   └── index.html
│   ├── json/                    #   └── employees.json
│   ├── pdf/                     #   └── invoice.pdf, manual.pdf
│   └── txt/                     #   └── project_objectives.txt
├── readers/                     # Core application modules
│   ├── app.py                   # Streamlit dashboard (entry point)
│   ├── fetcher.py               # Sequential data fetcher
│   ├── async_fetcher.py         # Concurrent data fetcher (asyncio)
│   ├── db.py                    # PostgreSQL database reader
│   ├── csv_reader.py            # CSV file reader (pandas)
│   ├── excel_reader.py          # Excel file reader (pandas + openpyxl)
│   ├── pdf_reader.py            # PDF file reader (PyPDF2)
│   ├── doc_reader.py            # DOCX file reader (python-docx)
│   ├── reader_json.py           # JSON file reader
│   ├── html_reader.py           # HTML file reader (BeautifulSoup)
│   ├── css_reader.py            # CSS file reader
│   ├── txt_reader.py            # Plain text file reader
│   └── web_reader.py            # Web page scraper (requests + BeautifulSoup)
├── requirements.txt             # Python dependencies
├── utils.py                     # Utility helpers
└── README.md
```

---

## 🔌 Supported Data Sources

| Source | Module | Library | Description |
|--------|--------|---------|-------------|
| **PostgreSQL** | `db.py` | `psycopg2` | Reads `employees` and `products` tables |
| **CSV** | `csv_reader.py` | `pandas` | Parses CSV files into DataFrames |
| **Excel** | `excel_reader.py` | `pandas` + `openpyxl` | Reads `.xlsx` files as list of dicts |
| **PDF** | `pdf_reader.py` | `PyPDF2` | Extracts text from all pages |
| **DOCX** | `doc_reader.py` | `python-docx` | Extracts paragraph text |
| **JSON** | `reader_json.py` | `json` (stdlib) | Loads JSON data |
| **HTML** | `html_reader.py` | `BeautifulSoup` | Parses title and paragraph content |
| **CSS** | `css_reader.py` | — (stdlib) | Reads raw CSS text |
| **TXT** | `txt_reader.py` | — (stdlib) | Reads plain text files |
| **Web Pages** | `web_reader.py` | `requests` + `BeautifulSoup` | Scrapes live web pages |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **PostgreSQL** — running locally with a `company_db` database containing `employees` and `products` tables.

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/sivakumar026/Asyncfile.git
   cd Asyncfile
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**

   Update the connection details in [`readers/db.py`](readers/db.py) to match your PostgreSQL setup:

   ```python
   def get_connection():
       return psycopg2.connect(
           host="localhost",
           database="company_db",
           user="your_username",
           password="your_password"
       )
   ```

### Running the Dashboard

```bash
cd readers
streamlit run app.py
```

Click the **"Fetch Data"** button in the browser to trigger both sequential and concurrent fetches and compare their performance.

### Running Fetchers Directly (CLI)

```bash
# Sequential fetch
cd readers
python fetcher.py

# Concurrent fetch
cd readers
python async_fetcher.py
```

---

## ⚙️ How It Works

### Sequential Fetching (`fetcher.py`)

Each data source is read **one after another**. Every reader includes a simulated `time.sleep(1)` delay to represent real-world I/O latency. With 15 data sources, the sequential approach takes **~15 seconds**.

```
Source 1 → Source 2 → Source 3 → ... → Source 15
                                              ↓
                                        ~15 seconds
```

### Concurrent Fetching (`async_fetcher.py`)

All data sources are read **simultaneously** using `asyncio.gather()` with `asyncio.to_thread()` to offload blocking I/O to separate threads. Total time drops to roughly **~1 second** — the duration of a single `time.sleep(1)`.

```
Source 1  ─┐
Source 2  ─┤
Source 3  ─┼── asyncio.gather() ── ~1 second
...        │
Source 15 ─┘
```

---

## 🧪 CI / CD

The project includes a [GitHub Actions workflow](.github/workflows/python-ci.yml) that runs on every push and pull request to `main`/`master`:

| Step | Description |
|------|-------------|
| **Matrix testing** | Runs against Python 3.10, 3.11, and 3.12 |
| **Dependency caching** | Caches pip packages for faster builds |
| **Linting** | `flake8` checks for syntax errors and code quality |
| **Import verification** | Validates that all reader modules import correctly |

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Interactive web dashboard |
| `pandas` | CSV and Excel data processing |
| `PyPDF2` | PDF text extraction |
| `python-docx` | DOCX document reading |
| `requests` | HTTP requests for web scraping |
| `beautifulsoup4` | HTML/web page parsing |
| `psycopg2-binary` | PostgreSQL database driver |
| `openpyxl` | Excel `.xlsx` file support |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m "Add my feature"`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ using Python &amp; Streamlit
</p>
