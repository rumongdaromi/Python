# #requests
# #BeautifulSoup  html 을 파이썬이 알아볼 수 있게 파싱함
# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://www.naver.com")
# #print(r.text)
# bs = BeautifulSoup(r.content,"html.parser")

# # h3 = bs.select_one("h3 > a") # h3의 자식요소를 출력핳 때

# selecter = bs.find("div",{"class": "partner_box"})
# print(selecter.text)

import requests
from bs4 import BeautifulSoup

r= requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=오늘의+날씨")
bs = BeautifulSoup(r.content,"html.parser")
whather = bs.select("div.temperature_info > dl > dd.desc")
#print("오늘의 체감온도는 : {} 입니다. ".format(whather[0].text))
print(whather)