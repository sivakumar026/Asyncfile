from docx import Document
import time

def read_docx(file_path):
    time.sleep(1)
    document = Document(file_path)

    text = []

    for para in document.paragraphs:
        text.append(para.text)

    return "\n".join(text)


if __name__ == "__main__":
    report = read_docx("data/docx/report.docx")
    meeting = read_docx("data/docx/meeting.docx")

    print("===== REPORT =====")
    print(report)

    print("===== MEETING =====")
    print(meeting)