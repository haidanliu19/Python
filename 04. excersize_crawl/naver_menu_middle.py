#naver_menu_middle.py
import urllib.request
import bs4
url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

div = bs_obj.find("div", {"class": "rolling-container"})

lis = div.findAll("li")
#print(lis)

for i in range(0, len(lis)):
    a_tag = lis[i].find("a")
#    span_tag = a_tag.find("span", {"class": "an_txt"})
    print(a_tag.text)
