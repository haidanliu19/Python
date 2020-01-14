#VI. 외장 함수
# sys
# C:/doit/Mymod/argv_test.py
import sys
print(sys.argv)
#['C:\\doIt\\excersize\\PPT_5.6_external_function.py']현재 위치

#강제로 스크립트 종료하기
#sys.exit

#자신이 만든 모듈 불러와 사용하기
# sys.path
import sys
sys.path


# C:/doit/Mymod/path_append.py
import sys
sys.path.append("C:/doit/Mymod")

#pickle
import pickle
f = open("test.txt",'wb')
data = {1:'python' , 2:'you need'}
pickle.dump(data,f)
f.close()

import pickle
f = open("test.txt",'rb')
data = pickle.load(f)
print(data)

#os
import os 
os.environ 

os.environ['PATH']

#위치 바꾸기
#os,chdir("")

#디렉토리 위치 돌려받기
os.getcwd()


#시스템 명령어 호출하기 - os.system
os.system("dir")

#실행한 시스템 명령어의 결과값 리턴 받기 - os.popen
f= os.popen("dir")

import shutil
shutil.copy("test.txt", "dst.txt")

#glob
import glob
glob.glob("C:\doIt\q*")

#tempfile
#tempfile.mktemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려줌
import tempfile
filename = tempfile.mktemp()
filename

#tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려줌
import tempfile
f = tempfile.TemporaryFile()
f.close()

#time
#time.time
import time
time.time()

#time.localtime
time.localtime(time.time())

#time.asctime
time.asctime(time.localtime(time.time()))

#time.ctime
time.ctime()

#time.strftime 
import time
time.strftime('%x',time.localtime(time.time()))
time.strftime('%c',time.localtime(time.time()))


#sleep1.py
import time
for i in range(10):
    print(i)
    time.sleep(1)


import calendar
print(calendar.calendar(2020))

calendar.prcal(2020)

calendar.prmonth(2020,1)
calendar.weekday(2020,1,7)
calendar.monthrange(2020,1)

import random
random.random()
random.randint(1,10)
random.randint(1,55)
random.randrange(0,29)

#random_pop.py
import random
def random_pop(data): #리스트의 요소 중에서 무작위로 하나를 선택하여 꺼내서 돌려줌
    number = random.randint(0,len(data)-1)
    return data.pop(number)#꺼내진 요소는 pop 메소드에 의해 사라짐

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))


def random_pop(data): 
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))


import random
data = [1,2,3,4,5]
random.shuffle(data)
data

import webbrowser
webbrowser.open("http://google.com")

webbrowser.open_new("http://google.com")
