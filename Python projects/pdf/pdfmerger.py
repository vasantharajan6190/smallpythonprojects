import PyPDF2
import sys

inputs  = sys.argv[1:]

def filemerger(pdflist):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdflist:
		merger.append(pdf)
	merger.write("super.pdf")
filemerger(inputs)