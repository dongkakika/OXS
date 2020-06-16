import urllib.request
import urllib.parse
import codecs # for using '한글'
from bs4 import BeautifulSoup as BS

# 몇 페이지를 크롤링할 것인지 입력한다. 7 pages.
lastPage = 7

pageNum = 1
pageNum2 = 0
while pageNum < lastPage+1:


    
    # 전자공학부 홈페이지의 url
    # 유의할 점은 'search='를 통해 '장학' 키워드에 접근한다는 것
    url =f'https://ece.cbnu.ac.kr/board/list.ht?start={pageNum2}&keyCode=5&sf=0&start1=1'

    html = urllib.request.urlopen(url).read()
    soup = BS(html, "html.parser")

    # 키워드를 이용해 필요한 정보만을 긁어온다.
    tds = soup.find_all("td")

    # 타이틀, 날짜, 조회수를 한 번에 가져와 파일로 만든다.
    idx = 0
    trig = 0
    for td in tds:
        nmg = idx % 5

        # 주의할 점 : 전자정보대학의 공지사항 타이틀에는 noise가 섞여있다.
        if nmg == 1:
            with open("jjd_info_title.txt", "a") as f:
                f.write(td.text.replace('\n',"").replace('\xa0', "").replace('\u5b66', "").replace('\u53d8', "") + '\n')
        elif nmg == 2:
            with open("jjd_info_date.txt", "a") as f:
                f.write(td.text + '\n')
        elif nmg == 4:
            with open("jjd_info_view.txt", "a") as f:
                f.write(td.text + '\n')
        idx += 1

    # 마지막으로 href를 추출하기 위한 코드
    a_group = soup.select("#con > div > div > fieldset > table > tbody > tr > td > a")

    file = open("jjd_info_href.txt", 'a')
    for a in a_group:
        if 'href' in a.attrs:
            file.write('https://ece.cbnu.ac.kr/board/' + a.attrs['href'] + '\n')
    file.close()
    
    # 모든 페이지 다 끝내뿌따ㅠㅠ 아고 목 뿌아지겠네...

    pageNum += 1 # 다음 페이지 데이터 추출
    pageNum2 += 10

