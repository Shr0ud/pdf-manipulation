#imports 
import PyPDF2

try:
    with open('Michael_Chen_Transcript.pdf', 'rb') as inFile: #rb is read binary
        # creates a reader
        reader = PyPDF2.PdfFileReader(inFile)

        page = reader.getPage(0) # Only the first page needed to be rotated

        page.rotateCounterClockwise(180) # page was upside down so rotated 180 degs

        with open('Rotated.pdf', 'wb') as outFile: # wb = write binary

            # create writer
            # adds the rotated page
            # then write to the outfile
            writer = PyPDF2.PdfFileWriter()
            writer.addPage(page)   
            writer.write(outFile)

except FileNotFoundError:
    print("The file was not found")