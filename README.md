
# Magic the Gathering Card Proxy 

Proxy is a program lets the user format a MTG card proxy from a deck list by taking .txt decklist file and makes a .tex file.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```


## License
[MIT](https://choosealicense.com/licenses/mit/)





##Specific Program Requirements:

1. Folder with only a decklis.txt file of the format:
		>quantity of card \*space* name of card \*n/*
		<br/> i.e 
		<br/> 5 Forest 
		<br/> 4 Cling to dust
		<br/> ... 

	* Deck list of this format can be found at: http ://wwwmtggoldfish.com/metagame/modern#paper
2. Some way of typsetting a .tex file


