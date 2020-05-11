from Crawling.stringGetter import getPageString
from bs4 import BeautifulSoup

def getLists(string)
    bsObj = BeautifulSoup(string, "html.parser")

    print(bsObj)
    return []

url = "https://www.chungbuk.ac.kr/site/www/boardList.do?page=1&boardSeq=113&key=699"
pageString = getPageString(url)
print(getLists(PageString))