import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as BS

# 몇 페이지를 크롤링할 것인지 입력 받는다. 5 pages.
lastPage = 5

pageNum = 1
while pageNum < lastPage+1:

    # 충북대학교 홈페이지의 url
    # 유의할 점은 'search='를 통해 '장학' 키워드에 접근한다는 것
    url = f'https://www.chungbuk.ac.kr/site/www/boardList.do?page={pageNum}&boardSeq=113&key=699&searchType=ALL&searchKeyword=%EC%9E%A5%ED%95%99'

    html = urllib.request.urlopen(url).read()
    soup = BS(html, "html.parser")

    # 키워드를 이용해 필요한 정보만을 긁어온다.
    link_list = soup.select("#body_line > nobr > a ")
    body_line = soup.find_all(id = "body_line")
    body_num = soup.find_all(class_ = "body_num")

    # 날짜 정보만 습득 ( 조건문의 비교 연산의 숫자가 핵심이다. )
    file = open('cbnu_info_date.txt', 'a')
    b = 1
    for a in body_num:
        if(b%4 == 3):
            file.write(a.text + '\n')
        b += 1
    file.close()

    # 조회수 정보만 습득 
    file = open('cbnu_info_view.txt', 'a')
    b = 1
    for a in body_num:
        if(b%4 == 0):
            file.write(a.text + '\n')
        b += 1
    file.close()

    # 타이틀 정보만 습득
    file = open('cbnu_info_title.txt', 'a')
    for link in link_list:
        if 'href' in link.attrs:
            file.write(link.text + '\n')
    file.close()

    # href 정보만 습득
    file = open('cbnu_info_href.txt', 'a')
    for link in link_list:
        if 'href' in link.attrs:
            file.write("https://www.chungbuk.ac.kr" + link.attrs['href'])
            file.write("\n")
    file.close()

    pageNum += 1 # 다음 페이지 데이터 추출
