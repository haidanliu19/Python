#V. 내장 함수
#abs
#abs(x)는 어떤 숫자를 입력을 받았을 때, 그 숫자의 절대값을 돌려주는 함수
print(abs(3))
print(abs(-3))
print(abs(-1.2))

#all
#all(x)는 반복 가능한 자료형 x를 입력 인수로 받으며 이
#x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려줌
print(all([1,2,3]))#True
print(all([1,2,3,0]))#False

#any
#any(x)는 x중 하나라도 참이 있으면 True를 돌려주고,
#x가 모두 거짓일 때에만 False 를 돌려줌. all(x)의 반대임.
print(any([1,2,3,0]))#True
print(any([0,'']))#False

#chr
#chr(i)는 아스키 코드 값을 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수
print(chr(97))
print(chr(48))

#dir
#dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
#print(dir([1,2,3]))
#print(dir({'1':'a'}))

#divmod
#divmod(a, b)는 2개 숫자를 입력으로 받아서 a를 b로 나눈 몫과 나머지를 튜플 형태
#로 돌려주는 함수
print(divmod(7,3))#(2, 1)


#enumerate
#순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는
#enumerate 객체를 돌려주는 함수
for i, name in enumerate(['body','foo','bar']):
    print(i,name)


#eval
#eval(expression)은 실행 가능한 문자열(1+2, ‘hi’ + ‘a’ 등)을 입력으로 받아
#문자열을 실행한 결과값을 돌려주는 함수
print(eval('1+2'))
print(eval("'hi'+'a'"))
print(eval('divmod(4,3)'))

#filter
#첫 번째 인수로 함수 이름을,
#두 번째 인수로 그 함수에 차례로 들어갈 자료형을 받음 
#positive.py
def positive(l):
    result = []
    for i in l:
        if i > 0 :
            result.append(i)
    return result
print(positive([1,-3,2,0,-5,6]))
# filter 함수를 사용하면 앞의 내용을 간략하게 작성할 수 있음
def positive(x):
    return x >0
print(list(filter(positive,[1,-3,2,0,-5,6])))

print(list(filter(lambda x:x>0,[1,-3,2,0,-5,6])))

#hex
# hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수
print(hex(234))
print(hex(3))

#id
#id(object)는 객체를 입력 받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수
a = 3
print(id(a))
b = a
print(id(b))
print(id(4))

#input
# input([prompt])은 사용자 입력을 받는 함수
a = input()
print(a)
b = input("Enter:")
print(b)

#int
#int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수
print(int('3'))
print(int(3.4))#3
#int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려줌
print(int('11',2))
print(int('1A',16))

# isinstance
#isinstance(object, class)는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스를 받음
class Person:pass
a = Person()
print(isinstance(a, Person))#True
b =3
print(isinstance(b, Person))#False

#lambda
#lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 함
add = lambda a, b :a +b
result = add(3,4)
print(result)#7
#리스트 내에 lambda 함수 만들기
myList = [lambda a,b :a+b, lambda a, b : a*b]
print(myList)
print(myList[0])
print(myList[0](3,4))
print(myList[1](3,4))

#len
# len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수
print(len("python"))
print(len([1,2,3]))
print(len((1,'a')))

#list
#list(s)는 반복 가능한 자료형 s를 입력받아 리스트를 돌려주는 함
print(list("python"))
print(list((1,2,3)))
a = [1,2,3]
b = list(a)
print(b)

#map
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받음
#map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
#two_times.py
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result
result = two_times([1,2,3,4])
print(result)# [2, 4, 6, 8]

def two_times(x):return x*2
print(list(map(two_times,[1,2,3,4])))

print(list(map(lambda a : a*2,[1,2,3,4])))


#max
#max(iterable)는 인수로 반복 가능한 자료형을 입력받아 최대값을 돌려주는 함수
print(max([1,2,3]))
print(max("python"))

#min
#min(iterable)는 인수로 반복 가능한 자료형을 입력받아 최소값을 돌려주는 함수
print(min([1,2,3]))
print(min("python"))

#oct
# oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수
print(oct(34))
print(oct(12345))

#open
#b 바이너리 모드로 파일 열기
#wb , rb
#f = open("binary_fil", "rb")
fread = open("read_mode.txt", "r")
fread2 = open("read_mode.txt")

fappend = open("append_mode.txt", "a")

#ord
#ord(c)는 문자를 입력으로 받아 아스키 코드 값을 리턴하는 함수
print(ord('a'))
print(ord('0'))

#pow
#pow(x, y)는 x의 y제곱한 결과값을 리턴하는 함수
print(pow(2,4))
print(pow(3,3))


#range
# range([start,]stop[,step])는 for문과 함께 자주 사용되는 함수
#인수가 하나일 경우
print(list(range(5)))
#인수가 2개일 경우
print(list(range(5,10)))
#인수가 3개일 경우
print(list(range(1,10,2)))
print(list(range(0,-10,-1)))


#round
#round(number[,ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수
print(round(4.6))#5
print(round(4.2))#4

print(round(5.678,2))

#sorted
print(sorted([3,1,2]))
print(sorted(['a','c','b']))
print(sorted("zero"))
a = [3,1,2]
print(sorted(a))
print(a)
#sorted안 변하는 데 sort는 값이 변한다.
# sort 
#sort(iterable) 함수는 리스트 객체 그 자체를 정렬할 뿐
#정렬된 결과를 돌려주지 않음
a = [3, 1, 2]
result = a.sort()
print(result)#None
print(a)

#str
#str(object)은 문자열 형태로 객체를 반환하여 돌려주는 함수
print(str(3))
print(str('hi'))
print(str('hi'.upper()))

#sum
#sum(iterable)은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
print(sum([1,2,3]))
print(sum([4,5,6]))

#tuple
#tuple(iterable)은 반복 가능한 자료형을 입력 받아 튜플 형태로 바꾸어 돌려주는 함
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

#type
#type(object)은 입력값의 자료형이 무엇인지 알려 주는 함
print(type("abc"))
print(type([]))
print(type(open("test","w")))

#ZIP
#zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
print(list(zip([1,2,3],[4,5,6])))#[(1, 4), (2, 5), (3, 6)]
print(list(zip([1,2,3],[4,5,6],[7,8,9])))#[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip("abc","def")))#[('a', 'd'), ('b', 'e'), ('c', 'f')]

      
