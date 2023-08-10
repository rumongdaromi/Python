# 웹페이지에 들어가지 않고 뉴스 검색 , 기사제목 , 본문 ,링크 ,게시날짜를 엑셀에 담아 저장

from turtle import title
import requests
from bs4 import BeautifulSoup
import pandas as pd
# 웹페이지에 들어가지않고 검색

keyword = input("검색하고자 하는 키워드를 입력해 주세요.  >  ")

r = requests.get("https://news.google.com/search?q=" + keyword + "&hl=ko&gl=KR&ceid=KR%3Ako")  # %20 = 띄어쓰기 1번
bs = BeautifulSoup(r.text,"html.parser")
#titles = bs.select("div.xrnccd article > h3 > a")
titles = bs.find_all("div",{"class":"xrnccd"})
news = []

for i in titles:
    title = i.find("h3").text
    links = "https://news.google.com" + i.find("a")["href"][1:]
    date = i.find("time").text
    
    news.append([title, links , date])
    goNews_df = pd.DataFrame(news, columns=["기사제목","링크주소","게시날짜"])

goNews_df.to_excel("뉴스크롤링결과3.xlsx")
print("저장성공 ! ")

# for i in titles:
#     title = i.text
#     links = "https://news.google.com" + i.get("href")[1:]
    
#     news.append([title, links])
#     google_news_df = pd.DataFrame(news,columns = ["기사제목", "링크 주소"])

#print(google_news_df)
#google_news_df.to_excel("뉴스크롤링결과.xlsx")
#print("저장성공 ! ")

