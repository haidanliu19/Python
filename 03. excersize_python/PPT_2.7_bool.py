#VII. 불 자료형
#불(bool) 자료형이란? 
#참(True)과 거짓(False)을 나타내는 자료형
a = True
b = False
print(type(a))#<class 'bool'>
print(type(b))#<class 'bool'>

print(1 == 1)
print(2 > 1)
print(2 < 1)

#문자열 "python" 참   "" 거짓
#리스트[1, 2, 3] 참 [] 거짓
#튜플 () 거짓
#딕셔너리 {} 거짓
#숫자형 0이 아닌 숫자 참 0 거짓
#None 거짓
#문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면(““, [], (), {}) 거짓이 됨
#당연히 비어 있지 않으면 참이 됨
#숫자는 그 값이 0일 때 거짓이 됨

#참과 거짓이 프로그램에서 쓰이는 사례
a = [1,2,3,4]
while a:
    print(a.pop())


if []:
    print("True")
else:
    print("False")
#False


if [1,2,3]:
    print("True")
else:
    print("False")
#True

#불(bool) 연산
print(bool('python'))#True
print(bool(''))#False
print(bool([1,2,3]))
print(bool([]))#False
print(bool(0))#False
print(bool(3))
