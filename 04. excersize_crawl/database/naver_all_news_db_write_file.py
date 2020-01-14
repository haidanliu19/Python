#naver_all_urllib.request
import bs4
import time
import os
import sqlite3
import csv

con, cur = None, None
data0,data1, data2, data3 ="", "", "", ""
row = None
sql = ""
result = ""
con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

cur.execute("select * from news1")
f = open("news.csv",'w',encoding="UTF-8")#경로 바꿀 수 있음
list = []

while True:
    row = cur.fetchone()
    if row == None:
        break
    #list = []
    #list.insert(0,row[0])
    #list.insert(1, row[1])
    #list.insert(2, row[2])
    #list.insert(3, row[3])
    #wr = csv.writer(f)
    #wr.writerow(list)
    result = ""
    data0 = row[0].strip()
    data1 = row[1].strip()
    data2 = row[2].replace(",", ".")
    data3 = row[3]

    result = "%s, %s, %s, %s\n" % (data0,data1,data2,data3)
    print(result)
    #result = data0+","+ data1+","+data2+","+ data3+"\n"
    f.write(result)

con.close()
f.close()