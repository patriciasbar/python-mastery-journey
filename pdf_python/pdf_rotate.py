import PyPDF2 as pdf2

filename = "sample_files\dummy.pdf"

with open(filename, 'rb') as file:
    reader = pdf2.PdfReader(file)
    #page = len(reader.pages)
    page = reader.pages[0]
    page.rotate(90)
    writer = pdf2.PdfWriter()
    writer.add_page(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)
    

