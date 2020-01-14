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
    url = "https://media.daum.net/"
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")
    first_div = bs_obj.find("div",{"class":"box_headline"})
    first_ul_list = first_div.findAll("ul",{"class":"list_headline"})
    #ul
    for first_ul in first_ul_list:
        #li
        first_li_list = first_ul.findAll("li")
        for j in range(1,len(first_li_list)):
            strong_tag = first_li_list[j].find("strong",{"class":"tit_g"})
            a_tag = strong_tag.find("a",{"class":"link_txt"})
            writer = strong_tag.find("span", {"class": "info_news"})
            if a_tag != None:
                data1 = "daum"  # 뉴스 구분
                data2 = a_tag.text.strip()
                data2 = data2.replace("'", "\"")  # 뉴스 제목
                data3 = writer.text  # 작성자
                sql = "INSERT INTO news1 VALUES(datetime('now','localtime'),'" + data1 + "', '" + data2 + "', '" + data3 + "')"
                print(sql)
                cur.execute(sql)

    con.commit()
    con.close()
    time.sleep(3600)  # 한시간 마다 들어간다.




