#imports 
import PyPDF2

try:
    # Adds a watermark to pdfs
    # This is the 1 line way of opening files
    fileToWatermark = PyPDF2.PdfFileReader(open('test.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

    outFile =  PyPDF2.PdfFileWriter()

    for x in range(fileToWatermark.getNumPages()):

        page = fileToWatermark.getPage(x)

        # mergepage combines 2 pages's content into 1
        page.mergePage(watermark.getPage(0))  # watermark only has 1 page

        outFile.addPage(page)
    
    with open('outFile', 'rb') as output:
        outFile.write(output)

except FileNotFoundError:
    print("The file was not found")