#naver_menu_right.py
import urllib.request
import bs4
url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
ul = bs_obj.find("ul", {"id": "PM_ID_serviceNavi"})
lis = ul.findAll("li")
#print(lis)
for i in range(0, len(lis)):
    a_tag = lis[i].find("a")
    span_tag = a_tag.find("span", {"class": "an_txt"})
    print(span_tag.text)

