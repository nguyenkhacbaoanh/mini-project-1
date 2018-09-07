import re
s = "Di cho supermarche 40,35\nDi an ngoai va di cho 60\nMua nuoc 0,60\n"
# Dot: match any character exclude new line, except that it have flags DOTALL
print(s)
pattern = "o."
m = re.search(pattern, s)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# Caret: "^": this match the start of string
pattern = "^.i"
m = re.search(pattern, s)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# Dola: "$": match the end of string or just before the newline at the end of string
pattern = "6.$"
m = re.search(pattern, s)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# Stat: "*": match 0 or more repetitions of the preceding RE as many repetitions as are possible
pattern = "ho*"
m = re.search(pattern, s)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# Plus: "+": like * but match 1 or more repetition
pattern = "ia+"
m = re.search(pattern, s)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

pattern = "an ng+"
m = re.search(pattern, s)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# intergator: "?": match 0 or 1 repetitions of the preceding RE as many repetitions as are possible
pattern = "ho?"
m = re.search(pattern, s)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# ".*": match all string, . for any character, * for zero or more repetitions as possible
pattern = " .* "
m = re.search(pattern, s)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# ".*?": match string, . for any character, * for zero or few character repetitions as possible
pattern = " .*? "
m = re.search(pattern, s)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# {m}: match character with m repetitions
# {m,n}: match character from m to n repetitions
# {m,n}?: match character with few repetitions possible, m repetitions

# "\": back flash, either match a escape special character or signal a escape sequence
pattern = "40*\,"
m = re.search(pattern, s)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

s1 = "bao anh-hhh "
pattern = "anh\-"
m = re.search(pattern, s1)
try:
	print(m.group(0))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# brace "[]": a set of characters
pattern = "r[a-z]."
m = re.search(pattern, s)
try:
	print(m.group())
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")
pattern = "r[a-z]+"
m = re.search(pattern, s)
try:
	print(m.group())
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")
pattern = "(r[a-z]*)"
m = re.search(pattern, s)
try:
	print(m.group())
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# [^5] with be match any character except 5, if "^" is the first character of a set

# match the digit number
pattern = "(?P<num>[1-9][0-9])"
m = re.findall(pattern, s)
try:
	print(m.group(num))
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

# | is or: "A|B" is match either A or B

# (?...): a ? following by a ( is not meaningful)

pattern = "(?:[1-9][0-9])"
m = re.findall(pattern, s)
try:
	print(m.group())
except AttributeError:
	print("dont match")
print(m)
print("---------------------------------------------")

pattern = "(?P<num>(\d+).*?(\d+))"
for m in re.finditer(pattern, s):
	try:
		print(m.group("num"))
	except AttributeError:
		print("dont match")
	print(m)
print("---------------------------------------------")

string = """di cho het 30
mua nuoc 15,6
mua do an sang 0,33
"""

pattern = re.compile("([a-zA-Z\s]+)([0-9,.]+)", flags=re.MULTILINE)
matches = pattern.finditer(string)

for match in matches:
	print(match.group(2))
print("---------------------------------------------")