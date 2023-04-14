import sys
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

N_argumentos = len(sys.argv)

def replace_text(input_path, output_path, find_text, replace_text):
    with open(input_path, 'rb') as infile:
        pdf_reader = PdfFileReader(infile)
        pdf_writer = PdfFileWriter()

        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            new_text = text.replace(find_text, replace_text)
            page.mergeTextFields()
            page.mergeTextString(new_text)
            pdf_writer.addPage(page)

        with open(output_path, 'wb') as outfile:
            pdf_writer.write(outfile)

def main():
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    find_text = sys.argv[0]
    replace_text = sys.argv[1]
    replace_text(input_path, output_path, find_text, replace_text)

if N_argumentos <= 0:
    print("Error nenhum argumento foi encontrado!!!")
elif N_argumentos < 4:
    print("Error argumentos faltando!!!")
elif N_argumentos == 4:
    main()