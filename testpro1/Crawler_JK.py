from bs4 import BeautifulSoup as BS
from selenium import webdriver
import urllib.request
import urllib.parse
import requests as rq

# 몇 페이지를 크롤링할 것인지 입력한다. 4 pages.
lastPage = 5
pageNum = 1

# chromedriver 경로 : 같은 층에 있으므로 상대 경로
path = 'chromedriver.exe'



while pageNum < lastPage+1:

    # url이 while 내에서 돌아야 하는 이유?
    # pageNum이 지속적으로 변하고 이를 반영해야 하기 때문이다.
    url = f'http://koamma.cbnu.ac.kr/bbs/bbs.php?db=notice&search=%C0%E5%C7%D0&searchKey=subject&category=&pgID=ID12415888101&page={pageNum}'



##### 여기서부터 selenium 사용으로 크롬 드라이버 동작 #####
    driver = webdriver.Chrome(path)
    driver.get(url)
    soup = BS(driver.page_source, 'lxml')
    
    # 타이틀 정보만 수집한다.
    title_list = soup.select("#body_line > nobr > a")

    # 날짜, 조회수 정보를 수집한다.
    date_view_list = soup.find_all(class_ = "body_num")

    # href 정보만 수집한다.
    href_list = soup.select("#body_line > nobr > a")
    
    driver.quit()
##### 여기까지 selenium 사용 및 필요 데이터 추출 완료 #####



    # 타이틀 정보 리스트를 파일로 추출
    file = open('jk_info_title.txt', 'a')
    for ti in title_list:
        file.write(ti.text + '\n')
    file.close()

    # 날짜 정보 리스트를 파일로 추출
    idx = 0
    file = open('jk_info_date.txt', 'a')
    for li in date_view_list:
        if idx % 4 - 2 == 0:
            file.write(li.text + '\n')
        idx += 1
    file.close()

    # 조회수 정보 리스트를 파일로 추출
    idx = 0
    file = open('jk_info_view.txt', 'a')
    for li in date_view_list:
        if idx % 4 - 3 == 0:
            file.write(li.text + '\n')
        idx += 1
    file.close()
    
    # href 정보 리스트를 파일로 추출
    file = open('jk_info_href.txt', 'a')
    for hr in href_list:
        if 'href' in hr.attrs:
            file.write("https://koamma.chungbuk.ac.kr" + hr.attrs['href'] + '\n')
    file.close()

    pageNum += 1 # 다음 페이지 데이터 추출
