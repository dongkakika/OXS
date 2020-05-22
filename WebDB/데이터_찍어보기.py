import sqlite3

con = sqlite3.connect("C:\\Users\\Jim\\Desktop\\Git\\OXS\\WebDB\\oxsData.db")

cur = con.cursor()

# 따로 찍어보기
cur.execute("SELECT * FROM Crawlingdata")
for row in cur:
    print(row)

# 한 번에 찍어보기
cur.execute("select * from Crawlingdata")
rows = cur.fetchall()

print(rows)
