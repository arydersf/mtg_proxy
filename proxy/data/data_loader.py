import os 
import re
import pandas as pd
import urllib
import requests
import time
import logging

logger = logging.getLogger(__name__)


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


def download_pngFiles(target_dir, card_list):
    '''Downloads card png files from the scryfall database'''

    card_pngs = []

    for card in card_list:        
        r_fullData = requests.get(f"https://api.scryfall.com/cards/named?exact={card[1]}")

        if r_fullData.status_code == 200:
            card_allData = r_fullData.json()

            r_png = requests.get(card_allData["image_uris"]["png"])

            file_name = card[1].replace(" ","-").lower()+".png"
       
            with open(os.path.join(target_dir, "images", file_name), "wb") as file:
                logger.debug("Download %s", file_name)
                file.write(r_png.content)

        else:
            logger.warning(f"Card cannot be found: {card[1]}. Will not be included in final pdf.")

        time.sleep(0.1) ##per Scryfall community guidlines
