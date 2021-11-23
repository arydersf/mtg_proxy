import os
import shutil
import tkinter as tk
from tkinter import filedialog
import logging


logger = logging.getLogger()

def choose_dir():
	root = tk.Tk()
	root.withdraw()

	file_path = filedialog.askdirectory()

	return(file_path)


def choose_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    return(file_path)


def make_dir(root_dir, dir_name):
    folder_dir = os.path.join(root_dir, dir_name)

    if os.path.exists(folder_dir):
    	shutil.rmtree(folder_dir)

    os.makedirs(folder_dir)


def setup_dir(file_dir):
    '''summary
    Takes a file directory and makes two subdirectories at that location: 
        -latex : where the latex document will created
        -images : where the card image files will be stored
    '''

    pdf_folder  = "./latex"
    image_folder    = "./images"

    make_dir(file_dir, pdf_folder)
    make_dir(file_dir, image_folder)


def typset_tex_file(latex_file, latex_dir):
	os.chdir(latex_dir)
	os.system(f"pdflatex {latex_file}")


def clean_up(file_dir):
    """Delets al directories and files created by program that are not the final pdf"""

    image_dir = os.path.join(file_dir, "images")
    if os.path.exists(image_dir):
        shutil.rmtree(image_dir)

    latex_dir = os.path.join(file_dir, "latex")
    if os.path.exists(latex_dir):
        #shutil.rmtree(latex_dir)
        pass


def test():
    #print("Statement from system handeler")
    #logger.warning("System handler --  logger")
    logging.warning("System handler -- logging")



graphics = f"\\graphicspath{{{{{image_folder[:-1]}}}}}"


image_folder="xx"
print(f"\\graphicspath{{{image_folder}}}")