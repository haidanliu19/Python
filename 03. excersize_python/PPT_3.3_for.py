#III. for문
#for문의 기본 구조
#1. 전형적인 for문
test_list = ['one','two','three']
for i in test_list:
    print(i)

#2. 다양한 for문의 사용
a = [(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)

#총 5명의 학생이 시험을 보았는데 시험 점수가
#60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
#합격인지 불합격인지 결과를 보여주시오.
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

#점수 출력 및 소수점 처리
marks = [95,25,67,45,80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 %.2f이여서 합격입니다." % (number,mark))
    else:
        print("%d번 학생은 %.2f이여서 불합격입니다." % (number,mark))


#for문과 continue
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다." % number)
    
#for와 함께 자주 사용하는 range함수
a = range(10)
print(a)#range(0, 10)0, 1, 2, 3, 4, 5, 6, 7, 8, 9
a = range(1,11)
print(a)#range(1, 11)1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# range 함수의 예시 살펴보기
add = 0
for i in range(1,11):
    add += i
print(add)

#60점 이상이면 합격’이라는 문장을 출력하는 예제를 range 함수로 구현함
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:continue
    print("%d번 학생 축하합니다. 합격입니다. " % (number + 1))

#for와 range를 사용한 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i * j , end = " ")
    print('')

for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=" ")#출력할 때 다음 줄로 넘기지 않고 그 줄에 계속 출력함 
    print(' ')

a= list(range(len(marks)))
print(a)
    
#리스트 내포 사용하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)
print(result)

result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)

#리스트 내포의 일반적인 문법
#[표현식 for 항목 in 반복 가능 객체 if 조건]
#for문을 여러 개 사용할 때의 문법
#[표현식 for 항목 in 반복 가능 객체 if 조건1
#        for 항목 in 반복 가능 객체 if 조건2 ...
#        for 항목 in 반복 가능 객체 if 조건n]
#구구단의 모든 결과를 리스트에 담고 싶다면 리스트 내포를 사용하여 구현함
result = [x*y for x in range(2,10)
              for y in range(2,10)]
print(result)
result = [x*y*z for x in range(2,10)
                for y in range(1,10)
                for z in range(1,10)]
print(result)

#1-100
#for문
for i in range(100):
    print(i+1,end=" ")
#while문
i = 0
while i < 100:
    i+=1
    print(i,end=" ")

#평균 점수 구하기
scores = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in scores:
    total += score
print(total/len(scores))


scores = [70,60,55,75,95,90,80,80,85,100]
total = 0
for i in range(len(scores)):
    total += scores[i]
print(total/len(scores))


numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n%2 != 0 :
        result.append(n*2)
print(result)


numbers = [1,2,3,4,5]
result = []
#리스트 내포
result = [num* 2 for num in numbers if num%2 != 0]
print(result)


treeHit=0
for i in range(10):
    treeHit =  i+1
    print("나무를 %d를 찍었습니다" % treeHit)
print("나무 넘어갑니다.")


a = [(1,2),(3,4),(5,6)]
for(first,last) in a:
    print(first+last)

