import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
#html이라는 변수 안에 텍스트 형식으로 네이버 첫
#페이지를 호출한 데이터가 문자열 형태로 들어감
#print(html.read())
bs_obj = bs4.BeautifulSoup(html,"html.parser")# bs_obj에는 전체 소스가 들어 있음
#print(bs_obj)
top_right = bs_obj.find("div",{"class":"area_links"})
#div 태그 중에서 class가 “area_links”로 되어있는 div를 찾으라는 명령
#print(top_right)
first_a = top_right.find("a")#첫 번째 나오는 a태그를 찾음
print(first_a)# a태그 안에 있는 text만 뽑아냄
print(first_a.text)

first_a1 = bs_obj.find("a",{"class":"al_favorite"})
print(first_a1.text)

###공지사항
notice_div = bs_obj.find("div",{"class":"area_notice"})
notice_a = notice_div.find("a",{"class":"an_ta"})
print(notice_a.text)

notice_h2 = bs_obj.find("h2",{"class":"blind"})
print(notice_h2)
