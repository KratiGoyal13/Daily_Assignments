from pypdf import PdfReader
reader=PdfReader("EY_Digital_PDF_Practice.pdf")
print("PDF opened sucessfully!")

print("Number of pages:",len(reader.pages))
page1=reader.pages[0].extract_text()or""
print("Page 1 extracted successfully")
print(page1)

page2=""
if len(reader.pages)>=2:
    page2=reader.pages[1].extract_text() or ""
print("Page 2 extracted successfully")
print(page2)

combined_text=page1+ "\n" +page2
print("Combined text extracted successfully")
print(combined_text)

print("NorthStar Maintenance found:","NorthStar Maintenance" in combined_text)

print("vendor count:",combined_text.lower().count("vendor"))

with open("pypdf_output.txt", "w",encoding='utf-8') as file:
    file.write(combined_text)
print("Text saved successfully")

