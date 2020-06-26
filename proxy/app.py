# import os
# import re 
# import urllib
# import requests
# import pandas as pd
# import tkinter as tk
# from tkinter import filedialog

import system_handler.system_handler
import data.data_loader
import latex_parser.latex_parser
 


def pipeline2():
    print("Setting up directory ...  \n")
    root_dir, image_dir, latex_dir = system_handler.system_handler.setup_dir()


    print("Loading files ... \n")
    deck_list = data.data_loader.load_decklist(root_dir)
    card_df = data.data_loader.load_card_data()
    data.data_loader.populate_image_dir(deck_list, card_df,image_dir)



    print("Formatting LaTeX document...\n")
    latex_parser.latex_parser.make_latex_tex_file(image_dir, deck_list, latex_dir)


    #system_handler.system_handler.typset_tex_file("cards_for_print.tex", latex_dir)
    print("YAY! The latex document is made")


pipeline2()
