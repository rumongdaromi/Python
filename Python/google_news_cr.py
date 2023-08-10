import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://news.google.com/search?q=%EC%9D%B4%EC%A4%80%EC%84%9D&hl=ko&gl=KR&ceid=KR%3Ako")
bs = BeautifulSoup(r.text,"html.parser")
titles = bs.select("div.xrnccd article > h3 > a")

news = []

for i in titles:
    title = i.text
    links = "https://news.google.com" + i.get("href")[1:]
    
    news.append([title, links])
    google_news_df = pd.DataFrame(news,columns = ["기사제목", "링크 주소"])

print(google_news_df)
google_news_df.to_excel("뉴스크롤링결과.xlsx")
print("저장성공 ! ")