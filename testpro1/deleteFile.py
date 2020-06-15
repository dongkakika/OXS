import os
import time

# DB에 반영 후 수집 데이터 삭제

time.sleep(30)

os.remove('sw_info_title.txt')
os.remove('sw_info_view.txt')
os.remove('sw_info_date.txt')
os.remove('sw_info_href.txt')

os.remove('com_info_title.txt')
os.remove('com_info_view.txt')
os.remove('com_info_date.txt')
os.remove('com_info_href.txt')

os.remove('jj_info_title.txt')
os.remove('jj_info_view.txt')
os.remove('jj_info_date.txt')
os.remove('jj_info_href.txt')
