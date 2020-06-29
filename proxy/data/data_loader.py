import os 
import re
import pandas as pd
import urllib
import requests

def load_decklist(proxy_folder):
    card_list = []
    
    txt_files = [f for f in os.listdir(proxy_folder) if f.endswith('.txt')]
    
    if len(txt_files) != 1:
        raise ValueError('should be only one txt file in the current directory')
    
    cards = open(os.path.join(proxy_folder, txt_files[0])).readlines()
    
    for card in cards:
        name = card[2:-1]
        if name != "":
            qnty = int(card[0])
            card_list.append([qnty, name])
    
    return(card_list)


def get_image_paths(images_dir, deck_list):
    ## The .tex file needs the path of all the images it will use  
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


def load_card_data(git_dir):
    #data_path = os.path.join(os.getcwd(),
    ## method called from app, recouses sub dir is in the same folder as where its called. 
    recources_path = os.path.join(git_dir, "proxy/", "recources/")

    ## If no card file, download from interent: FIX!! ###
    JSON_file = "orace-cards.json"

    path_ = os.path.join(recources_path, JSON_file)

    card_df = pd.read_json(path_)

    return card_df


def populate_image_dir(deck_list, card_df, save_path):

    for card in deck_list:
        target_card = card_df[card_df["name"] == card[1]]

        target_png_url = target_card['image_uris'].values[0]['png']

        if target_png_url:
            downloaded_obj = requests.get(target_png_url)

            #LaTex doesn't like space in names, so changing file names to dashes
            file_name = card[1].replace(" ","-").lower()+".png"

            with open(os.path.join(save_path, file_name), "wb") as file:
                file.write(downloaded_obj.content)

        else:
            print(f"Cannot find {card[1][1]}") 

