#III. 파일 읽고 쓰기
#파일 생성하기 
#파일을 생성하기 위해 open이라는 내장 함수를 사용함
f = open("새파일.txt",'w')
f.close()
#파일 객체 = open(파일 이름, 파일 열기 모드)
#r 읽기 모드 - 파일을 읽기만 할 때 사용
#w 쓰기 모드 - 파일에 내용을 쓸 때 사용
#a 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
#writedata.py
f = open("c:\doit\새파일.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법 
#1. readline() 함수 이용하기
#readline.py 
f = open("c:\doit\새파일.txt",'r')
line = f.readline()
print(line)
f.close()
#모든 줄을 읽어서 화면에 출력하고 싶다면 다음과 같이 작성하면 됨
#readline_all.py 
f = open("c:\doit\새파일.txt",'r')
while True:
    line = f.readline()
    if not line:break
    print(line)
f.close()

f = open("c:\doit\새파일.txt",'r')
while 1:
    line = f.readline()
    if not line:break
    print(line)
f.close()



#2. readlines() 함수 이용하기
#readlines.py
f = open("c:\doit\새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#3. read() 함수 이용하기
#read.py
f = open("c:\doit\새파일.txt",'r')
data = f.read()
print(data)
f.close()

#파일에 새로운 내용 추가하기
#원래 있던 값을 유지하면서 새로운 값만 추가할 때는 파일을 추가 모드(‘a’)로 열면 됨
#adddata.py
f = open("c:\doit\새파일.txt",'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


#with문과 함께 사용하기
f = open("c:\doit\새파일.txt",'w')
f.write("Life is too short, you need python")
f.close()

#하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리하는 것이 편리하지 않을까?
with open("C:\doit\foo.txt", 'w') as f:
    f.write("Life is too short, you need python")

#sys 모듈로 매개변수 주기
#명령 프롬프트 명령어 [인수1  인수2  …]
#sys1.py
import sys

args = sys.argv[1:]
for i in args:
    print(i)
#python  sys1.py  aaa bbb ccc
#aaa
#bbb
#ccc

#문자열 관련 함수인 upper()를 이용하여 명령 행에 입력된 소문자를 대문자로 바꾸어 주는 프로그램임
#sys2.py
import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end = ' ')
