#naver_news_db2.py
import urllib.request
import bs4
import time
import sqlite3

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3 = "", "", ""
sql = ""

# 메인 코드 부분 ##
while True:
    url = "http://news.naver.com/"
    html = urllib.request.urlopen(url)

    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    hdline_article_list = bs_obj.find("ul", {"class":"hdline_article_list"})
    lis = hdline_article_list.findAll("li")

    con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
    cur = con.cursor()

    for li in lis:
        a = li.find("a")
        a.text.strip()

        data1 = "정치"  # 뉴스 구분
        data2 = a.text.strip()
        data2 = data2.replace("'", "\"")  # 뉴스 제목
        data3 = "ydgil"  # 작성자

        sql = "INSERT INTO news1 VALUES(datetime(), '" + data1 + "', '" + data2 + "', '" + data3 + "')"
        cur.execute(sql)

    con.commit()
    con.close()
    time.sleep(3600)
