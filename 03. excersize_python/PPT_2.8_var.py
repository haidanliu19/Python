#VIII. 자료형의 값을 저장하는 공간, 변수
#변수를 만들 때는 =(assignment) 기호를 사용
#변수명 = 변수에 저장할 값
#변수란?
#파이썬에서 사용하는 변수는 객체를 가리키는 것
a = [1,2,3]
print(id(a))# id() 함수는 변수가 가리키고 있는 객체의 주소 값을 돌려줌
#변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소를 가리키게

#리스트를 복사할 때
a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(a is b)#True
a[1] = 4
print(a)#[1, 4, 3]
print(b)#[1, 4, 3]

# b 변수를 생성할 때 a 변수의 값을 가져오면서 다른 주소를 가리키도록 만드는 방법
#1. [:] 이용
# a 리스트 값을 바꾸더라도 b 리스트에는 영향을 끼치지 않음
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)#[1, 4, 3]
print(b)#[1, 2, 3]

#2. copy 모듈 이용
from copy import copy
a = [1,2,3]
b = copy(a)
print(a)
print(b)
print(b is a)#False

#변수를 만드는 여러 가지 방법

#튜플로 a, b에 값을 대입할 수 있음
a,b = ('python','life')
print(a)#python

#튜플은 괄호를 생략해도 됨
(a,b) = 'python','life'
print(a)#python

#리스트로 변수를 만들 수 있음
[a,b] = ['python','life']
print(a)#python

#여러 개의 변수에 같은 값을 대입할 수 있음
a = b = 'python'
print(a)#python


a = 3
b = 5
a,b = b,a
print(a)#5
print(b)#3


#메모리에 생성된 변수 없애기
a = 3
b = 5
del(a)
del(b)


