#naver_headlinenews.py
import urllib.request
import bs4
import time
import os
while True:
    url = "https://news.naver.com/"
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    ul = bs_obj.find("ul", {"class": "hdline_article_list"})
    div = ul.findAll("div", {"class": "hdline_article_tit"})

    #print(lis)
    for i in range(0, len(div)):
        a_tag = div[i].find("a")
        print(a_tag.text.strip())

    time.sleep(5)
    os.system("cls")
