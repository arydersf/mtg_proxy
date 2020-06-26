import os 
import re
import pandas as pd

def read_deckList():
    card_list = []
    
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    if len(txt_files) != 1:
        raise ValueError('should be only one txt file in the current directory')
    
    cards = open(txt_files[0]).readlines()
    
    for card in cards:
        name = card[2:-1]
        if name != "":
            qnty = int(card[0])
            card_list.append([qnty, name])
    
    return(card_list)


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


def load_card_data():
	JSON_path = "orace-cards.json"
	card_df = pd.read_json(JSON_path)

	return card_df