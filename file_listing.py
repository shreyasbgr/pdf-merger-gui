import os
from logger_util import custom_logger
from PyPDF2 import PdfFileReader, PdfFileWriter

logger = custom_logger().get_logger()

def get_files_path(path):
    files=os.listdir(path)
    files_full_path=[os.path.join(path,f) for f in files]
    return files_full_path

def get_pdf_files_path(path):
    files=os.listdir(path)
    pdf_files_path=[os.path.join(path,f) for f in files if f.endswith('.pdf')]
    return pdf_files_path
    

def get_files(path):
    files=os.listdir(path)
    return files

def get_pdf_files(path):
    files=os.listdir(path)
    pdf_files = [f for f in files if f.endswith('.pdf')]
    return pdf_files

def pdf_merger(paths,output):
    if paths is None or len(paths)==0:
        logger.info("No pdf files are present.")
        return

    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

    logger.info(f"pdf files merged successfully at {output}")
