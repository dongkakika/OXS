from bs4 import BeautifulSoup as BS
import requests as rq
import urllib.request
import urllib.parse


# 몇 페이지를 크롤링할 것인지 입력 받는다. 시작 페이지는 '1'.
i = input("몇 페이지를 크롤링 할까요? :")
lastPage = int(i)

file = open('소웨장학정보.txt', 'w')

pageNum = 1
while pageNum < lastPage+1:

    # 소프트웨어학과 홈페이지의 url
    url =f'https://software.cbnu.ac.kr/bbs/bbs.php?db=notice&search=%C0%E5%C7%D0&searchKey=subject&category=&pgID=ID12415888101&page={pageNum}'

    html = urllib.request.urlopen(url).read()
    soup = BS(html, "html.parser")

    link_list = soup.select("#body_line > nobr > a ")
    
    for link in link_list:
        if 'href' in link.attrs:
            file.write(link.text + '\n')
            file.write("https://software.cbnu.ac.kr" + link.attrs['href'])
            file.write("\n")
    
    pageNum += 1

file.close()
