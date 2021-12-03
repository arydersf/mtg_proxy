from system_handler import system_handler
from latex import latex_parser
from data import data_loader
from Decklist import Decklist

import os
import test
import logging

##Logging configuration
logger = logging.getLogger()
logger.setLevel(level = logging.INFO)

stream = logging.StreamHandler()
streamformat = logging.Formatter("[%(asctime)s]: [%(levelname)s]: [%(module)s]: %(message)s")
stream.setFormatter(streamformat)
stream.setLevel(logging.INFO)

logger.addHandler(stream)


def run():
    #1. Get decklist filepath
    logger.info("Started Application")
    decklist_file = system_handler.choose_file()
    logger.info(f"Loaded desklist: %s", decklist_file)


    #2. Load decklist contents
    decklist = decklist.build_cardDict(decklist_file)


    # #3. Create directory structure
    # system_handler.setup_dir(decklist_dic["file_dir"])
    # logger.info(f"Made subdirecotires: %s, and %s", decklist_dic["image_dir"], decklist_dic["latex_dir"])


    # #4. Download png images from decklist_dict and place in appropriate directory (imageDirectory)
    # data_loader.download_pngFiles(decklist_dic["file_dir"], decklist_dic["card_info"])
    # logger.info(f"Downloaded all the image files to: %s", decklist_dic["file_dir"])


    # #5. Build latex document 
    # latex_file = latex_parser.make_latex_tex_file(decklist_dic["image_dir"], decklist_dic["card_info"], decklist_dic["latex_dir"])
    # logger.info(f"Created .tex file")

    # #6. Typset latex document
    # latex_parser.compile_tex(latex_file, decklist_dic["file_dir"])


    # #7. Clean up
    # system_handler.clean_up(decklist_dic["file_dir"])
    # logger.info(f"Deleted subdirecotires:")

    # logger.info("Finished Application")









    
    # #1. Get decklist filepath
    # logger.info("Started Application")
    # decklist_file = system_handler.choose_file()
    # logger.info(f"Loaded desklist: %s", decklist_file)


    # #2. Load decklist contents
    # decklist = decklist.build_cardDict(decklist_file)


    # #3. Create directory structure
    # system_handler.setup_dir(decklist_dic["file_dir"])
    # logger.info(f"Made subdirecotires: %s, and %s", decklist_dic["image_dir"], decklist_dic["latex_dir"])


    # #4. Download png images from decklist_dict and place in appropriate directory (imageDirectory)
    # data_loader.download_pngFiles(decklist_dic["file_dir"], decklist_dic["card_info"])
    # logger.info(f"Downloaded all the image files to: %s", decklist_dic["file_dir"])


    # #5. Build latex document 
    # latex_file = latex_parser.make_latex_tex_file(decklist_dic["image_dir"], decklist_dic["card_info"], decklist_dic["latex_dir"])
    # logger.info(f"Created .tex file")

    # #6. Typset latex document
    # latex_parser.compile_tex(latex_file, decklist_dic["file_dir"])


    # #7. Clean up
    # system_handler.clean_up(decklist_dic["file_dir"])
    # logger.info(f"Deleted subdirecotires:")

    # logger.info("Finished Application")


def run2():

    #1. Get decklist filepath
    logger.info("Started Application")
    decklist_file = system_handler.choose_file()
    logger.info(f"Loaded desklist: %s", decklist_file)


    #2. Load decklist contents
    decklist = Decklist(decklist_file)
    decklist.populate_attributes()


    #3. Create directory structure
    system_handler.setup_dir(decklist.file_dir)
    logger.info(f"Made subdirecotires: %s, and %s", decklist.file_dir, decklist.latex_dir)


    #4. Download png images from decklist_dict and place in appropriate directory (imageDirectory)
    data_loader.download_pngFiles(decklist.file_dir, decklist.card_info)
    logger.info(f"Downloaded all the .png files to: %s", decklist.file_dir)

    #5. Build laTEX document 
    decklist.make_latex()
    logger.info(f"Created the laTEX string")

    system_handler.make_file(decklist.latex_dir, decklist.latex_docName, decklist.latex_docString)
    logger.info(f"Made laTEX file")

    #6. Compile laTEX document
    system_handler.compile_latex(decklist.latex_file, decklist.file_dir)


    #7. Clean up
    system_handler.clean_up(decklist.file_dir)
    logger.info(f"Deleted subdirecotires:")

    logger.info("Finished Application")

run2()


