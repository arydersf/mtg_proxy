import os
import re 
import urllib
import requests
import pandas as pd
import tkinter as tk
from tkinter import filedialog

import system_handler.system_handler
import data.data_loader
 


def choose_dir():
	root = tk.Tk()
	root.withdraw()

	file_path = filedialog.askdirectory()

	return(file_path)

def make_folder(root_dir, dir_name):
    folder_dir = os.path.join(root_dir, dir_name)

    if os.path.exists(folder_dir):
        #need to make this more robust
        os.rmdir(folder_dir)

    os.makedirs(folder_dir)

def load_decklist(root_dir):
    card_list = []
    
    txt_files = [f for f in os.listdir(root_dir) if f.endswith('.txt')]
    if len(txt_files) != 1:
        raise ValueError('should be only one txt file in the current directory')
    
    cards = open(os.path.join(root_dir, txt_files[0])).readlines()
    
    for card in cards:
        name = card[2:-1]
        if name != "":
            qnty = int(card[0])
            card_list.append([qnty, name])
    
    return(card_list)
 
def load_card_JSON(path):
	card_df = pd.read_json(path)
	return card_df

def pull_image(deck_list, card_df, save_path):
    
    for card in enumerate(deck_list):
        #print(card[1][1])
        specific_card = card_df[card_df["name"] == card[1][1]]["image_uris"]
        
        if specific_card.tolist():
            for obj in specific_card:
                test_str = str(obj)

            matched_url = re.search("'png': '(.+?)', 'art_crop':", test_str)

            if matched_url:
                found_url = matched_url.group(1)
                 
                
            downloaded_obj = requests.get(found_url)
            
            #LaTex doesn't like space in names, so changing file names to dashes
            file_name = card[1][1].replace(" ","-").lower()+".png"

            with open(os.path.join(save_path, file_name), "wb") as file:
                file.write(downloaded_obj.content)


        else:
            print(f"Cannot find {card[1][1]}")

def get_paths(images_dir, deck_list):
    cards_paths_latex = []
    image_paths = os.listdir(images_dir)

    for card in deck_list:
        path = card[1].replace(" ","-").lower()
        r = re.compile(f".*{path}.*")
        path = list(filter(r.match, image_paths)) 

        if path:
            for i in range(card[0]):
                cards_paths_latex.append(path)
        else:
            print(f"Unable to find {card[1]}")
            
    return cards_paths_latex

def make_card_table(cards_paths_latex):
    table_text = []
    begin_table = "\\begin{tabular}{ccc}"
    end_table = "\\end{tabular}"

    for i, path in enumerate(cards_paths_latex):
        if i == 0:
            table_text.append(begin_table)
            text = f"\\includegraphics[width=2.5in, height = 3.5in]{{{path[0]}}}&"
            table_text.append(text)

        elif i == len(cards_paths_latex)-1:
            text = f"\\includegraphics[width=2.5in, height = 3.5in]{{{path[0]}}}"
            table_text.append(text)
            table_text.append(end_table)

        elif (i+1) % 9 == 0:
            text = f"\\includegraphics[width=2.5in, height = 3.5in]{{{path[0]}}}"
            table_text.append(text)
            table_text.append(end_table)
            table_text.append("")
            table_text.append("\\newpage")
            table_text.append("")
            table_text.append(begin_table)   

        elif (i+1) % 3 == 0:
            text = f"\\includegraphics[width=2.5in, height = 3.5in]{{{path[0]}}} \\\\"
            table_text.append(text)
            table_text.append("")


        else:
            text = f"\\includegraphics[width=2.5in, height = 3.5in]{{{path[0]}}}&"
            table_text.append(text)
    
    return table_text

def make_pdf(image_folder, deck_list, pdf_folder):
    
    file_name = "cards_for_print.tex"
    
    cards_paths = get_paths(image_folder, deck_list)
    
    card_table = make_card_table(cards_paths)
    
    preamble = '''
    \\documentclass{article}
    \\usepackage{graphicx}
    \\usepackage[ paperwidth=210mm, paperheight=297mm, margin=10mm]{geometry}
    \\usepackage[table]{xcolor}

    \\begin{document}

    \\setlength{\\tabcolsep}{0.5pt}   
    \\addtolength{\\tabcolsep}{0.5pt} 
    \\def\\arraystretch{0.5} 

    \\graphicspath{{../images/}}


        '''

    ending = "\\end{document}"
    


    if os.path.exists(os.path.join(pdf_folder, file_name)):
      os.remove(os.path.join(pdf_folder, file_name))

    f = open(os.path.join(pdf_folder, file_name), "x")
    f.write(preamble)

    for listitem in card_table:
        f.write('%s\n' % listitem)

    f.write(ending)
    f.close()

def pipeline():
	root_dir 	= choose_dir() 
	pdf_folder 	= "./pdf"
	image_folder	= "./images"

	make_folder(root_dir, pdf_folder)
	make_folder(root_dir, image_folder)

	print("Made folders")

	deck_list = load_decklist(root_dir)

	print("Loading JSON card data ... ")

	JSON_path = "/Users/ARyder/Documents/Project/MTG_coding/dataFile/orace-cards.json"

	card_df = load_card_JSON(JSON_path)

	
	# card_df = pd.read_json(JSON_path)

	print("All Files Uploaded")

	print("making LaTeX document...")

	pull_image(deck_list, card_df, image_folder)

	make_pdf(image_folder, deck_list,pdf_folder)

	print("YAY! The latex document is made")


def pipeline2():
    root_dir, image_dir, latex_dir = system_handler.system_handler.setup_dir()
    print("Directy is ready")


    deck_list = data.data_loader.load_decklist(root_dir)

    print("Loading JSON card data ... ")

    card_df = data.data_loader.load_card_data()

    print("All Files Uploaded")

    

    print("making LaTeX document...")

    pull_image(deck_list, card_df, image_dir)

    make_pdf(image_dir, deck_list, latex_dir)

    system_handler.system_handler.typset_tex_file("cards_for_print.tex", latex_dir)

    print("YAY! The latex document is made")

#pipeline("/Users/ARyder/Documents/MTG/Modern/2020/2020_06_12/Tron")

pipeline2()
