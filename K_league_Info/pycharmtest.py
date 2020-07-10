import re

import requests
from bs4 import BeautifulSoup

#K리그 일정 페이지 크롤링 --> 고정 url이 아니라 똑같이 메인홈페이지에서 가져와서 그때그때 최신 일정으로 받아올 수 있게
webpage = requests.get("http://www.kleague.com/schedule?ch=091425")
soup = BeautifulSoup(webpage.content, "html.parser")

# 경기 날짜 배열로 각각 파싱하여 저장
"""
dates = str(soup.find_all('th'))
dates = re.sub('<.+?>','',dates,0).strip().split(", ")
"""

games = str(soup.find_all('table'))
games = re.sub('<.+?>','',games,0).strip()
games = games.replace(" ","").replace("-->","").replace("\n\n","")
games = re.sub("R\d::\d::",'',games,0)#10R1594204412::1593853200::지우면 끝

#각각 id찾아서 들어가면 됨
matchcenter = str(soup.find_all('button',class_="btn btn-outline-blue btn_matchcenter"))
matchcenter = matchcenter.replace(" ","")
matchcenter = re.sub("\D", " ", matchcenter, 0).replace("  ","").split(" ")


print(games)
print(matchcenter)
