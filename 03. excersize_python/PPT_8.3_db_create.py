import sqlite3

con = sqlite3.connect("C:/sqlite/naverDB")
cur = con.cursor()

#cur.execute("DROP TABLE news")
cur.execute("CREATE TABLE news (div char(10), title char(100), writer char(10))")

con.commit()
con.close()