########20191210
R은 VECTOR자료구조가 더 작다. Python 은 VECTOR보다 더 작다.
R은 함수중심의 언어	Python 은 객체지향
8.9장은 교제에 없다. 9장은 웹 크롤링
interrupt 언어는 한 줄 단위로 해서 바로 바로 보여주는 것 번역하는데 빠르다.
컴파일러 언어는 전체 소스를 한번에 한다. EXEC 생긴다. 컴파일 하는데 늦지만 실행하는데 빠르다.
Python은 데이터를 처리하는데 좋은 소프트프로그램이다.
Python IDLE사용

# 1장. Python이란 무엇인가?
## I. Python이란?
 1990년 귀도 반 로섬(Guido Van Rossum)이 개발한 인터프리터 언어
 자신이 좋아하는 코미디쇼인 ‘몬티 Python의 날아다니는 서커스’에서 이름을 따왔음
 고대 신화에 나오는 파르나소스 산의 동굴에 살던 큰 뱀
 컴퓨터 프로그래밍 교육을 위해 많이 사용하지만, 기업의 실무를 위해서도 많이 사용하는 언어임
 구글에서 만들어진 소프트웨어의 50% 이상이 Python임
 온라인 사진 공유 서비스 인스타그램(Instagram)
 파일 동기화 서비스 드롭박스(Dropbox)
 공동 작업과 유지 보수가 매우 쉽고 편함
 국내에서도 사용자 층이 더욱 넓어지고 있음

## II. Python의 특징
 Python은 인간다운 언어임
 Python은 문법이 쉬워 빠르게 배울 수 있음
 Python은 무료이지만 강력함
	사용료 걱정 없이 언제 어디서든 Python을 다운로드하여 사용 (Open Source)

=>Python은 간결함
펄(Perl) 프로그램 언어가 100가지 방법으로 하나의 일을 처리할 수 있다면, Python은 가장 좋은 방법 1가지만 이용하는 것을 선호
 실행이 되게 하려면 꼭 줄을 맞추어야 됨
simple.py
languages = ['python','perl','c','java']

for lang in languages:
    if lang in ['python','perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c','java']:
        print("%6s need compilter" % lang)
    else:
        print("should not reach here")
결과 ======>
 
Python은 프로그래밍을 즐기게 해 줌
Python은 개발 속도가 빠름

## III. Python으로 무엇을 할 수 있을까?
=>Python으로 할 수 있는 일
 시스템 유틸리티 제작
 GUI 프로그래밍
 C/C++와의 결합
 웹 프로그래밍
 수치 연산 프로그래밍
 데이터베이스 프로그래밍
 데이터 분석, 사물 인터넷
=>Python으로 할 수 없는 일
 시스템과 밀접한 프로그래밍 영역
 모바일 프로그래밍

## IV. Python 설치하기
www.python.org
=>python shell
**주의사항
 
PATH default로 찾는 위치
=>notepad를 실행하려면 원래는 경로까지 가서 클릭해야 하는데 명령어로 사용하면 직접 열리게끔 하는 것이다.
=>환경변수에 추가된다.
pip 명령어를 어디에서나 사용하게 하기 위해서 설정한다.

pip명령이 오류가 발생하는 경우:
=>pip command가 없다고 나오는 경우
python이 설치되지 않았거나 python명령어   디렉토리가 path에 추가되지 않은 경우 입니다.

=>windows의 경우에는 VC++로 패키지를 만드는 경우가 있는데 이러한 패키지들은 vc++ 재배포 패키지를 설치해야만 설치되는 패키지들이 있습니다.
pip처음 사용시 pip를 업데이트 하라고 한다.
	python –m pip install –upgrade pip

