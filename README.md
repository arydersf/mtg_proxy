
# Magic the Gathering Card Proxy 

Proxy is a program lets the user format a MTG card proxy from a deck list by taking .txt decklist file and makes a .tex file.  All proxy images come from [Scyfall](https://scryfall.com/).


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages. 

```bash
pip install -r requirements.txt
```


## Usage

First download a decklist from [MTGGoldfish](https://www.mtggoldfish.com/metagame/modern#paper).  

Then, in terminal navigate to the proxy code directory and use the bash command, 
```bash
python -m proxy 
```

The program will then prompt you to choose a Decklist file.  The program will then,
1. Query Scryfall and download .png image files of the cards in your list
2. Create a formatted LaTEX document
3. Typset the LaTEX document and place the resulting PDF file in the same directory as the Decklist file
4. Clean up all auxiliary files


## License
[MIT](https://choosealicense.com/licenses/mit/)

## Future
One possible extension of this project would be to integrate the code with MTGGoldfish to remove the need to download the decklist. This could be accomplished using some form of Chrome extension. 

Another avenue to explore would be render the PDF with something other than LaTEX.  


