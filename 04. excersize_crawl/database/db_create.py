#db_create.py
import sqlite3

con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

cur.execute("DROP TABLE news")#테이블 있으면 삭제하고 해야 한다.
#위에것 최초생성시 주석 처리한다.
cur.execute("CREATE TABLE news (div char(10), title char(100), writer char(10))")

con.commit()
con.close()