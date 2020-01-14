#III. 패키지
#패키지(Package)는 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로
#관리할 수 있게 해줌

#패키지 만들기
#패키지 기본 구성 요소 준비하기 
#1. C:\doit 디렉터리 밑에 game 및 서브 디렉터리를 생성하고 .py 파일들을 만듦
#C:/doit/game/__init__.py
#C:/doit/game/sound/__init__.py
#C:/doit/game/sound/echo.py
#C:/doit/game/graphic/__init__.py
#C:/doit/game/graphic/render.py
#2. 각 디렉터리에 __init__.py 파일을 만들어 놓기만 하고 내용은 일단 비워 둠
#3. echo.py 파일은 다음과 같이 만듦
# echo.py
def echo_test():
    print("echo")
# 4. render 파일을 다음과 같이 만듦
# render.py
def render_test():
    print("render")

#5. game 패키지를 참조할 수 있도록 명령
#프롬프트창에서 set 명령어로 PYTHONPATH 환경 변수에 C:\doit 디렉터리를 추가함
# C:\>set PYTHONPATH=C:\doit
# python

#패키지 안의 함수 실행하기
#첫 번째, echo 모듈을 import하여 실행하는 방법
import game.sound.echo
game.sound.echo.echo_test()

#두 번째, echo 모듈이 있는 디렉터리까지를
#from ··· import하여 실행하는 방법
from game.sound import echo
echo.echo_test()
#세 번째, echo 모듈의 echo_test 함수를 직접 import하여 실행하는 방법
from game.sound.echo import echo_test
echo_test()

#패키지 안의 함수 사용할 때 주의사항
#첫 번째, 다음과 같이 echo_test 함수를 사용하는 것은 불가능함
#import game
#game.sound.echo.echo_test()

#두 번째, import 마직막 항목에 함수를 사용하는 것도 불가능함
#import game.sound.echo.echo_test

#relative 패키지
# render.py
from game.sound.echo import echo_test

def render_test():
    print("render")
    echo_test()
#수정 후 다음과 같이 수행함
from game.graphic.render import render_test()
render_test()

# render.py
from ..sound.echo import echo_test
def render_test():
    print("render")
    echo_test()
    
#파이썬 인터프리터에서 relative한 접근자를 사용하면
#‘SystemError: cannot perform relative import’와 같은 오류가 발생함




