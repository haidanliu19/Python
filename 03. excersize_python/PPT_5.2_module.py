#함수->클래스->모듈->패키지
#II. 모듈
#함수나 변수 또는 클래스를 모아 놓은 파일
#다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 함
#모듈 만들기
# mod1.py
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

#import 모듈 이름

#모듈 불러오기
import mod1
print(mod1.add(3,4))
print(mod1.sub(3,4))


#from 모듈 이름 import 모듈 함수
from mod1 import add
add(3,4)

#from mod1 import add, sub
#from mod1 import *
#if __name__ == “__main__”: 의 의미

# mod1.py 
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

if __name__ == "__main__":
    print(add(1,4))
    print(add(4,2))
#python mod1.py cmd창에서 호출 


#클래스나 변수 등을 포함한 모듈
# mod2.py
PI = 3.141592

class Math:
    def solv(self,r):
        return PI * (r **2)

def add(a,b):
    return a+b

if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(add(PI,4.4))

#mod2.py 모듈을 다른 파일에서 불러오기
# modtest.py
import mod2
result = mod2.add(3,4)
print(result)

# CMD창에서 해결 하는 방법
# cd C:\doit
# mkdir mymod #새 디렉터리 생성
# move mod2.py mymod #지정한 디렉터리로 파일 이동

#1.sys.path.append(모듈을 저장한 디렉터리)사용하기
#import sys
#sys.path
#sys.path.append("C:/doit/mymod")
#2.pythonpathn 환결 변수 사용하기
#set PYTHONPATH = C:\doit\mymod
#python
#import mod2

