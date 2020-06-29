import os
import shutil
import tkinter as tk
from tkinter import filedialog



def choose_dir():
	root = tk.Tk()
	root.withdraw()

	file_path = filedialog.askdirectory()

	return(file_path)


def make_folder(root_dir, dir_name):
    folder_dir = os.path.join(root_dir, dir_name)

    if os.path.exists(folder_dir):
    	shutil.rmtree(folder_dir)

    os.makedirs(folder_dir)


def setup_dir():
    root_dir = choose_dir()

    pdf_folder  = "./latex"
    image_folder    = "./images"

    make_folder(root_dir, pdf_folder)
    make_folder(root_dir, image_folder)

    return root_dir, root_dir + image_folder[1:],  root_dir + pdf_folder[1:] 


def typset_tex_file(latex_file, latex_dir):
	os.chdir(latex_dir)
	os.system(f"pdflatex {latex_file}")

