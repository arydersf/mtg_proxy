
# Magic the Gathering Card Proxy 

Proxy is a program lets the user format a MTG card proxy from a deck list by taking .txt decklist file and makes a .tex file.  All proxy images come from [Scyfall](https://scryfall.com/).


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages. 

```bash
pip install -r requirements.txt
```


## Usage

First download a decklist from [MTGGoldfish](https://www.mtggoldfish.com/metagame/modern#paper) and put it into a directory by itself.  

Then, in terminal navigate to the proxy code directory and use the bash command, 
```bash
python -m proxy 
```

The program will then promp have you choose a Decklist file.  It will then create a PDF of the decklist cards. 

TODO: Fill in steps for this process. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
