coffee = 10
while True:
    #money,cnt = input("돈과 개수를 넣어 주세요:").split()
    money = int(input("돈을 넣어 주세요:"))
    if money == 300:
        print("커피를 줍니다.") 
        coffee -= 1
    elif money > 300:
        #print(money%300)
        #print(money//300)
        maxCnt = money//300
        if maxCnt > coffee:
            maxCnt = coffee
        if maxCnt > 1:
            cnt = int(input(f'%d잔 이하 가능합니다.몇잔 하시겠습니까?' % maxCnt))
        else:
            cnt = maxCnt
        print("거스롬돈 %d를 주고 커피를 줍니다." % (money - 300*cnt ))
        coffee -= cnt
            
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다." % coffee)

    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
