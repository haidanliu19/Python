#naver_news_db_write_file.py
import urllib.request
import bs4
import time
import os
import sqlite3

con, cur = None, None
data0,data1, data2, data3 ="", "", "", ""
row = None
sql = ""
result = ""
con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

cur.execute("select * from news1")
f = open("news.txt",'w')
while True:
    row = cur.fetchone()
    if row == None:
        break
    data0 = row[0]
    data1 = row[1]
    data2 = row[2]
    data3 = row[3]
    result = data0+"|"+data1+"|"+data2+"|"+data3+"\n"
    f .write(result)

f.close()
