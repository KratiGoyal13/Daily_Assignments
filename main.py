import pymupdf
doc=pymupdf.open("EY_Digital_PDF_Practice.pdf")
print("PDF  opened successfully")
print(doc)
print("Number of pages:",len(doc))

page1=doc[0].get_text()
print("Page 1 text is:")
print(page1)

all_text=""
for page in doc:
    all_text+=page.get_text()+"\n"
print("All pages text:")
print(all_text)

print("Maintenance found:","maintenance" in all_text.lower())

print("V303 Appears:",all_text.count("V303"),"times")

if len(doc)>=2:
    page2=doc[1].get_text()
    print("Page 2 text is:")
    print(page2)
else:
    print("Page 2 does not exist.")

with open("EY_Digital_PDF_Practice_duplicate.text", "w",encoding="utf-8") as file:
    file.write(all_text)
print("Text saved successfully")
doc.close()