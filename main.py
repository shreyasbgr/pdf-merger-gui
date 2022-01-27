import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def get_files_directories(path):
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
    path=input("Enter the path where at which all the pdf's need to be merged: ")
    paths = get_files_directories(path)
    pdf_paths = [p for p in paths if p.endswith('.pdf')]
    files = [os.path.basename(p) for p in paths]
    pdf_files = [os.path.basename(p) for p in pdf_paths]

    print("All the files and folders in the current directory are: \n")
    for f in files:
        print(f)
    print()

    print("All the pdf files in the current directory are: \n")
    for f in pdf_files:
        print(f)
    print()

    pdf_merger(pdf_paths, output=os.path.join(path,"merged.pdf"))

final_fn()

