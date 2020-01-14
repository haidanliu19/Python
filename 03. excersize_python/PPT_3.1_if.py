money = 1
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# if문을 만들 때는 if 조건문: 바로 아래 문장부터
#if 문에 속하는 모든 문장에 들여쓰기(indentation)를 해주어야 함
# 들여쓰기는 공백(Spacebar) 4개나 탭(Tab)을 사용하며, 2가지를 혼용하지 말 것 
money = True
if money:
    print("택시를")
else:
    print("가라")
#들여쓰기 너비가 다르기 때문에 오류가 발생함

#if 조건문에서 ‘조건문’이란 참과 거짓을 판단하는 문장을 말함

#비교연산자
#조건문에 비교연산자(<, >, ==, !=, >=, <=)를 쓰는 경우가 많음
#비교     연산자 설명
#x < y  x가 y보다 작음
#x > y  x가 y보다 큼
#x == y x와 y가 같음
#x != y x와 y가 같지 않음
#x >= y x가 y보다 크거나 같음
#x <= y x가 y보다 작거나 같음
x = 3
y = 2
print(x > y)#True
print(x < y)#False
print(x == y)#False
print(x != y)#True


#만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라.
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#x or y  x와 y 둘 중에 하나만 참이면 참임
#x and y x와 y 모두 참이어야 참임
#not x   x가 거짓이면 참임
#돈이 3000원 이상 있거나 카드가 있으면 택시를 타고 그렇지 않으면 걸어 가라.
money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# x in s, x not in s
#x in 리스트    x not in 리스트
#x in 튜플      x not in 튜플
#x in 문자열    x not in 문자열
print(1 in [1,2,3])     #True
print(1 not in [1,2,3]) #False
print('a' in ('a','b','c'))#True
print('j' not in 'python') #True

#택시 예제에 in을 적용
#만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라.
pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#125
#주머니에 카드가 없다면 걸어가로 , 있다면 버스 타라
pocket = ['paper','cellphone','money']
if 'card' in pocket:
    print("버스 타고 가라")
else:
    print("걸어 가라")

#주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라.
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

#다양한 조건을 판단하는 elif
#주머니에 돈이 있으면 택시를 타고, 주머니에 돈이 없지만
#카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라.
pocket = ['paper','cellphone']
card = True #혹은 1
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")
        
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#if문을 한 줄로 작성하기
pocket = ['paper','cellphone','money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
pocket = ['paper','cellphone','money']
if 'money' in pocket:pass
else:print("카드를 꺼내라")

#조건부 표현식
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

#조건부 표현식(conditional expression)을 사용하면 간단히 표현할 수 있음
#조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
message = "success" if score >= 60 else "failure"
print(message)
#조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우


#응용예제01. 학점 세분화 프로그램
score = int(input("점수를 입력하세요:"))
grade = ""
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    score = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f'{score}는 {grade}학점입니다.')


