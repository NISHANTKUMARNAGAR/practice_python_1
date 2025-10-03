#for merging two pdf
"""from PyPDF2 import PdfReader,PdfWriter

pw=PdfWriter()

for i in ['test.pdf','test1.pdf']:
    r=PdfReader(i)
    for p in r.pages:
        pw.add_page(p)

with open("merged.pdf",'wb') as of:
    pw.write(of)"""

#for merging the pdf using append instead of merging individual pages
"""from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()"""


#for reading  pdf file data and its metadata
'''import PyPDF2
with open('test.pdf','rb') as t:
    reader=PyPDF2.PdfReader(t)

    print(f"total_pages={len(reader.pages)}")

    for i in reader.pages:
        page=i
        print(page.extract_text())

    m=reader.metadata
    print(m.author)
    print(m.title)
    print(m.creation_date)'''

    
