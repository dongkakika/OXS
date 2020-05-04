from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

Url = "https://www.chungbuk.ac.kr/site/www/boardList.do?boardSeq=113&key=699"
print(Url)

driver = webdriver.Chrome()
driver.get(Url)
