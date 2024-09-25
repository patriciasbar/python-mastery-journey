import PyPDF2 as pdf2
import sys

inputs = sys.argv[1:] #grab all files into a list

#filename = "sample_files\dummy.pdf"

def pdf_merger(pdf_list):
    merger = pdf2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')

pdf_merger(inputs)