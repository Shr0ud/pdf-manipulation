#imports 
import PyPDF2
import sys

# merges pdfs
try:
    pdfs = sys.argv[1:] # gets pdf file name argument

    merger = PyPDF2.PdfFileMerger() # creates merger

    # merges all the files
    for pdf in pdfs:
        merger.append(pdf)

    with open('merged.pdf', 'wb') as outFile:
        merger.write('merged.pdf')

except FileNotFoundError:
    print("The file was not found")