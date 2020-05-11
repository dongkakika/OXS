from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.chungbuk.ac.kr/site/www/boardList.do?page=1&boardSeq=113&key=699"

print(url)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

subject = soup.select(".subject")
print(subject)

driver.close()