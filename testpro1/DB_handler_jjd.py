import sqlite3
import codecs # for using '한글'
import os

# 타이틀 정보 읽어오기
f = codecs.open("jjd_info_title.txt", "r")
title_list = []
while True:
	line = f.readline()             # 한 줄씩 읽
	if not line: break              # break the loop when it's End Of File
	title_list.append(line)       # split the line and append it to list
f.close()

# 날짜 정보 읽어오기
f = codecs.open("jjd_info_date.txt", "r")
date_list = []
while True:
	line = f.readline()             # 한 줄씩 읽
	if not line: break              # break the loop when it's End Of File
	date_list.append(line)       # split the line and append it to list
f.close()

# 조회수 정보 읽어오기
f = codecs.open("jjd_info_view.txt", "r")
view_list = []
while True:
        line = f.readline()
        if not line: break
        view_list.append(line)
f.close

# href(링크) 정보 읽어오기
f = codecs.open("jjd_info_href.txt", "r")
href_list = []
while True:
        line = f.readline()
        if not line: break
        href_list.append(line)
f.close

################################################################################
###################################### DB ######################################
# below 'print' is for checking the data structure. Don't care.
#print("saved data(1) : ", list[0][0]) 
#print("saved data(2) : ", list[1])

# connect 'db.sqlite3' in the django folder and manipulate it
con = sqlite3.connect("db.sqlite3")
cur = con.cursor() # use 'cursor' to use DB

# you don't need to care the below CREATE TABLE command.
# cur.execute("CREATE TABLE if not exists website1_crawlingdata(Name text, Period text);")

total_list = []
for i in range(len(date_list)):
        temp = [str(i+1), title_list[i], date_list[i], view_list[i], href_list[i]]
        total_list.append(temp)

# print(total_list)

cur.execute("delete from website1_jjd_info;")

idx = 0 # 리스트의 인덱스에 접근하는 변수
while idx < len(date_list):
	cur.execute("INSERT INTO website1_jjd_info VALUES(?, ?, ?, ?, ?);", total_list[idx])
	# 'INSERT' each value of the total_list to the table of DB.
	idx += 1
	
con.commit() # The new input is gonna be saved in the DB with 'commit' command

idx = 0

con.close()
