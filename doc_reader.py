from docx import Document

def read_docx(file_path):
    document = Document(file_path)

    text = []

    for para in document.paragraphs:
        text.append(para.text)

    return "\n".join(text)


report = read_docx("data/docx/report.docx")
meeting = read_docx("data/docx/meeting.docx")

print("===== REPORT =====")
print(report)

print("===== MEETING =====")
print(meeting)