#! /usr/nguyenkhacbaoanh/anaconda3/bin
import re
class membre:
	def __init__(self, name, income=None, outcome=None):
		self.name = name
		self.income = income
		self.outcome = outcome
	def __str__(self):
		return "{}".format(self.name)

	def __add__(self, other):
		return (self.income + other.income, self.outcome + other.outcome)

class Pay(membre):
	
	def __init__(self, name, income=None, outcome=None):
		super().__init__(name, income, outcome)

	def entry_items_prices(self):
		entries = ""
		data = {"description":[],
				"price": []}
		while True:
			d = input("entry of {}: ".format(self.name))
			if d == "":
				entries = entries.strip()
				break
			entries = entries + d + "\n"
		entries = entries.strip()
		print(entries)
		pattern = re.compile("([a-zA-Z\s]+)([0-9,.]+)", flags=re.MULTILINE)
		matches = pattern.finditer(entries)

		for match in matches:
			data["description"].append(match.group(1).strip())
			data["price"].append(float(match.group(2).strip()))
		# self.outcome += data
		# return self.outcome
		return data

if __name__ == '__main__':
	# Anh = membre("Anh", 500, 200)
	# Ngoc = membre("Ngoc", 600, 300)

	# # print( Anh + Ngoc)
	chi_tieu_anh = Pay("Anh", 500, 200).entry_items_prices()
	chi_tieu_ngoc = Pay("Ngoc", 600, 300).entry_items_prices()
	print(chi_tieu_anh["price"] + chi_tieu_ngoc["price"])