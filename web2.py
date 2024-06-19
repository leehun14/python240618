#web2.py
#웹서버와 통신
import requests

#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#파일로 저장(append, read, write)
f = open("daangn.txt", "a+", encoding = "utf-8")

posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.strip()
    price = priceElem.text.strip()
    addr = addrElem.text.strip()
    #파이썬 3.6 f-string문법
    print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}\n")

#  <div class="card-desc">
#       <h2 class="card-title">아이폰12프로맥스 512기가</h2>
#       <div class="card-price ">
#         650,000원
#       </div>
#       <div class="card-region-name">
#         서울 강북구 삼각산동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 10
#           </span>
#         ∙
#         <span>
#             채팅 76
#           </span>
#       </div>