[Ctrl + Z → Enter눌리면 나간다.
명령어
프로그램을 종료 시
sys.exit()

V. Python 둘러보기
=>Python 기초 실습 준비하기
 [시작] 메뉴에서 [모든 프로그램 → Python 3.8 → Python 3.8(64-bit)] 선택  
아래의 화면을 대화형 인터프리터라고 함(Python shell)
 
=>Python 종료:
Python을 종료하려면 [Ctrl + Z → Enter] 또는 아래의 화면과 같이 sys 모듈을 사용하 여 종료할 수 있음

=>Python 기초 문법 따라 해보기
==>사칙연산 – 더하기
 >>> 1 + 2

결과값 =>  

==>사칙연산 - 나눗셈과 곱셈
 >>> 3 / 2.4
 >>> 3 * 9

결과값 => 

==>변수에 숫자 대입하고 계산하기
>>> a = 1
>>> b = 2
>>> a + b

결과값 => 

==>변수에 문자 대입하고 출력하기
>>> a = "Python"
>>> print(a)

결과값 => 

==>조건문 if  
아래의 예제는 a가 1보다 크면 ‘a is greater than 1’이라는 문장 출력
‘…’는 아직 문장이 끝나지 않았음을 의미
>>> a = 3
>>> if a > 1:
>>>     print("a is greater than 1")


결과값 => 

==>반복문 for
아래의 예제는 for문을 이용하여 [1, 2, 3] 안의 값들을 하나씩 출력
>>> for a in [1,2,3]:
>>> 	print(a)



결과값 => 

==>반복문 while
아래의 예제는 i 값이 3보다 작은 동안 i = i +1과 print(i)를 수행
>>> i = 0
>>> while i < 3:
>>>     i += 1
>>>     print(i)




결과값 => 

==>함수  
def는 함수를 만들 때 사용하는 예약어임  
아래의 예제는 sum(a, b)에서 a, b는 입력값이고, a + b는 결과 값임  
즉 3, 4가 입력으로 들어오면 3+4를 수행하고 결과값 7을 돌려
>>> def sum(a,b):
>>>     return a + b
>>>
>>> print(sum(3,4))





결과값 => 

메모리의 위치는 변수가 알려준다.
변수를 저장하면 메모리에 데이터 쌓이고 가공하는 것이다.
... 은 더 입력하다 라는 것이다.

VI. Python과 에디터
=>Python IDLE(Intergrated Development and Learning Environment)
파이참(PyCharm)
비주얼 스튜디오 코드

IDLE로 Python 프로그램 작성하기
IDLE(Intergrated Development and Learning Environment)
[시작 → 모든 프로그램 → Python 3.8 → IDLE]을 선택해 Python IDLE을 실행함

=>[IDLE 에디터] Python 프로그램 작성하기
 '#은 주석으로 그 줄 끝까지 프로그램 수행에 전혀 영향을 주지 않음
 
IDLE은 두 가지 창으로 구성됨  
IDLE 셸 창(Shell Window): IDLE 에디터에서 실행한 프로그램의 결과가 표시되 는 창으로 Python 셸과 동일한 기능을 수행함.  
IDLE 에디터 창(Editor Window): IDLE 에디터가 실행되는 창

=>IDLE 셸 창 메뉴에서 [FILE → New File]을 선택해 실행함
IDLE 에디터 창 메뉴에서 [Run → Run Module]을 선택함(단축키:F5)
파일을 저장하면 자동으로 Python 프로그램이 실행됨

python idle은 오류에 민감하다.
python idle은 두 번째 줄부터 뛰어 쓰기가 두 번씩 확 가버린다.그래서 코딩하기 불편하다.
그래서 간단한 것은 python한 것은 python shell에서 하고 
idle edit에서 작성하고 저장 한 다음 idle shell에서 결과 확인

명령 프롬프트 창에서 Python 프로그램 실행하기
[윈도우 키 + R]을 누르고, 빈 칸에 ‘cmd’를 입력하고 [확인]을 선택함
 
Python 프로그램 실행하기
 

여러 줄 주석
“””
‘’’
