import sqlite3
import codecs # for using '한글'

f = codecs.open("data.txt", "r", "utf-8")
# open the file with 'utf-8'.
# reading the data and then return as a list.

list = []
while True:
	line = f.readline()             # 한 줄씩 읽
	if not line: break              # break the loop when it's End Of File
	list.append(line.split())       # split the line and append it to list

f.close()

# Point : 텍스트를 한 줄씩 읽는다. split으로 공백을 단위로 문자열을 나눈다.
#         나뉜 문자열 모두를 하나의 리스트로 묶어 return한다.
#         따라서 해당 반환 리스트를 목표 'list'에 append한다 -> 리스트의 리스트.


################################################################################
# Next  : 즉, 처음 텍스트를 받을 때, 긴 한 문장으로 받는다.
#         이를 중심으로 어떻게 처리할지 관련 함수가 필요하다.
#         1. 함수는 '공백' 단위로 처리하므로 이를 이용.
#         2. 함수는 공백 단위로 나뉘어진 리스트 요소를 이용해 필요 데이터 추출.
################################################################################


# below 'print' is for checking the data structure. U don't need to delete it.
print("saved data(1) : ", list[0][0]) 
print("saved data(2) : ", list[1])

# connect 'oxsData.db' and manipulate it
con = sqlite3.connect("oxsData.db")

cur = con.cursor() # use 'cursor' to use DB
# below CREATE command is only used once when the table should be created
# cur.execute("CREATE TABLE Crawlingdata(Name text, Period text);")

idx = 0
while idx < len(list):
	cur.execute("INSERT INTO Crawlingdata VALUES(?, ?);", list[idx])
	# 'INSERT' each value of a list.
	idx += 1
	
con.commit() # The new input is gonna be saved in the DB with 'commit' command

idx = 0

con.close()
