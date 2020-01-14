import sqlite3
conn = sqlite3.connect('c:\sqlite\sqlite-tools-win32-x86-3300100\pythonDB')


c = conn.cursor()
c.execute("Drop TABLE userTable")
c.execute("CREATE TABLE userTable(id char(4),userName char(15),email char(15),birthYear int)")

c.execute("Insert into userTable values('john','John Bann','john@naver.com',1990)")
c.execute("Insert into userTable values('kim','Kim Chi','Kim@naver.com',1992)")
c.execute("Insert into userTable values('lee','Lee Pal','lee@naver.com',1988)")
c.execute("Insert into userTable values('park','Park su','park@naver.com',1980)")

conn.commit()

conn.close()
