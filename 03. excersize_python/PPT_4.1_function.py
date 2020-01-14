#I. 함수
#함수(function)는 입력 값을 가지고 어떤 일을 수행한 다음에 그 결과물을 내어놓은 것
#함수를 사용하는 이유는 무엇일까? 
#동일한 내용을 반복해서 작성할 때 한 번만 코딩해 두고 반복해서 사용 
#프로그램을 함수화하면 프로그램의 흐름을 일목요연하게 볼 수 있음
#함수의 구조
#def 함수이름(매개변수):
#    <수행할 문장1> <수행할 문장2>
#    ...
#    return 결과값
def add(a,b):
    return a + b
a = 3
b = 4
c = add(a,b)
print(c)

#매개변수와 인수 
def add(a,b): 
    return a+b

print(add(3,4))
#입력값과 결과값에 따른 함수의 형태 
#1. 일반적인 함수
#def 함수이름(매개변수):
#    수행할 문장 ...
#    return 결과값
#일반적인 함수의 예
def add(a,b):
    result = a+b
    return result
a = add(3,4)
print(a)
#결과값을 받을 변수 = 함수이름(입력인수 1, 입력인수 2, ···)


#2.입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)
#결과값을 받을 변수 = 함수명()

#3. 결과값이 없는 함수
def add(a,b):
    print("%d , %d 의 합은 %d입니다." % (a,b, a + b))
add(3,4)
#함수이름(입력인수1, 입력인수2, ···)
#결과값이 없는지 확인하기 위한 예
a = add(3,4)
print(a) #None

#4. 입력값도 결과값도 없는 함수
def say():
    print("Hi")
say()
#함수명()

#매개변수 지정하여 호출하기
def add(a,b):
    return a + b
#함수를 호출할 때 매개변수를 지정할 수 있음
result = add(a = 3, b = 7)
print(result)
#매개변수를 지정하면 순서에 상관없이 사용할 수 있다는 장점이 있음
result = add(b = 3, a = 7)
print(result)

#입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
#def 함수이름(*매개변수)
#    수행할 문장
#1. 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result
result = add_many(1,2,3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
#2. 다양한 종류의 매개변수를 받는 함수 만들기
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result
result = add_mul('add',1,2,3,4,5)
print(result)
result = add_mul('mul',1,2,3,4,5)
print(result)


#키워드 파라미터
#키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(**)를 붙임
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a = 1)#{'a': 1}
print_kwargs(name = 'foo', age = 3)#{'name': 'foo', 'age': 3}

#함수의 결과값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b , a* b
result = add_and_mul(3,4)
print(result)#(7, 12)

#하나의 튜플 값을 2개의 결과값처럼 받고 싶다면 다음과 같이 함수를 호출하면 됨
result1,result2 = add_and_mul(3,4)

#아래와 같이 return문을 2번 사용하면, 2개의 결과값을 돌려주지 않을까?
#두 번째 return문인 return a*b는 실행되지 않음
#함수는 return문을 만나는 순간 결과값을 돌려준 다음 함수를 빠져나가게 됨
def add_and_mul(a,b):
    return a+b
    return a*b
result = add_and_mul(2,3)
print(result)#5


#return의 또 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)
say_nick('야호')
say_nick('바보')

#매개변수에 초기값 미리 설정하기
def say_myself(name,old, man = True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

# 매개변수에 초기값 설정하는 사용 예
say_myself("박응용",27)
say_myself("박응용",27,True)

say_myself("박응용", 27, False)

#함수의 매개변수에 초기값 설정할 때 주의사항
#def say_myself(name, man = True,old):
#Syntax Error: non-default argument follows default argument
#    print("나의 이름은 %s 입니다." % name)
#    print("나이는 %d살입니다." % old)
#    if man:
#        print("남자입니다.")
#    else:
#        print("여자입니다.")


#say_myself1("박응용",27)
#Syntax Error: non-default argument follows default argument

#함수 안에서 선언한 변수의 효력 범위
#vartest.py
#함수 안에서 사용할 변수의 이름을 함수 밖에서도 동일하게 사용한다면 어떻게 될까?
a = 1    #함수 밖의 변수 a
def vartest(a):     #vartest 함수 선언
    a += 1
vartest(a) #vartest 함수의 입력값으로 a를 줌 
print(a)   # a의 값 출력 1

#vartest_error.py
#del a
#def vartest(a):
#    a += 1
#vartest(3)
#print(a)# error

#함수 안에서 함수 밖의 변수를 변경하는 방법
#1. return 사용하기
#vartest_return.py 
a = 1
def vartest(a):
    a += 1
    return a
a = vartest(a)
print(a)#2

#2. global 명령어 이용하기
#vartest_global.py
a = 1
def vartest():
    global a
    a += 1
vartest()
print(a)#2

#lambda
#lambda 매개변수1, 매개변수2, … : 매개변수를 사용한 표현식
# lambda(람다)는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 함
add = lambda a,b : a+b
result = add(3,4)
print(result)

mul = lambda a,b:a*b
result = mul(3,4)
print(result)

sub = lambda a,b:a-b
result = sub(3,4)
print(result)

div = lambda a,b:a/b
result = div(3,4)
print(result)

#응용예제01. 커피 자판기 프로그램
#coffee01.py
coffee = 0
coffee = int(input("어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노)"))
print()
print("#1. 뜨거운 물을 준비한다.")
print("#2. 종이컵을 준비한다.")
if coffee ==1: print("#3. 아메리카노를 탄다.")
elif coffee == 2: print("#3. 카페라떼를 탄다.")
elif coffee == 3: print("#3. 카푸치노를 탄다.")
else: print("#3. 아무거나 탄다.")
print("#4. 물을 붓는다.")
print("#5. 스푼으로 젓는다.")
print()
print("손님~커피 여기 있습니다.")



