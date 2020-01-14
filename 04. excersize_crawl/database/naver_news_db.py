#naver_news_db.py
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
    #div = bs_obj.findAll("div",{"class":"mtype_list_wide"})
    #print(div)
    first_h = bs_obj.find("ul", {"class": "hdline_article_list"})
    lis = first_h.findAll("li")
    # print(lis)

    #헤드라인 뉴스 검색
    for i in range(len(lis)):
        a = lis[i].find("a")

        data1 = "헤드라인 뉴스"  # 뉴스 구분
        data2 = a.text.strip()
        data2 = data2.replace("'", "\"")  # 뉴스 제목
        data3 = "hhh"  # 작성자
        sql = "INSERT INTO news1 VALUES(datetime('now','localtime'),'" + data1 + "', '" + data2 + "', '" + data3 + "')"
        print(sql)
        cur.execute(sql)

    #기타 뉴스 검색
    first_a_list = bs_obj.findAll("ul",{"class":"mlist2 no_bg"})
    title = bs_obj.findAll("h4")#title가져오기

    for i in range(len(first_a_list)):
        lis = first_a_list[i].findAll("li")

        for li in lis:
            a = li.find("a")
            writer= li.find("span",{"class":"writing"}).text

            data1 = title[i+1].text #뉴스 구분
            data2 = a.text.strip()
            data2 = data2.replace("'", "\"")#뉴스 제목
            data3 = writer#작성자
            sql = "INSERT INTO news1 VALUES(datetime('now','localtime'),'" + data1 + "', '" + data2 + "', '" + data3 + "')"
            print(sql)
            cur.execute(sql)

    con.commit()
    con.close()
    time.sleep(3600)#한시간 마다 들어간다.
    # os.system("cls")
