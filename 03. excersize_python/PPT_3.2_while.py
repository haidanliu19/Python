# while문의 기본 구조 
# 반복해서 문장을 수행해야 할 경우 while문을 사용함 
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

#while문 만들기
#number라는 변수에 0을 먼저 대입함 
prompt = """
1. Add
2. Del
3. 3.List
4. Quit

Enter number:"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())

# while문 강제로 빠져나가기 (break)
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남의 커피의 양은 %d개입니다."  % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#실제 자판기 작동 과정을 만든 예
#coffee.py
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요:"))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다."  % (money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다." % coffee)

    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
              
# while문의 맨 처음으로 돌아가기 (continue) 
a = 0
while a < 10:
    a += 1
    if a % 2 == 0 :continue
    print(a)

#136페이지
#1부터 10까지의 숫자 중에서 3의 배수를 뺀 나머지 값을 출력해 보자
a = 0
while a < 10:
    a += 1
    if a % 3 == 0 :continue
    print(a)

#무한 루프
while True:
    print("CTRL+C를 눌러야 while문을 빠져나갈 수 있습니다.")

#응용예제01. 로그인 프로그램
myId = "python"
myPsswd = "1234"
count = 0

while True:
    #usrId = input("아이디를 입력하세요.")
    #usrPwd = input("패스워드를 입력하세요.")
    if count >= 5 :
        print("시도 횟수 초과하였습니다.")
        break
    userId, userPwd = input("아이디와 패스워드를 ,로 구분하여 입력하세요").split()
    
    if userId == myId and myPsswd == userPwd:
        print("정상적으로 로그인에 성공했습니다.")
        break
    elif userId != myId and myPsswd == userPwd:
        print("아이디가 틀렸습니다.\n")
    elif userId == myId and myPsswd != userPwd: 
        print("패스워드가 틀렸습니다.\n")
    else:
        print("아이디와 패스워드가 틀렸습니다.\n")
    count+=1 #최대한 공간을 줄이기 위해서 마지막에 연다.


#응용예제02. 별 모양 출력하기
#실습
#i = 0
#while True:
#    i += 1
#    if i>5:break
#    print("\u2605"*i+"\n")

#for문
#1.
input1 = input("1.숫자를 여러 개 입력하세요 :")
for i in input1:
    print("\u2605"*int(i))
print("="*50)

#while문
#2.
cnt = 0
input1 = input("2.숫자를 여러 개 입력하세요 :")
while cnt < len(input1):
    print("\u2605"*int(input1[cnt]))
    cnt+=1
print("="*50)

#3.
cnt = 0
input1 = input("3.숫자를 여러 개 입력하세요 :")
while input1[cnt:]:
    print("\u2605"*int(input1[cnt]))
    cnt+=1
print("="*50)

#4.
cnt = 0
input1 = input("4.숫자를 여러 개 입력하세요 :")
while input1[cnt]:
    print("\u2605"*int(input1[cnt]))
    cnt+=1
    if len(input1) == cnt:
        break
print("="*50)

#5.
input1 = input("5.숫자를 여러 개 입력하세요 :")
for i in range(len(input1)):
    print("\u2605"*int(input1[i]))
print("="*50)

#6.
#list내포는 result리스트로 만든다.
input1 = input("6.숫자를 여러 개 입력하세요 :")
result =["\u2605"*int(n) for n in input1]
print(result)


