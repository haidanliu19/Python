# c:/crwal/db_create2.py
import sqlite3

con=sqlite3.connect("C:/sqlite/naverDB")
cur = con.cursor()

#cur.execute("DROP TABLE news")
cur.execute("CREATE TABLE news (wrdt date, div char(20), title char(100), writer char(20))")
cur.execute("CREATE INDEX wrdt_idx on news (wrdt)")
#cur.execute("INSERT INTO news VALUES(datetime(), '정치', 'John Bann', 'ydgil')")
con.commit()
con.close()
