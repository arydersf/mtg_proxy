import re
import os 
import logging

logger = logging.getLogger(__name__)


class Decklist:
	"""Where all the proxy information is stroed."""

	def __init__(self, decklist_path):
		self.decklist_path = decklist_path
		self.file_dir = ""
		self.card_info = ""
		self.image_dir = ""
		self.latex_dir = ""
		self.latex_file = ""
		self.latex_docName = "cards_for_print.tex"
		self.latex_docString = ""


	def populate_attributes(self):
		"""Method out Decklist attributes used in other methods"""

		card_array = []
		cards = []

		with open(self.decklist_path) as f:
			cards = f.readlines()

		for card in cards:
			single_card = card.strip('\n').split(" ", 1) ## Assume the first 'space' seperates {quantity} and {card name}

			if len(single_card) == 2: 
				card_qnty = int(single_card[0])
				card_name = single_card[1]
				card_array.append([card_qnty, card_name])

		##Store attributes
		file_dir = self.decklist_path.rsplit("/", 1)[0]
		self.file_dir = file_dir
		self.card_info = card_array
		self.image_dir = os.path.join(file_dir, "images")
		self.latex_dir = os.path.join(file_dir, "latex") 
		self.latex_file = os.path.join(self.latex_dir, self.latex_docName)


	def get_image_paths_for_latex(self, images_dir, deck_list):
		'''Method that returns an array with all the .png file paths that exist in deck_list and can be found in image_dir'''

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
				logging.warn(f"Unable to find {card[1]}")

		return cards_paths_latex


	def make_latex_card_table(self, cards_paths_latex):
		'''Method to format the 'tabular' for latex'''
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

		#convert array to single string
		table =""
		for line in table_text:
			table += line + "\n"

		return table


	def make_latex(self):
		'''Creates the latex document as a string and stores it as self.latex_docString'''

		cards_paths = self.get_image_paths_for_latex(self.image_dir, self.card_info)

		card_table = self.make_latex_card_table(cards_paths)

		preamble = '''
			\\documentclass{article}
			\\usepackage{graphicx}
			\\usepackage[ paperwidth=210mm, paperheight=297mm, margin=10mm]{geometry}
			\\usepackage[table]{xcolor}

			\\begin{document}

			\\setlength{\\tabcolsep}{0.5pt}   
			\\addtolength{\\tabcolsep}{0.5pt} 
			\\def\\arraystretch{0.5} 

			'''

		graphics = f"\\graphicspath{{{{{self.image_dir}/}}}}\n"

		ending = "\\end{document}"


		self.latex_docString = preamble + graphics + card_table + ending

