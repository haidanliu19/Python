#리스트 자료형
#리스트를 어떻게 만들고 사용할까
#리스트명 = [요소1, 요소2, 요소3, ···]
odd = [1,3,5,7,9]
a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'Life','is']
e = [1,3,['Life','is']]
#리스트의 인덱싱
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0]+a[2])
print(a[-1])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])
#삼중 리스트에서 인덱싱하기
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])
#리스트의 슬라이싱
#문자열 슬라이싱
a = "12345"
print(a[0:2])
a = [1, 2, 3, 4, 5]
print(a[0:2])
b = a[:2]
c = a[2:]
print(b)
print(c)
#중첩된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

#리스트 연산하기
#1. 리스트 더하기(+)
a = [1, 2, 3] 
b = [4, 5, 6]
print(a+b)#[1, 2, 3, 4, 5, 6]
#2. 리스트 반복하기(*)
print(a*3)#[1, 2, 3, 1, 2, 3, 1, 2, 3]
#3. 리스트 길이 구하기
print(len(a))#3
#리스트 연산 오류
#a[2] + "hi" unsupported operand type(s) for +: 'int' and 'str'
#정수와 문자열은 서로 더할 수 없기 때문에 형(type) 오류가 발생함
print(str(a[2])+"hi")
#리스트의 수정과 삭제
#리스트에서 값 수정하기
a[2] = 4
print(a)#[1, 2, 4]
#del 함수를 사용해 리스트 요소 삭제하기
del a[1]
print(a)#[1, 4]
#del a == del(a)
print(a)#name 'a' is not defined
#슬라이싱 기법을 사용하여 리스트의 요소 여러 개를 삭제함 
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)
#[ ] 사용해 리스트 요소 삭제함 
a = [1, 'a', 'b', 'c', 4]
a[1:3] = []
print(a)
#리스트 관련 함수
#리스트 변수 이름 뒤에 ‘.’를 붙여서 리스트 관련 함수를 사용할 수 있음
#리스트에 요소 추가(append)
a = [1,2,3]
a.append(4)
print(a)#[1, 2, 3, 4]
a.append([5,6])
print(a)#[1, 2, 3, 4, [5, 6]]
#리스트 정렬(sort)
a = [1,2,3]
a.sort()
print(a)#[1, 2, 3]
a = ['a','c','b']
a.sort()
print(a)#['a', 'b', 'c']
#리스트 뒤집기(reverse)
a = ['a','c','b']
a.reverse()
print(a)
#내림차순으로
#1).
a = ['a','c','b']
a.sort()
a.reverse()
print(a)
#2).
a = ['a','c','b']
a.sort(reverse = True)
print(a)
#sort원자료도  정렬된다.
#위치 반환(index)
a = [1,2,3]
#index(x) 함수는 리스트에 x라는 값이 있으면 x의 위치 값을 돌려줌
#그 값의 위치이지 그 자리수의 값을 반환하는 것이 아니다.
print(a.index(3))
print(a.index(1))
#print(a.index(0))#0 is not in list
#스트에 요소 삽입(insert)
#insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수임
a = [1,2,3]
a.insert(0,4)
print(a)
#리스트에 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a) #[1, 2, 1, 2, 3]
a.remove(3)
print(a) #[1, 2, 1, 2]
#리스트 요소 끄집어 내기(pop)
a = [1,2,3]
print(a.pop())#3
print(a)#[1, 2]
# pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제함
a = [1,2,3]
print(a.pop(1))#2
print(a)#[1, 3]
#리스트에 포함된 요소 x의 개수 세기(count)
#count(x)는 리스트 내에 x개가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수 
a = [1, 2, 3, 1]
print(a.count(1))#2

#리스트 확장(extend)
a = [1, 2, 3]
a.extend([5,6])
print(a)#[1, 2, 3, 5, 6]
b = [6,7]
a.extend(b)
print(a)#[1, 2, 3, 5, 6, 6, 7]


