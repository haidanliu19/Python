#112페이지 연습문제
#1.평균점수
a = 80 #국어
b = 75 #영어
c = 55 #수학
print((a+b+c)/3)

#2.13이 홀수 인지 짝수
a = 13
if a%2 ==0:
    print("짝수")
else:
    print("홀수")

#3.
pin = "881120-1068234"
yyyymmdd =pin[:6]
num =pin[7:]
print(yyyymmdd)#연월일 부분 출력
print(num)#숫자 부분 출력

#4.
pin = "881120-1068234"
print(pin[7])

#5.
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

#6.
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7.
a = ['Life','is','too','short']
a = " ".join(a)
print(a)

#8.
a = (1,2,3)
a = a + (4,)
print(a)

#9.
a = dict()
a['name'] = 'python'
print(a)
a[('a',)] = 'python'
print(a)
#a[[1]] = 'python'
#print(a)#unhashable type: 'list'
a[250] = 'python'
print(a)

#10.
a = {'A':90,'B':80,'C':70}
result = a.pop("B")
print(a)
print(result)


#11.
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

#12.
a = b = [1,2,3]
a[1] = 4
print(b)
print(a is b)
