from .system_handler import system_handler
from .data import data_loader
from .latex_parser import latex_parser
import os
 

def run():
    print("Setting up directory ...  \n")
    root_dir, image_dir, latex_dir = system_handler.setup_dir()
    #root_dir, image_dir, latex_dir = setup_dir()


    print("Loading files ... \n")
    deck_list = data_loader.load_decklist(root_dir)
    card_df = data_loader.load_card_data(os.getcwd())
    data_loader.populate_image_dir(deck_list, card_df, image_dir)



    print("Formatting LaTeX document...\n")
    latex_parser.make_latex_tex_file(image_dir, deck_list, latex_dir)


    #system_handler.system_handler.typset_tex_file("cards_for_print.tex", latex_dir)
    print("YAY! The latex document is made")