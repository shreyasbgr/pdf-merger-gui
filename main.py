import os
import tkinter as tk
import logger_util
from PyPDF2 import PdfFileReader, PdfFileWriter
master = tk.Tk()
directory_var = tk.StringVar()
directory_input = tk.Entry(master,textvariable = directory_var).grid(row=0,column=1)

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
    logger_utility = logger_util.custom_logger()
    logger_utility.logger.info("Hi there!")

    path=directory_var.get()
    paths = get_files_directories(path)
    pdf_paths = [p for p in paths if p.endswith('.pdf')]
    files = [os.path.basename(p) for p in paths]
    pdf_files = [os.path.basename(p) for p in pdf_paths]

    # print("All the files and folders in the current directory are: \n")
    Lb1=tk.Listbox(master)
    i=0
    for f in files:
        Lb1.insert(i,f)
        i+=1
    Lb1.grid(row=1,column=0)

    #print("All the pdf files in the current directory are: \n")
    Lb2=tk.Listbox(master)
    for f in pdf_files:
        Lb2.insert(i,f)
        i+=1
    Lb2.grid(row=1,column=1)

    pdf_merger(pdf_paths, output=os.path.join(path,"merged.pdf"))

def final_fn_gui():
    master.title("PDF Merger App")
    tk.Label(master, text='Enter the path of the directory:').grid(row=0)
    button = tk.Button(master,text='Merge PDFs',width=25,command=final_fn).grid(row=0,column=2)
    master.mainloop()
final_fn_gui()

