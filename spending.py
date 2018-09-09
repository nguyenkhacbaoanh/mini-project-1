#! /usr/nguyenkhacbaoanh/anaconda3/bin
import re
import sqlite3
class Pay:
	def __init__(self, name, data=None):
		self.name = name
		self.data = data


	def entry_items_prices(self, entries):
		# entries = ""
		data_local = {"description":[],
				"price": []}
		# while True:
		# 	d = input("entry of {}: ".format(self.name))
		# 	if d == "":
		# 		entries = entries.strip()
		# 		break
		# 	entries = entries + d + "\n"
		entries = entries.strip()
		pattern = re.compile(r"([a-zA-Z\s]+)([0-9,.]+)", flags=re.MULTILINE)
		matches = pattern.finditer(entries)

		for match in matches:
			data_local["description"].append(match.group(1).strip())
			data_local["price"].append(float(match.group(2).strip()))
		# self.outcome += data
		# return self.outcome
		if self.data == None:
			self.data = data_local
		self.insert_depending_detail
		return self.data
	# @property
	# def display_data_by_table(self):
	# 	for k,v in self.data.items:
	# 	print("================")
	# 	print("={}=")
	@property
	def connection_database(self):
		conn = sqlite3.connect("database.db") #database.db
		c = conn.cursor()
		try:
			c.execute("""CREATE TABLE membre (
										name text,
										descr text,
										price integer
										)

			""")
		except sqlite3.OperationalError:
			pass
		return conn, c

	@property
	def insert_depending_detail(self, duplicate=True):
		if duplicate:
			conn, c = self.connection_database
			with conn:
				for i in range(len(self.data)+1):
					c.execute("INSERT INTO membre VALUES (:name,:descr,:price)",{'name':self.name, 'descr':self.data['description'][i], 'price':self.data['price'][i]})
			conn.commit()
			conn.close()
		return
	def get_dependings_by_name(self):
		conn, c = self.connection_database
		c.execute("SELECT * FROM membre WHERE name=:name", {'name':self.name})
		return c.fetchall()

	def get_sum_by_name(self):
		conn, c = self.connection_database
		c.execute("SELECT name, SUM(price) FROM membre WHERE name=:name GROUP BY name", {'name':self.name})
		return c.fetchall()

class Membre(Pay):
	income = 0
	outcome = {}
	def __init__(self, name, data=None):
		super().__init__(name, data)

	def __str__(self):
		return "{} is here".format(self.name)


	@classmethod
	def income_per_month(cls, amount):
		cls.income = amount

	def outcome_per_month(self, strings):
		Membre.outcome = sum(super().entry_items_prices(strings)['price'])
		return Membre.outcome
	# @classmethod
	# def outcome_per_month(cls, strings):
	# 	cls.outcome = super(Membre, cls).entry_items_prices(cls, strings)
	# 	return cls.outcome

if __name__ == '__main__':
	entries1 = "buy vegetable 30\nbuy water 20\neating outdoor 15"
	entries2 = "withdraw 45\nbreakfast 10\ncoffee 5"
	anh = Membre("Anh")
	anh.income_per_month(700)
	print(anh.income)
	anh.outcome_per_month(entries1)
	print(anh.outcome)

	ngoc = Membre("Ngoc")
	ngoc.income_per_month(900)
	print(ngoc.income)
	ngoc.outcome_per_month(entries2)
	print(ngoc.outcome)

	


