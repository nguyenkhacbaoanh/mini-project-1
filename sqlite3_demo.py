import sqlite3
# help(sqlite3)

conn = sqlite3.connect('database.db')

c = conn.cursor()

# c.execute("""CREATE TABLE membre (
# 								name text,
# 								income integer,
# 								outcome integer
# 								)

# 	""")

# c.execute("INSERT INTO membre VALUES ('Bao Anh', 300, 200)")
# c.execute("INSERT INTO membre VALUES ('Trinh Ngoc', 500, 100)")
# c.execute("INSERT INTO membre VALUES ('Jerome', 0, 100)")
# c.execute("UPDATE membre SET outcome=200 WHERE name=='Jerome'")
c.execute("SELECT * FROM membre")
print(c.fetchall())
c.execute("SELECT name, SUM(price) FROM membre GROUP BY name")


print(c.fetchall())


