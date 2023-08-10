import requests
from bs4 import BeautifulSoup

r= requests.get("https://vibe.naver.com/chart/total")
bs = BeautifulSoup(r.text,"html.parser")

#가수의 목록 
#노래의 목록

song_name = []
singer_name = []

song = bs.select("tr > td.song > div.title")
print(song)