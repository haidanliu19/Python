import sqlite3
##변수 선언 부분 ##
conn, cur = None,None
data1,data2, data3, data4 = "","","",""
sql = ""

conn = sqlite3.connect('c:\sqlite\sqlite-tools-win32-x86-3300100\pythonDB')
cur = conn.cursor()

#id = input("사용자 id입력 ==>")
#cur.execute("select * from userTable where id='"+id+"'")
cur.execute("select * from userTable")
print("사용자ID 사용자이름 이메일 출생년도")
print("-"*100)
while (True):
    row = cur.fetchone()#조회
    if row ==None:break
    data1= row[0]
    data2= row[1]
    data3= row[2]
    data4= row[3]
    print("%5s %15s %15s %d" % (data1,data2,data3,data4))
    
conn.close()
