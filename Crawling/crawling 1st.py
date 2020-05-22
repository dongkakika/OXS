from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.chungbuk.ac.kr/site/www/boardList.do?page=1&boardSeq=113&key=699"
path = './chromedriver'

print(url)

driver = webdriver.Chrome(path)
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

subject = soup.select(".subject")
print(subject)

driver.quit()
