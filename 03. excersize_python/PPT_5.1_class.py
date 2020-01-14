#5장. 파이썬 날개 달기, 객체지향 프로그래밍
#I. 클래스
#클래스(class)는 객체 지향 프로그래밍(OOP)에서 특정 객체를 생성하기 위해
#변수와 메소드 (함수)를 정의하는 일종의 틀(template)이다.
#클래스는 도대체 왜 필요한가?
#함수를 이용해 계산기의 ‘더하기‘ 기능을 구현한 예
#add1.py
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))#3
print(add(4))#7

#계산기 2대 있을 경우 함수 사용 방식
#add2.py 
result1 = 0
result2 = 0
#계산기 1
def add1(num):
    global result1
    result1 += num
    return result1
#계산기 2
def add2(num):
    global result2
    result2 += num
    return result2
print(add1(3))#3
print(add1(4))#7
print(add2(3))#3
print(add2(7))#10

#클래스를 이용
#add3.py
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self,num):
        self.result += num
        return self.result
    def sub(self,num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#Calculator 클래스에 빼기 기능 함수를 추가한 예
def sub(self,num):
    self.result -= num
    return self.result

#클래스와 객체
class Cookie:
    pass
#앞에서 만든 Cookie 클래스의 객체를 만드는 방법
a = Cookie()
b = Cookie()
#[객체와 인스턴스의 차이] 
#클래스로 만든 객체를 인스턴스라고도 함 
#a = Cookie() 이렇게 만든 a는 객체임 
#a 객체는 Cookie의 인스턴스임 
#즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계
#    위주로 설명할 때 사용됨 
#a는 ‘인스턴스’ 보다는 a는 ‘객체’라는 표현이 어울림 
#a는 ‘Cookie의 객체’보다는 a는 ‘Cookie의 인스턴스’라는 표현이 어울림
#사칙연산 클래스 만들기
#클래스 안에 함수는 메소드(Method)라고 부름
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal(4,2)
b = FourCal(3,8)
#a = FourCal()
#b = FourCal()
#a.setdata(4,2)
#b.setdata(3,8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

#생성자(Constructor)
#위에서 만든 FourCal 클래스를 다음과 같이 실행하면 어떻게 될까?
a = FourCal(4, 2) #__init__부분 사용

#상속(Inheritance)이란 ‘물려받다’라는 뜻으로,
#어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것임
#class 클래스 이름(상속할 클래스 이름)
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
#[왜 상속을 해야 할까?]  
#상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경 하려고 할 때 사용한다.  
#기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이 라면 상속을 사용해야 한다.


#매소드 오버라이딩(Overriding)
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second
a = SafeFourCal(4,0)
print(a.div())

#클래스 변수
#클래스 변수 선언
class Family:
    lastname = "김"
print(Family.lastname)
a = Family()
b = Family()
print(a.lastname)#김
print(b.lastname)#김
Family.lastname = "박"
print(a.lastname)#박
print(b.lastname)#박  
#두개 아이디가 같다.
