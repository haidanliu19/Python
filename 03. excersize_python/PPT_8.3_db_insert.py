import sqlite3
##변수 선언 부분 ##
conn, cur = None,None
data1,data2, data3, data4 = "","","",""
sql = ""

conn = sqlite3.connect('c:\sqlite\sqlite-tools-win32-x86-3300100\pythonDB')
cur = conn.cursor()

while (True):
    data1 = input("사용자ID   ==>")
    if data1 =="":break
    data2 = input("사용자이름 ==>")
    data3 = input("이메일     ==>")
    data4 = input("출생년도   ==>")

    sql = "INSERT INTO userTable Values('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)

conn.commit()
conn.close()
