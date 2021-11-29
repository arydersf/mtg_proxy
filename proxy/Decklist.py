import os

class Decklist:
	"""Where all the proxy information is stroed."""

	def __init__(self, decklist_path): #, latex_path, images_path, latex_string):
		self.decklist_path = decklist_path


	def populate_attributes(self):
		"""Builds out Decklist attributes used in other methods"""

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




	def parse_decklist():
		pass

	def build_latex_string():
		pass





# test_path = "/Users/ARyder/Documents/Projects/mtg_proxy/proxy/recources/example/Deck - Eldrazi Tron.txt"
# tt = Decklist(test_path)
# tt.populate_attributes()
# print(tt.card_info)