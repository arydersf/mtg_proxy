import os 
import re
import pandas as pd
import urllib
import requests
import time
import logging

logger = logging.getLogger(__name__)

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
    ## method called from app, recouses sub dir is in the same folder as where its called. 
    recources_path = os.path.join(git_dir, "proxy/", "recources/")

    ## I decided to only download the card.json file once. This could be upgraded to be called if a card isnt found, etc. 
    JSON_file = "orace-cards.json"

    if os.path.exists(os.path.join(recources_path, JSON_file)):
        print("alread exists")
        card_df = pd.read_json(os.path.join(recources_path, JSON_file))

    else:
        bulkData_url = "https://api.scryfall.com/bulk-data"

        download_obj_bulk_data = requests.get(bulkData_url)

        download_df = pd.read_json(download_obj_bulk_data.content)

        json_download_uri = download_df["data"][0]["download_uri"]

        download_obj_card_df = requests.get(json_download_uri)

        with open(os.path.join(recources_path, JSON_file) , "wb") as file:
            file.write(download_obj_card_df.content)

        card_df = pd.read_json(os.path.join(recources_path, JSON_file))

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


def build_cardDict(file_path):

    ##Take a decklist with format: {card quantiy} {card name}\n ... 

    #Format Cards
    card_array = []

    cards = open(file_path).readlines()
    
    for card in cards:
        single_card = card.strip('\n').split(" ", 1)## Assume a 'space' seperates qnty and card_name

        if len(single_card) == 2: 
            card_qnty = int(single_card[0])
            card_name = single_card[1]
            card_array.append([card_qnty, card_name])

    ##Create diction
    file_dir = file_path.rsplit("/", 1)[0]
    card_dict = {
        "file_path": file_path,
        "file_dir": file_dir,
        "card_info": card_array,
        "image_dir": os.path.join(file_dir, "images"),
        "latex_dir": os.path.join(file_dir, "latex") 
            }

    return(card_dict)


def download_pngFiles(target_dir, card_list):
    '''summary
    Downloads the card png files from the scryfall database
    '''

    card_pngs = []
    ##Get PNG File links and download png fies tot
    for card in card_list:
        
        r_fullData = requests.get(f"https://api.scryfall.com/cards/named?exact={card[1]}")

        if r_fullData.status_code == 200:

            card_allData = r_fullData.json()

            ##download png files to target_dir
            r_png = requests.get(card_allData["image_uris"]["png"])

            file_name = card[1].replace(" ","-").lower()+".png"
       
            with open(os.path.join(target_dir, "images", file_name), "wb") as file:
                file.write(r_png.content)

        else:
            logger.warning(f"Card cannot be found: {card[1]}. Will not be included in final pdf.")

        time.sleep(0.1) ##per Scryfall community guidlines



#build_cardDict test:
#test_path = "/Users/ARyder/Documents/Projects/mtg_proxy/proxy/recources/example/Deck - Eldrazi Tron.txt"
#xx = build_cardDict(test_path)
#print(xx)


##download_png test:
#test_dir='/Users/ARyder/Desktop/tt'
#test_cardList= [[12, 'All Is Dust'], [1, 'Blast Zone'], [1, 'Cavern of Souls']]
#download_pngFiles(test_dir, test_cardList)

