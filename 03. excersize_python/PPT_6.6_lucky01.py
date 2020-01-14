#lucky01.py
import random

##함수 선언 부분 ##
def getNumber():
    return random.randint(1,200)

##메인 프로그램 부분 ##
print("** 행운권 추첨을 시작합니다 ** ")
num = getNumber()
print("당첨번호 : %d" % num)
print("당첨되셨습니다. !! 축하합니다.\n")
