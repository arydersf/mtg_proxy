import os
import shutil
import tkinter as tk
from tkinter import filedialog
import logging


logger = logging.getLogger()

def choose_dir():
    """Opens a file chooser and returns selected directory"""
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory()
    logger.debug("Choosen filepath: %s", file_path)

    return(file_path)


def choose_file():
    """Opens a file chooser and returns selected filepath"""

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    logger.debug("Choosen filepath: %s", file_path)

    return(file_path)


def make_dir(root_dir, dir_name):
    """Creates a blank directory at root_dir"""

    folder_dir = os.path.join(root_dir, dir_name)

    if os.path.exists(folder_dir):
        logger.debug("Directory [%s] existed. Deleted previous directory and created new one", folder_dir)
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


def make_file(directory, filename, file_contents):

    with open(os.path.join(directory, filename), "w") as f:
        f.write(file_contents)


def compile_latex(latex_file, target_dir):
    '''Compiles a latex_file document and places resulting .pdf file into the target directory'''

    file_dir = latex_file.rsplit("/", 1)[0]

    file_name = latex_file.rsplit("/", 1)[1][:-4]

    #compile
    if os.path.exists(latex_file):
        os.system(f"pdflatex -interaction=nonstop -output-directory={file_dir} {latex_file}")

    #move
    pdf_file = f"{file_dir}/{file_name}.pdf"
    if os.path.exists(pdf_file):
        os.system(f"mv {pdf_file} {target_dir}/{file_name}.pdf")


def clean_up(file_dir):
    """Delets al directories and files created by program that are not the final pdf"""

    image_dir = os.path.join(file_dir, "images")
    if os.path.exists(image_dir):
        shutil.rmtree(image_dir)

    latex_dir = os.path.join(file_dir, "latex")
    if os.path.exists(latex_dir):
        #shutil.rmtree(latex_dir)
        pass

