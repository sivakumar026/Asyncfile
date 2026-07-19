from PyPDF2 import PdfReader
import time

def read_pdf(file_path):
    time.sleep(1)
    reader = PdfReader(file_path)

    text = []

    for page in reader.pages:
        text.append(page.extract_text())

    return "\n".join(text)


invoice = read_pdf("data/pdf/invoice.pdf")
manual = read_pdf("data/pdf/manual.pdf")

print("===== INVOICE =====")
print(invoice)

print("===== MANUAL =====")
print(manual)