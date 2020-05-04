import sqlite3

# reading the data and then return as a list.
f = open("data.txt", "r")

list = []
while True:
	line = f.readline()
	if not line: break
	list.append(line.split())

f.close()

print("saved datas : ", list)

con = sqlite3.connect("oxsData.db")

cur = con.cursor()
# below CREATE command is only used once when the table should be created
cur.execute("CREATE TABLE Crawlingdata(Name text, Period text);")

idx = 0
while idx < len(list):
	cur.execute("INSERT INTO Crawlingdata VALUES(?, ?);", list[idx])
	idx += 1

idx = 0

con.close()
