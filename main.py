import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def list_files_directories(path):
    files=os.listdir(path)
    files_full_path=[os.path.join(path,f) for f in files]
    return files_full_path

def pdf_merger(paths,output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def final_fn():
    path = r"C:\Users\shrey\Documents\Zoom"
    paths = list_files_directories(path)
    pdf_merger(paths, output=os.path.join(path,"merged.pdf"))

final_fn()

