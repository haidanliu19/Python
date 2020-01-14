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
    url = "https://news.google.com/?hl=ko&tab=rn1&gl=KR&ceid=KR:ko"
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")
    div_list = bs_obj.findAll("div",{"class":"xrnccd F6Welf R7GTQ keNKEd j7vNaf"})

    title_list = bs_obj.findAll("a",{"class":"wmzpFf"})

    #ul
    title=""
    for i in range(len(div_list)):
        #li
        a_list = div_list[i].findAll("a",{"class":"DY5T1d"})
        for i in range(len(a_list)):
            writer = div_list[i].findAll("a",{"class":"wEwyrc AVN2gc uQIVzc Sksgp"})[i]

            data1 = "google"  # 뉴스 구분
            data2 = a_list[i].text.strip()
            data2 = data2.replace("'", "\"").replace("\u2027","")  # 뉴스 제목
            print(data2)
            data3 = writer.text  # 작성자
            sql = "INSERT INTO news1 VALUES(datetime('now','localtime'),'" + data1 + "', '" + data2 + "', '" + data3 + "')"
            print(sql)
            cur.execute(sql)


    con.commit()
    con.close()
    time.sleep(3600)  # 한시간 마다 들어간다.




