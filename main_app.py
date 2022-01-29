import os
import tkinter as tk
import file_listing
class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.master = master
        master.title("PDF Merger App")

        self.label_directory_input=tk.Label(master, text='Enter the path of the directory:')
        self.label_directory_input.grid(row=0,column=0)

        self.var_directory_input = tk.StringVar()
        self.directory_input = tk.Entry(master,textvariable = self.var_directory_input)
        self.directory_input.grid(row=0,column=1)

        self.merge_pdf_button = tk.Button(master,text='Show Files',width=25,command=self.update_files)
        self.merge_pdf_button.grid(row=1,column=0)

        self.merge_pdf_button = tk.Button(master,text='Merge PDFs',width=25,command=self.merge_pdfs)
        self.merge_pdf_button.grid(row=1,column=1)
        
        self.label_list_box_all = tk.Label(master, text='All files in the given path')
        self.label_list_box_all.grid(row=2,column=0)
        self.list_box_all=tk.Listbox(master)
        self.list_box_all.grid(row=3,column=0)
        self.label_list_box_pdf = tk.Label(master, text='All pdf files in the given path')
        self.label_list_box_pdf.grid(row=2,column=1)
        self.list_box_pdf=tk.Listbox(master)
        self.list_box_pdf.grid(row=3,column=1)

    def clear_files(self):
        self.list_box_all.delete(0,tk.END)
        self.list_box_pdf.delete(0,tk.END)

    def update_files(self):
        self.clear_files()
        path=self.var_directory_input.get()
        all_files = file_listing.get_files(path)
        pdf_files = file_listing.get_pdf_files(path)
        # Update list_box_all
        i=0
        for f in all_files:
            self.list_box_all.insert(i,f)
            i+=1
        
        # Update list_box_pdf
        i=0
        for f in pdf_files:
            self.list_box_pdf.insert(i,f)
            i+=1

    def merge_pdfs(self):
        path=self.var_directory_input.get()
        pdf_paths = file_listing.get_pdf_files_path(path)
        file_listing.pdf_merger(pdf_paths, output=os.path.join(path,"merged.pdf"))

if __name__ == "__main__":
    window = tk.Tk()
    MainApplication(window)
    window.mainloop()