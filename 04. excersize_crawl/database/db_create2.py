#db_create2.py
import sqlite3

con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

cur.execute("DROP TABLE news1")
cur.execute("CREATE TABLE news1 (wrdt data,div char(20),title char(100),writer char(20))")
cur.execute("create index wrdt on news1 (wrdt)")

con.commit()
con.close()