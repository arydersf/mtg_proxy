
# Magic the Gathering Card Proxy 

Proxy is a program lets the user format a MTG card proxy from a deck list by taking .txt decklist file and makes a .tex file.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages. 

```bash
pip install -r requirements.txt
```

NOTE: a LaTEX typsetter is NOT INCLUDED here. You can either download a LaTEX editor or use online tools such as [Overleaf](https://www.overleaf.com/)

## Usage

First download a decklist from [MTGGoldfish](https://www.mtggoldfish.com/metagame/modern#paper) and put it into a directory by itself.  

Then, in terminal navigate to the proxy code directory and use the bash command, 
```bash
python -m proxy 
```

The program will then promp have you choose a directory. Make sure the only item in the directory is the decklist file (.txt).  It will then create two subdirectores:

1. ./images 
	
	* One coppy of each card will be placed in here. The file name will be name-of-card.png 

2. ./latex

	* A properly formated .tex file will be generated. It is up to the user to then typset the file.  NOTE: the .tex file will use images stored in the ./image directory. So if you move it, also move the ./images directory.  



## License
[MIT](https://choosealicense.com/licenses/mit/)
