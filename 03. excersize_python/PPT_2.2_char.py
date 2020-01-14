#II. 문자열 자료형
#문자열 자료형 만드는 4가지 방법
#1. 큰따옴표(“)로 양쪽 둘러싸기
#2. 작은따옴표(‘)로 양쪽 둘러싸기
#3. 큰따옴표 3개를 연속(“””)으로 써서 양쪽 둘러싸기
#4. 작은따옴표 3개를 연속(‘’’)으로 써서 양쪽 둘러싸기

#문자열에 따옴표 포함시키기
#구문 오류(Syntax Error)->",' 기호를 적절하게 사용해야 한다.
#1. 문자열에 작은따옴표(‘) 포함시키기
#2. 문자열에 큰따옴표(“) 포함시키기 
#3. 백슬래시(\)를 이용해서 작은따옴표(‘)와 큰따옴표(“)를 문자열에 포함시키기
#백슬래시(\)를 작은따옴표(‘)나 큰따옴표(“) 앞에
#삽입하면 백슬래시(\) 뒤의 작은따옴표(‘)나 큰따옴표(“)는
#문자열을 둘러싸는 기호의 의미가 아니라 (‘), (“) 그 자체를 의미함
food = 'Python\'s favorite food is perl' 
say = "\"Python is very easy.\" he says."
#여러 줄인 문자열을 변수에 대입하고 싶을 때
#[이스케이프 코드]
multiline = "Life is too short\nYou need python"
print(multiline)
#프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 ‘문자 조합‘이며, 출력물을 보기 좋게 정렬해 줌
#   \n 문자열 안에서 줄을 바꿀 때 사용
#   \t 문자열 사이에 탭 간격을 줄 때 사용
#   \\ 문자 \를 그대로 표현할 때 사용
#   \’ 작은따옴표(‘)를 그대로 표현할 때 사용
#   \” 큰따옴표(“)를 그대로 표현할 때 사용
#1. 줄을 바꾸는 이스케이프 코드 ‘\n’ 삽입하기
#2. 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 이용
#문자열 연산하기 
#1. 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head + tail)
#2. 문자열 곱하기
a = "python"
print(a*2)#pythonpython
#3. 문자열 곱하기 응용
#4. 문자열 길이 구하기
a = "Life is too short"
print(len(a))
#문자열 인덱싱과 슬라이싱
#인덱싱(Indexing)이란 무엇인가를 가리킨다는 의미이고
#슬라이싱(Slicing)은 무엇인가를 잘라낸다는 의미임

#문자열 인덱싱
#파이썬은 0부터 숫자를 셈
a = "Life is too short, You need Python"
print(a[0])
print(a[-0])
#a[0]과 a[-0]은 같다.
print(a[12])
print(a[-1])
print(a[-2])
print(a[-5])


#문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

# a[시작 번호:끝 번호]
print(a[0:4]) #0 <= a < 4
print(a[0:5])
print(a[0:2])
print(a[5:7])
print(a[12:17])
print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])

#슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
year = a[:4]
day = a[4:8]
print(year)
print(day)

#문자열 바꾸기
#ption->python
a = "Pithon"
print(a[1])
#a[1] = 'y'->오류가 난다.문자열의 요솟값은 바꿀 수 없는 값이기 때문입니다.
#'str' object does not support item assignment
print(a)
a = 'Pithon'
print(a[:1])
print(a[2:])
a = a[:1] + 'y' +a[2:]
print(a)

#문자열 포밋팅
#문자열 포매팅 따라하기
#1. 숫자 바로 대입
print("I eat %d apples." % 3)
#2. 문자열 바로 대입
print("I eat %s apples." % "five")
#3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)
#4. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number,day))
#문자열 포맷 코드
#   %s 문자열(String)
#   %c 문자 1개(Character)
#   %d 정수(Integer)
#   %f 부동 소수(Floating-point)
#   %o 8진수
#   %x 16진수
#   %% Literal %(문자 ‘%’ 자체)
print("I have %s apples" % 3)
print("rate is %s" % 3.234)
#포맷팅 연산자 %d와 %를 같이 쓸 때는 %%를 씀
#print("Error is %d%." %98)오류
print("Error is %d%%." % 98)
#Error is 98%.

#포맷 코드와 숫자 함께 사용하기
#1. 정렬과 공백
print("%10s" % "hi" )#글이 오른쪽
print("%-10sjane" % "hi" )#'hi        jane'
#2. 소수점 표현하기
print("%0.4f" % 3.42134234)#3.4213
print("%10.4f" % 3.42134234)#    3.4213

#format 함수를 사용한 포매팅
#숫자 바로 대입하기
print("I eat {0} apples".format(3))#I eat 3 apples
#문자열 바로 대입하기
print("I eat {0} apples".format("five"))
#숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples".format(number))
#2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples.so I was sick for {1} days.".format(number,day))
#이름으로 넣기
print("I ate {number} apples.so I was sick for {day} days.".format(number= 10,day = 3))
#인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples.so I was sick for {day} days.".format(10,day = 3))
#왼쪽 정렬
print("{0:<10}".format("hi"))
#오른쪽 정렬
print("{0:>10}".format("hi"))
#가운데 정렬
print("{0:^10}".format("hi"))
#공백 채우기
print("0:=^10".format("hi"))
print("0:!<10".format("hi"))
#소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{{ and }}".format())
#f 문자열 포매팅->파이썬 3.6버전 부터
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다.나이는 {age}입니다.')
#표현식 지원
age = 30
print(f'나는 내년이면 {age+1}입니다.')
#print(f'나는 내년이면 {age}+1입니다.')#나는 내년이면 30+1입니다.
#딕셔너리 사용
d = {'name':'홍길동','age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
#정렬
print(f'{"hi":<10}')#왼쪽 정렬
print(f'{"hi":>10}')
print(f'{"hi":^10}')
#공백 채우기
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')
#소수점 표현하기
y = 3.42134234
print(f'{y:0.4f})')
print(f'{y:10.4f}')
#{ 또는 } 문자 표현하기
print(f'{{ and }}')

#문자열 관련 함수
#문자 개수 세기(count)
a = "hobby"
print(a.count('b'))
#위치 알려주기 1(find)
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k')) #없으면 -1
#위치 알려주기 2(index)
a = "Life is too short"
print(a.index('t'))
#print(a.index('k'))#ValueError: substring not found
#문자열 삽입(join)
a = ","
print(a.join('abcd'))#a,b,c,d
print(a.join(['a','b','c','d']))#a,b,c,d
#소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())
#대문자를 소문자로 바꾸기(lower)
print(a.lower())
#왼쪽 공백 지우기(lstrip)
a = "  hi  " 
print(a.lstrip())
#오른쪽 공백 지우기(rstrip)
print(a.rstrip())
#양쪽 공백 지우기(strip)
print(a.strip())
#문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life","Your leg"))
#문자열 나누기(split)
a = "Life is too short"
print(a.split())
a = "a:b:c:d"
print(a.split(":"))
#공백(스페이스,탭,엔트)등


