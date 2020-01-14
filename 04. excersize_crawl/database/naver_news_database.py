#naver_news_database.py
import urllib.request
import bs4
import time
import os
import sqlite3

con, cur = None, None
data1, data2, data3 = "", "", ""
sql = ""

con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

while True:
    url = "https://news.naver.com/"
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    ul = bs_obj.find("ul", {"class": "hdline_article_list"})
    div = ul.findAll("div", {"class": "hdline_article_tit"})

    # print(lis)

    for i in range(0, len(div)):
        a_tag = div[i].find("a")
        print(a_tag.text.strip())

        data1 = "헤드라인"
        data2 = a_tag.text.strip()
        data2 = data2.replace("'","\"")
        data3 = "SHee28"
        sql = "INSERT INTO news VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "')"
        #print(sql)
        cur.execute(sql)
    # print(sql)
    

    con.commit()
    con.close()

    # time.sleep(5)
    # os.system("cls")
