import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

pageNum = 1
lastPage = 3 # 크롤링할 페이지 수

while pageNum < lastPage+1:
    url = f'https://www.chungbuk.ac.kr/site/www/boardList.do?page={pageNum}&boardSeq=113&key=699&searchType=TITLE&searchKeyword=%EC%9E%A5%ED%95%99'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")


    # '공지'로 상단에 고정처리되어 반복적으로 긁어와지는 게시글을 카운팅한다.
    how_many_gongji = soup.find_all(style="font-weight:bold;")

    # 카운팅한 개수를 아래의 각종 정보를 수집할 때 꼭 활용해야 한다.
    # '공지'의 개수는 매번 변동하므로 동적인 크롤링을 위함임
    count = 0
    for h in how_many_gongji:
        count += 1

    # '장학'과 관련된 모든 글을 긁어온다.
    total_subject = soup.find_all(class_='subject')

    # print(count) # 카운팅된 횟수만큼 매 페이지마다 게시글을 무시한다.
    
    # 모든 타이틀 정보를 수집한다.
    file = open('cbnu_info_title.txt', 'a')
    idx = 0 # 1부터 14까지 한 페이지의 모든 내용에 접근하는 인덱스
    for title in total_subject:
        idx += 1
        if(idx - count <= 0): continue
        file.write(title.text.replace('\n',"").replace('\r', "").replace('\t', "") + '\n')
    file.close()


    # 조회수와 날짜 두 정보를 수집하는 many_list 선언 및 초기화
    many_list = soup.select("#contents > div > form > table > tbody > tr > td")

    
    # 처리 전 날짜 정보를 리스트에 수집한다.
    idx2 = 1
    not_processed_list = []
    for i in many_list:
        if (idx2 % 6 == 0):
            not_processed_list.append(i.text.replace('\n',"").replace('\r', "").replace('\t', "") + '\n')
        idx2 += 1
    
    # print(not_processed_list)

    # 처리 후 날짜 정보를 파일에 저장한다
    file = open('cbnu_info_date.txt', 'a')
    idx3 = 1
    for p in not_processed_list:
        if idx3 - count > 0: # count가 굵은 글씨체로 상단에 고정된 '고정' 게시글의 개수 임에 주의
            file.write(p)
        idx3 += 1
    file.close()

    # 조회수 정보만을 수집하기 위해 td의 텍스트들만을 정리한 리스트 구성
    idx4 = 1
    not_processed_list = []
    for td in many_list:
        not_processed_list.append(td.text.replace('\n',"").replace('\r', "").replace('\t', "") + '\n')
        idx4 += 1

    # td의 텍스트(장학 게시글 전체) 처리를 거쳐 필요한 조회수 정보만을 수집
    idx5 = 1
    idx6 = 1
    file = open('cbnu_info_view.txt', 'a')
    for pi in not_processed_list:
        if(idx5 % 6 == 5):
            if(idx6 > count): # count가 굵은 글씨체로 상단에 고정된 '고정' 게시글의 개수 임에 주의
                file.write(pi)
            idx6 += 1
        idx5 += 1
    file.close()

    # first = soup.select("#contents > td")
    # hrefs = first.findAll("a")
    # many_list의 1, 7, 13, 19...번째는 모두 href와 제목을 가지고 있음
    # count * 6의 범위 안에 들어오는 '현재' 1, 7, 13, 19는 모두 '공지'
    # lastPage * 한 페이지 게시글 maximum이 전체 게시글 범위이고,
    # many_list의 idx 범위를 위의 게시글 범위에 맞춰서 제한해야 한다.
    # Solution --> 가장 간단하게 many_list의 len을 구하면 된다.
    # 게시판의 한 페이지는 count + 10 인가? 아니면 10도 유동적으로 변하나?
    # ↓현재 84개 = ( 10 + 4(공지) ) * 6(한 게시글의 리스트 요소 수)
    # print(len(many_list))
    idx7 = 1
    file = open('cbnu_info_href.txt', 'a')
    for li in range(len(many_list)):
        if li % 6 == 1:
            if idx7 > count :
                file.write("https://www.chungbuk.ac.kr/site/www" + str(many_list[li])[57:181].replace('amp;',"") + '\n')
            idx7 += 1
        li += 1
    file.close()

    # <<< 참고 >>>
    # class인 bs4.element.Tag가 str 변환이 먹힐 줄 몰랐다...
    # print(str(many_list[1])[57:181].replace('amp;',""))
    # print(str(many_list[7])[57:181].replace('amp;',""))
    # print(str(many_list[13])[57:181].replace('amp;',""))
    # print(str(many_list[19])[57:181].replace('amp;',""))
    # print(str(many_list[25])[57:181].replace('amp;',""))

    # 반복문 인덱스 추가
    pageNum += 1
    

