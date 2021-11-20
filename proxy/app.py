from .system_handler import system_handler
from .data import data_loader
from .latex import latex_parser
import os

def run():
    
    #1. Find desired decklist
    decklist_file = system_handler.choose_file()


    #Parse file --> decklist_df: [[decklist directory],[[qnty, cardName_1],[qnty, cardName_2], ...]] 
    decklist_dic = data_loader.build_cardDict(decklist_file)


    #Create sub directories
    system_handler.setup_dir(decklist_dic["file_dir"])


    #Download png images from decklist_dict and place in appropriate directory (imageDirectory)
    data_loader.download_pngFiles(decklist_dic["file_dir"], decklist_dic["card_info"])


    #3. Build df for latex document. {quantity, png file path}
    latex_parser.make_latex_tex_file(decklist_dic["image_dir"], decklist_dic["card_info"], decklist_dic["latex_dir"])

    #5. Run latex document
    #latex.make_png(decklist_df)



    #system_handler.system_handler.typset_tex_file("cards_for_print.tex", latex_dir)
    print("YAY! The latex document is made")

