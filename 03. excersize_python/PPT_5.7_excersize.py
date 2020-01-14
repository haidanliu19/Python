#262페이지
#1.
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgrageCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgrageCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) #10에서 7을 뺀 3을 출력 


#2.
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
        
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
    

cal= MaxLimitCalculator()
cal.add(50)#50 더하기
cal.add(60)#60 더하기

print(cal.value)#100출력

#3.
all([1,2,abs(-3)-3])#abs(-3)-30
chr(ord('a')) == 'a'

#4.
list(filter(lambda x :x>0 ,[1,-2,3,-5,8,-3]))

#5.
hex(234)
int('0xea',16)

#6.
list(map(lambda x: x* 3, [1,2,3,4]))


#7.
max([-8,2,7,5,-3,5,0,1])
min([-8,2,7,5,-3,5,0,1])

#8.
17 /3
round(17/3,4)

#9.
#import sys
#numbers = sys.argv[1:]#파일 이름을 제외한 명령 행의 모든 입력

#result = 0;
#for number in numbers:
#    result += number
#print(result)

#10.
#import os
#os.chdir("c:\doIt")

#result = os.popen("dir")

#print(result.read())

#11.
import glob
glob.glob("c:\doit\*.py")

#12.
import time
time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))

#13.
import random
result = []

while len(result) < 6:
    num = random.randint(1,45)
    if num not in result:
        result.append(num)

print(result)

