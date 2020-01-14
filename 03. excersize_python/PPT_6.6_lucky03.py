#lucky03.py
import random

#random으로 생성
def getNumber(totalNum):
    return random.randint(1,totalNum)

##변수 선언 부분 ##
lotto = []
num = 0
totalNum = 0

#참석 인원수 추가
try:
    while True:
        totalNum = int(input("참석 인원은 몇명입니까?"))
        if totalNum > 0 :break
        else:print("0이상 입력하여 주십시요.")
except ValueError:
    print("참석 인원을 입력하여 주십시요.")
        
while True:

    #마감 종료시   
    if len(lotto) == totalNum :
        print("행운권 추첨 마감되였습니다.다음 기회에 도전하여 주십시요.")
        break

    #행원권 추첨
    start = input("행운권 추첨을 시작합니다.(y/n) **")
    if start not in ('y','n'):
        print("y/n만 가능합니다.")
        continue
            
    if start == "n": break
    
    #당첨된것은 안나오게 하는 것
    while True:
        num = getNumber(totalNum)
        
        if lotto.count(num) == 0:
            lotto.append(num)
        
            print("  당첨번호 : %d" %num)
            print("  당첨되셨습니다.!! 축하합니다. \n")
            break
        else:
            continue
        
