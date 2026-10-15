import pymupdf
import pytesseract
from PIL import Image
import io

pdf_path="EY_Scanned_PDF_OCR_Practice.pdf"
doc=pymupdf.open(pdf_path)
print("PDF opened successfully!")
print(doc)
print("Number of pages: ",len(doc))
all_text=""
for page_number, page in enumerate(doc,start=1):
    pix=page.get_pixmap(matrix=pymupdf.Matrix(2,2))
    image_bytes=pix.tobytes("png")
    image=Image.open(io.BytesIO(image_bytes))
    text=pytesseract.image_to_string(image)
    all_text+=text
    print(f"\n--- OCR Text: Page {page_number} ---")
    print(text)
doc.close()
full_text="\n".join(all_text)
lower_text=full_text.lower()

print("Forklift FL-17 detected:","forklift fl-17" in lower_text)

print("Word 'injuries' found:","injuries" in lower_text)

print("Lines mentioning Inspection:")
for line in full_text.splitlines():
    if "inspection" in line.lower():
        print(line)

with open("ocr_result.txt","w",encoding="utf-8") as file:
    file.write(full_text)
print("Text saved successfully")

inspection_count=lower_text.count("inspection")
print("Number of times inspection appears:",inspection_count)

print("Lines  containing Loading Bay:")
for line in full_text.splitlines():
    if "Loading Bay" in line.lower():
        print(line)
