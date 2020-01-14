#IV. 예외 처리
#오류 예외 처리 기법 

#try, except문 
#1. try, except만 쓰는 방법
#try:
#   ···
#except:
#   ···
#오류 종류에 상관없이 오류가 발생하면 except블록을 수행함
#2. 발생 오류만 포함한 except문
#try:
#    ···
#except 발생 오류:
#    ···
#3. 발생 오류와 오류 메시지 변수까지 포함한 except문
#try:
#    ···
#except 발생 오류 as 오류 메시지 변수:
#    ···
try:
    4/0
except ZeroDivisionError as e:
    print(e)

a= [1,2,3]
try:
    a[4]
except IndexError as e:
    print(e)

#try ·· else
# else절은 예외가 발생하지 않은 경우에 실행되며
#반드시 except절 바로 다음에 위치함
try:
    f = open('foo.txt','r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()

#try ·· finally
f = open('foo.txt','w')
try:
    #무언가를 수행함
    print(1)
finally:
    f.close()


#여러 개의 오류 처리하기
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError,IndexError) as e:
    print(e)

#오류 회피하기
try:
    f = open('나 없는 파일','r')
except FileNotFoundError:
    pass


#오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError

#class Eagle(Bird):
#    pass
#eagle = Eagle()
#eagle.fly()#NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle = Eagle()
eagle.fly()#very fast

#예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick('천사')
#say_nick('바보')#raise MyError()

#오류 메시지를 사용하고 싶다면 예외 처리해 봄
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print("허용되지 않는 별명입니다.")
    #print(e)




#오류 클래스에 __str__ 메소드 구현
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)
