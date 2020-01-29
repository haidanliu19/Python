===========20191219
# 웹 크롤링 - 데이터 수집
=>과목 소개
쉽게 배워 제대로 활용하기!
1. 단순 반복을 줄여주고 빠르게 처리하는 웹 크롤링!
웹 크롤링은 단순 반복을 줄여주고 빠르게 처리할 수 있으며, 일의 효율을 높여주고 인간이 좀 더 창의적인 활동에 집중할 수 있도록 도와주는 좋은 도구이다.
2. 초보자도 해볼 수 있는 수준!
꼭 알아야 할 핵심 개념은 기본 예제로 최대한 쉽게 설명하여 처음 배우는 분들도 쉽게 해볼 수 있는 수준이다.
3. 실습 환경
 파이썬 문법으로 작성한 소스코드를 실행하는 파이썬3
 파이썬을 개발하는 도구인 파이참
 크롤러를 만들 때 크롬에 있는 개발자 도구를 활용하기 위한 크롬(Chrome)
1장. 웹 기초
1절. HTTP
2절. URL
3절. HTML
2장. 크롤러 만들기
1절. 개발환경 설치하기
2절. urllib 패키지
3절. 뷰티풀솝 사용 방법
4절. 네이버에서 특정 데이터 가져오기
5절. 네이버 메뉴 이름 뽑아내기
6절. 네이버 뉴스 제목 가져오기
1. HTTP
HTTP는 Hyper Text Transfer Protocol의 약자
• ‘하이퍼 텍스트’는 마우스로 클릭하면 다른 페이지로 이동하는 기능을 말함.
• HTTP는 HTML로 작성되어 있는 하이퍼 텍스트를 전송하기 위한 프로토콜임.
프로토콜은 ‘약속, 규칙, 규약‘이라는 뜻
• A라는 지점에서 B라는 지점으로 데이터를 보낼 때 어떻게 보낼 것인지에 대한 규칙임.
• 인터넷 주소를 쓸 때 앞에 http://www.google.com 처럼 http를 붙임.

2. URL
URL(Uniform Resource Locator)은 인터넷 주소
• 보통 웹 브라우저에서 주소 표시줄에 나오는 주소를 의미함.
• 정확히는 네트워크상에서 자원의 위치를 알려주는 주소임.
• URL이 https://www.naver.com일 때, https 라는 규약(프로토콜)으로 www.naver.com라는 주소의 실제 위치에 접속해서 정보를 가져오겠다는 의미임.
 
3. HTML
=>HTML은 Hyper Text Markup Language의 약자
• 마크업 언어라는 것은 일종의 문법임.
• 우리가 검색하고 방문하는 웹 페이지들은 웹 페이지를 작성하기 위한 어떤 문법에 의해서 작성되는 데 , HTML도 문법들 중 한 종류임.
 

크롤링 ->인터넷에서 데이터 들고오는 것 
크롤러 ->데이터를 들고와서 개발 하는 것 
파싱 ->그중에서 내가 원하는 단어 문장 등을 가져오는 것

소스코드를 이미지등 예쁘게 하는 것은 rendering 이라고 한다.
참조한  inteprete가 없을 경우 결과가 안나온다.

=>웹 페이지 소스코드
• HTML 역시 웹 프로그램을 만들기 위한 프로그래밍 언어임.
• 글씨, 이미지, 웹 페이지에서 연결하려는 특정 주소 등 다양한 정보를 담으며 태그(tag) 와 함께 사용됨.
• 태크는 <head> <link> <html> 등과 같이 사용하는 일종의 약속된 키워드임.
 

1. 개발환경 설치하기
파이참 설치하기
파이썬을 개발하는 도구로 편한 ‘라이브러리 설치‘ 기능과 코딩 소스코드를 매끄럽게 작성할 수 있게 도와주는 ‘자동 완성 기능‘ 등이 있음.
파이참 홈페이지(www.jetbrains.com/pycharm)에서 Download를 클릭함
 
Community의 Download를 클릭하여 다운로드함
 
Next 버튼 클릭하여 설치 파일 설치하기
 
Next 버튼 클릭하여 파이참 설치 경로 지정하기
 
‘64-Bit launcher’와 ‘.py‘ 옵션 설정 후 Next 버튼 클릭
 
파이참을 시작 메뉴에 추가하기 위해 Install 버튼 클릭
 
Finish 버튼 클릭하여 설치완료
 

=>프로젝트 만들기
Create New Project을 클릭함
 

=>프로젝트가 생성될 위치 지정하고, Create 버튼 클릭
‘C:\crawl’ 에 프로젝트를 만듦
경로를 바꿀 수 있음
 
=>‘Close’ 버튼 클릭
 

=> “hello” 출력하는 프로그램 작성하기
Project  crawl  New  Python File 클릭 후, 프로그램명(hello) 입력
 

=>소스코드 작성하기
print("hello")
 

=>파이썬 프로그램 실행하기
상단의 메뉴에서 [Run  Run…]을 눌러서 실행할 수 있음
 

=>패키지 추가하기
메뉴 File -> Settings -> Project Interpreter 클릭
 

=>인터프리터에서 라이브러리 추가하기
우측의 + 버튼을 누름
 

=>라이브러리 검색하여 설치하기
라이브러리 선택 후 Install Package 누름
 

=>크롬(Chrome) 설치하기
크롬에 있는 개발자 도구가 크롤러를 만들 때 필요한 도구임.
 설치 페이지로 이동하기
• www.google.com/chrome
 

=>크롬 다운로드하기
웹 페이지의 다운로드 버튼을 누르고, <NEXT> 버튼을 누르면 설치됨.
 

2. urllib 패키지
urllib는 파이썬에서 인터넷 상의 데이터를 받아 오는 기능들이 들어 있는 패키지임. urllib에 인터넷 주소(URL)를 넣고 실행하면 데이터를 텍스트 형태로 받아옴. 데이터를 받아오는 것을 ‘크롤링’이라고 함. urllib는 크롤링을 하는 라이브러리임.
=>urllib 설치하기
urllib는 기본적으로 내장되어 있기 때문에 파이썬이 설치되어 있다면 임포트(import)할 수 있음.
기본으로 제공하는 urllib 패키지 이외에 urllib5 등 다른 버전을 사용하고자하는 경우에는 Project Interpreter에서 package를 검색하여 설치함
[파이참] 메뉴에서 [File → settings→ Project Interpreter] 패키지 검색하여 설치

=>네이버 첫 페이지 받아오기
크롬을 켜고 주소창에 www.naver.com을 입력해서 네이버로 들어감.
 

네이버 접속하고 마우스 오른쪽 버튼을 클릭해서 ‘페이지 소스보기‘를 선택
 

=>네이버 첫 페이지의 소스코드로 HTML 형식으로 되어 있음.
 
웹 브라우저는 텍스트 형태로 되어 있는 HTML 문서를 읽어서 우리가 보기 좋게 그려 주는 렌더링(rendering) 기능을 하는 프로그램임.
크롤링을 한다는 것은 이 텍스트 형태의 데이터를 받아오는 것을 말하며, 받아온 데이터에서 내가 필요한 것을 뽑아내는 것을 ‘파싱’이라고 함.
요즘에는 크롤링, 파싱, 스크래핑이 ‘인터넷에서 무언가 데이터를 받아서 필요한 정보만 뽑아 내는 것’이라는 뜻으로 같이 사용됨.

=>네이버 크롤링하기
파이참 실행하여 네이버 첫 페이지의 데이터를 크롤링하기
'# url_open.py
from urllib.request import urlopen
url = "https://www.naver.com"
html = urlopen(url)
print(html.read())
'#첫페이지 크로링 결과
'#bs4 를 이용해 파싱해야 한다.
결과:
 
이 텍스트를 웹 브라우저에서 해석해서 초록색으로 배치가 잘 된 화면을 보임.
웹은 HTML 형태로 되어 있어서 이 HTML 텍스트를 받아온 다음에 여기에서 우리가 필요한 정보들을 파싱할 수 있음.
'#bs4 를 이용해 파싱해야 한다.

=> 크롤링의 과정
==>페이지를 불러온다.
urllib.request를 써서 불러온다.
urlopen(url)을 쓴다.
==> 파싱을 한다.
bs4.BeautifulSoup으로 파싱한다.
개발자 도구를 켜서 원하는 데이터가 있는 위치를 찾는다.

3. 뷰피풀솝 사용 방법
=>BeautifulSoup(뷰티풀솝)
뷰티풀솝은 데이터를 추출하는 데 필요한 기능이 들어 있는 라이브러리이며,파싱 라이브러리라고도 함.
• 모래(반도체원료, 규소) = html(BeautifulSoup)
뷰티풀솝은 텍스트를 단계별로 접근을 할 수 있게 데이터를 구조화 시켜줌.
HTML 소스코드(문서)는 웹 브라우저가 화면을 그리기 위한 내용들이 많이 들어가 있지만, 이 중에서 우리가 필요한 단어나 내용은 아주 조금이므로 파싱은 html 소스코드에서 필요한 내용만 뽑아내는 것임.
=>library(라이브러리)
많이 사용하는 기능들을 다른 사람 또는 회사가 만들어서 올려놓은 것
라이브러리는 import를 해서 사용함
내장 라이브러리와 외장 라이브러리가 있음
내장 라이브러리는 import해서 사용하고, 외장 라이브러리는 설치한 후

=>뷰티풀솝 설치하기
BeautifulSoup(뷰티풀솝)은 외장 라이브러리 이므로 따로 설치를 해야 함.
[파이참] 메뉴에서 [File → settings → Project Interpreter → bs4] 패키지 검색하여 설치

=>뷰티풀솝 사용 방법
임포트한 후에 HTML형식의 문자열(string)을 BeautifulSoup()에 넣어주고 find()를 이용해 필요한 부분만 뽑아낼 수 있음.
import해서 사용함
'# beautiful_soup.py
import bs4
'#BeautifulSoup(뷰티풀솝)
'#뷰티풀솝은 데이터를 추출하는 데 필요한 기능이 들어 있는 라이브러리이며, 파싱 라이브러리라고도 함.
html_str = '<html><div>hello</div><div class ="ddd">hello1</div></html>'
'#hello만 뽑아 올것이다.
'#BeautifulSoup 예쁘게 나오기 위해서
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
'#html_str소스 코드를 html.parser로 파싱하겠다.

print(type(bs_obj))
print(bs_obj)
print(bs_obj.find('div'))#FIND 테그에 있는 것 보여주기
print(bs_obj.find('div').text)#DIV에 있는  TEXT를 원해
결과:
 

=>HTML 다운 예제로 .find() 기능 사용
'# bs4_2.py
import bs4
html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul")
print(ul)
결과:
 


=>여기에서 ‘hello’만 뽑아내려면 ul에서 li를 한 번 더 찾아주면 됨.
'# fild_li.py
import bs4
html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul")#ul 이라는 태그를 뽑아 냄
li = ul.find("li")#ul에서 li 이라는 태그를 찾아 줌.
print(li) #.find()는 만나는 첫 번째 태그를 리턴해 주는 함수
결과:
 

=><li></li>태그 안에 있는 ‘hello’만 뽑아내려면 .text 속성을 사용함.
'# find_li_text.py
import bs4
html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul")
li = ul.find("li")
print(li.text)#hello
결과:
 

=>findAll() 사용하기
.fildAll()은 조건에 해당하는 모든 요소를 리스트 [ ] 형태로 추출해주는 기능임.
'# find_all.py
import bs4
html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul")
li = ul.findAll("li")
print(li)
'#[<li>hello</li>, <li>by</li>, <li>welcome</li>]
결과:
 

=> 인덱스로 데이터 접근하기
인덱스(index)로 리스트 안에 있는 데이터에 접근할 수 있으며, 인덱스는 0부터 시작함.
'# find_all_index.py
import bs4
html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul")
li = ul.findAll("li")
print(li[1])
결과:
 

=>맨 마지막 줄을 print(list[1].text)로 바꾸면 ‘bye‘만 출력됨
'# find_all_index_text.py
import bs4
html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul")
li = ul.findAll("li")
print(li[1].text) # 두 번째 li 태그 안에 들어 있는 텍스트를 뽑아서 출력함
'#bye

for i in li:
    print(i.text)

for i in range(len(li)):
    print(li[i].text)
결과:
 

=>태그와 속성 그리고 속성값
HTML은 <html>로 시작해서 </html>로 끝나는 문서이며, HTML은 태그(tag)와 속성(property)으로 구성되어 있음.
태그란 html 문서를 표현 할 때 쓰는 화면 구성을 하는 표시들로 문서에 있는 특정 부분에 꼬리표를 붙여준다는 뜻으로 tag라고 씀.
• <html>, <div>, <ul>, <li>, <a>, <span> 등 있음.
<ul class=“greet”>
• 속성(property) : class
• 속성값 : “greet”
<a href=“https://www.google.com/”>
• 속성(property) : href
• 속성값 : “https://www.google.com/”

=>데이터 뽑을 때 class 속성 이용하기
HTML코드에 ul이 두 개 있는 경우, class 속성을 필터링 조건에 추가해서 추출함.
'# property_class.py
import bs4
html_str = """
<html>
    <body>
        <ul class ="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class ="replay">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul",{"class":"replay"})
print(ul)
결과:
 
.find()를 사용할 때, “ul”말고 {“class”:”replay”} 조건을 하나 더 추가해주면 뽑고 싶은 요소에 조금 더 정확하게 접근할 수 있음.
class를 이용하면 같은 태그가 있을 때 특정 블록을 선택해서 뽑아낼 수 있음.

=>속성값 뽑아내기
a태그에서 링크를 뽑아낼 때는 href라는 속성의 속성값을 뽑아내야 함.
'# property_href.py
import bs4
html_str ="""
<html>
    <body>
        <ul class= "ko">
            <li>
                <a href="https://www.naver.com">네이버</a>
            </li>
            <li>
                <a href="https://www.daum.net">다음</a>
            </li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
atag = bs_obj.find("a")
print(atag)
print(atag.text)
print(atag['href'])
print("="*50)
atagl = bs_obj.findAll("a")
for i in range(len(atagl)):
print(atagl[i]['href'])
결과:
 
a태그에 들어 있는 텍스트인 ‘네이버’를 뽑으려면 atag.text를 사용함
href속성의 속성 값인 네이버의 주소 https://www.naver.com/을 뽑기 위해서는 atag[‘href’] 이렇게 대괄호 안에 ‘를 붙인 속성을 넣어주면 ‘속성값’을 뽑아낼 수 있음.
a태그에서 대괄호 안에 'href‘를 붙인 속성을 넣어주면 속성값을 뽑아 냄

4. 네이버에서 특정 글자 추출하기
네이버 첫 페이지에서 맨 오른쪽 위에 있는 ‘네이버를 시작페이지로‘라는 단어 두 개만 뽑아보기
 
=> urllib로 네이버 첫 페이지 데이터 받아오기
웹에서 데이터를 받아오려면 request라는 요청을 보내서 받아와야 함.
파이썬에서 웹의 특정 주소로 요청을 보내는 기능은 urllib.request의 urlopen() 이라는 함수를 사용함.
'# naver_text.py
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
#html이라는 변수 안에 텍스트 형식으로 네이버 첫
#페이지를 호출한 데이터가 문자열 형태로 들어감
print(html.read())
결과:
 
네이버 첫 페이지를 받아오면, b’<!doctype html> 시작해서 </html>로 끝나는 데이터가 받아와 짐.

=>뷰티풀솝에 데이터 넣기
urlopen() 이라는 함수를 이용해 받아온 데이터를 파싱하기 위해서는 뷰티풀솝에 데이터를 넣어서 파이썬에서 가공할 수 있는 형태로 만들어 주어야 함.
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
#html이라는 변수 안에 텍스트 형식으로 네이버 첫
#페이지를 호출한 데이터가 문자열 형태로 들어감
#print(html.read())
bs_obj = bs4.BeautifulSoup(html,"html.parser")
print(bs_obj)
결과:
 
bs_obj = bs4.BeautifulSoup(html, "html.parser")
.BeautifulSoup(<받은텍스트>, <텍스트를 파싱할 파서>)에는 총 2가지가 들어감.
받은 텍스트 : 웹에서 받은 텍스트
텍스트를 파싱할 파서 : 웹 문서는 대부분 HTML로 되어 있어서 “html.parser”를 사용
- parser(파서)는 데이터를 뽑아내는(파싱) 프로그램임.
- 파이썬이 HTML 형식으로 인식하라는 뜻임.
- “html.parser”를 가장 많이 사용하며, “lxml”과 “xml” 등도 있음.

=>뷰티풀솝으로 필요한 부분 뽑아내기
원하는 데이터 HTML상에 어디에 있는지 찾기 위해서는 구글 크롬의 ‘개발자 도구’를 이용함.
크롬을 켜고 우측 상단에 ···버튼을 눌러서 [도구 더보기 → 개발자 도구]
 

개발자 도구에서 왼쪽 위의 화살표 아이콘을 누르면 색이 파란색으로 바뀌고, 마우스를 움직여 원하는 위치를 클릭하면 소스코드에서 해당부분을 알려줌.
‘네이버를 시작페이지로’ 버튼을 마우스로 찾은 후에 클릭하면, HTML 소스코드에서 어떤 부분인지 표시를 해줌.
 
 
‘네이버를 시작페이지로’는 <a>라는 태그 안에 텍스트가 들어 있는 형태임.
• <a>네이버를 시작페이지로<span></span></a>
HTML 코드를 보면, <div>라는 태그 안에 <a></a>가 들어 있는 구조임.
 
div 태그 안에 class=“area_links” 부분은 클래스를 가지고 파이썬의 뷰티풀솝 라이브러리를 이용해 데이터를 뽑아낼 수 있기 때문에 매우 중요함.
<div class=“area_links”></div> 이 영역만 추출해보도록 하겠음.
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
'#html이라는 변수 안에 텍스트 형식으로 네이버 첫
'#페이지를 호출한 데이터가 문자열 형태로 들어감
'#print(html.read())
bs_obj = bs4.BeautifulSoup(html,"html.parser")# bs_obj에는 전체 소스가 들어 있음
'#print(bs_obj)
top_right = bs_obj.find("div",{"class":"area_links"})
#div 태그 중에서 class가 “area_links”로 되어있는 div를 찾으라는 명령
print(top_right)
결과:
 

top_right = bs_obj.find("div", {"class":"area_links"})
• bs_obj에는 전체 소스가 들어 있음.
• bs_obj.find(“div“) 명령어는 전체에서 가장 처음 나타나는 <div>태그를 뽑으라는 명령
• “div”옆에 ,(콤마)를 찍고 {“class”:”area_links”}를 추가하면, div 태그 중에서 class가 “area_links”로 되어있는 div를 찾으라는 명령
이제 필요한 ‘네이버를 시작페이지로‘ 글자만 뽑아보겠음.
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
'#html이라는 변수 안에 텍스트 형식으로 네이버 첫
'#페이지를 호출한 데이터가 문자열 형태로 들어감
'#print(html.read())
bs_obj = bs4.BeautifulSoup(html,"html.parser")# bs_obj에는 전체 소스가 들어 있음
'#print(bs_obj)
top_right = bs_obj.find("div",{"class":"area_links"})
'#div 태그 중에서 class가 “area_links”로 되어있는 div를 찾으라는 명령
'#print(top_right)
first_a = top_right.find("a")#첫 번째 나오는 a태그를 찾음
print(first_a)# a태그 안에 있는 text만 뽑아냄
결과:
 

=>공지사항 등 기타 뽑아내기
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
'#html이라는 변수 안에 텍스트 형식으로 네이버 첫
'#페이지를 호출한 데이터가 문자열 형태로 들어감
'#print(html.read())
bs_obj = bs4.BeautifulSoup(html,"html.parser")# bs_obj에는 전체 소스가 들어 있음
'#print(bs_obj)
top_right = bs_obj.find("div",{"class":"area_links"})
'#div 태그 중에서 class가 “area_links”로 되어있는 div를 찾으라는 명령
'#print(top_right)
first_a = top_right.find("a")#첫 번째 나오는 a태그를 찾음
print(first_a)# a태그 안에 있는 text만 뽑아냄
print(first_a.text)

first_a1 = bs_obj.find("a",{"class":"al_favorite"})
print(first_a1.text)

###공지사항
notice_div = bs_obj.find("div",{"class":"area_notice"})
notice_a = notice_div.find("a",{"class":"an_ta"})
print(notice_a.text)

notice_h2 = bs_obj.find("h2",{"class":"blind"})
print(notice_h2)
결과:
 

5. 네이버 메뉴 이름 뽑아내기
=>네이버 첫 페이지에서 메뉴에 있는 ‘메일‘, ‘카페’, ‘블로그‘ 등의 글자 뽑아내기
메뉴 이름을 뽑는 방법과 뉴스 페이지에서 뉴스 제목을 뽑는 방법은 아주 비슷하므로 메뉴를 뽑아 보면서 크롤링을 익힐 수 있음.
 
결과
 

=>추출할 범위의 class 알아내기
[크롬] 메뉴에서 [···버튼 → 도구 더보기 → 개발자 도구 → 왼쪽위 화살표버튼]
 
<ul>···</ul>안에는 여러 개의 <li>···</li>태그가 들어 있으며, 네이버 메뉴들은 <li class=“an_item”>···</li> 구조 안에 들어 있음.
 
 
파이썬에서 <ul> 태그와 클래스(class)를 이용하여 li안에 있는 내용을 뽑아낼 예정임.

파이썬의 BeautifulSoup 라이브러리를 이용해 필요한 글자를 뽑아낼 수 있음.
• ul 태그와 class가 “an_l”인 ul을 전체 문서에서 찾기
'# naver_menu.py
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")
ul = bs_obj.find("ul",{"class":"an_l"})# ul 태그 중에서 class가 an_l인 ul을 찾음
print(ul)
결과:
 

ul안에 들어 있는 각각의 li만 뽑기
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")
ul = bs_obj.find("ul",{"class":"an_l"})# ul 태그 중에서 class가 an_l인 ul을 찾음
'#print(ul)
for li in ul:
    print(li)
결과:
 

=> .findAll( )로 li만 뽑아내기
.findAll( )은 조건에 해당하는 모든 것들을 [ ]리스트 안으로 추출해주는 함수임.
반복문 for를 이용해도 되지만, 중간에 빈칸이 뽑히는 경우가 있어서 .findAll( )을 써서 한 번 더 뽑아 주는 게 좋음.
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")
ul = bs_obj.find("ul",{"class":"an_l"})# ul 태그 중에서 class가 an_l인 ul을 찾음
'#print(ul)
'#for li in ul:
'#    print(li)
lis = ul.findAll("li")# ul 안에 있는 모든 li를 찾으라는 명령
print(lis)

----- [ ]리스트 안에 <li></li>가 여러 개 들어 있으며, 콤마(,)로 구분된 형태
결과:
 

=> li 하나씩 꺼내서 출력하기
대괄호와 중간의 콤마(,)가 나오지 않게 하나씩 뽑아보기
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")
ul = bs_obj.find("ul",{"class":"an_l"})# ul 태그 중에서 class가 an_l인 ul을 찾음
'#print(ul)
'#for li in ul:
'#    print(li)
lis = ul.findAll("li")# ul 안에 있는 모든 li를 찾으라는 명령
'# ul를 바로 for문을 사용하여 출력하면 중간에 빈칸이 뽑히는 경우가 있음
'#print(lis)
for li in lis:
    print(li)# lis 안에 있는 li들을 하나씩 꺼내서 출력
결과:
 

=>a태그 뽑아내기
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")
ul = bs_obj.find("ul",{"class":"an_l"})# ul 태그 중에서 class가 an_l인 ul을 찾음
'#print(ul)
'#for li in ul:
'#    print(li)
lis = ul.findAll("li")# ul 안에 있는 모든 li를 찾으라는 명령
'# ul를 바로 for문을 사용하여 출력하면 중간에 빈칸이 뽑히는 경우가 있음
'#print(lis)
for li in lis:
    #print(li)# lis 안에 있는 li들을 하나씩 꺼내서 출력
    a_tag = li.find("a")
    # li안에 있는 a태그를 뽑아서 a_tag라는 변수에 넣으라는 명령(점점 세밀하게 필요한 내용에 접근 )
    print(a_tag)
결과:
 
=> span인 것 중에 an_txt인 class 뽑아내기
 
<a>태그 안에 <span>이 두 개가 있으므로, 태그인 span과 클래스인 an_txt 두 조건으로 추출해야 함.
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")
ul = bs_obj.find("ul",{"class":"an_l"})# ul 태그 중에서 class가 an_l인 ul을 찾음
'#print(ul)
'#for li in ul:
'#    print(li)
lis = ul.findAll("li")# ul 안에 있는 모든 li를 찾으라는 명령
'# ul를 바로 for문을 사용하여 출력하면 중간에 빈칸이 뽑히는 경우가 있음
'#print(lis)
for li in lis:
    #print(li)# lis 안에 있는 li들을 하나씩 꺼내서 출력
    a_tag = li.find("a")
    # li안에 있는 a태그를 뽑아서 a_tag라는 변수에 넣으라는 명령(점점 세밀하게 필요한 내용에 접근 )
    #print(a_tag)
    span = a_tag.find("span",{"class":"an_txt"})
    # span 태그 중에서 an_txt 클래스를 가진것만 뽑으라는 명령
    print(span)
결과:
 

=>Text 뽑아내기
<span> 태그가 제외된, ‘메일’만 들어 있는 순수한 텍스트만 뽑아내기
import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)# html이라는 변수 안에는 웹에서 받은 텍스트가 들어감

bs_obj = bs4.BeautifulSoup(html,"html.parser")
'#bs4.BeautifulSoup() 에 웹에서 받은 텍스트를
'#넣으면, 파이썬에서 가공할 수 있는 html 형태의
'#텍스트가 bs_obj에 들어감
ul = bs_obj.find("ul",{"class":"an_l"})# ul 태그 중에서 class가 an_l인 ul을 찾음
'#print(ul)
'#for li in ul:
'#    print(li)
lis = ul.findAll("li")# ul 안에 있는 모든 li를 찾으라는 명령
'# ul를 바로 for문을 사용하여 출력하면 중간에 빈칸이 뽑히는 경우가 있음
'#print(lis)
for li in lis:
    #print(li)# lis 안에 있는 li들을 하나씩 꺼내서 출력
    a_tag = li.find("a")
    # li안에 있는 a태그를 뽑아서 a_tag라는 변수에 넣으라는 명령(점점 세밀하게 필요한 내용에 접근 )
    #print(a_tag)
    span = a_tag.find("span",{"class":"an_txt"})
    # span 태그 중에서 an_txt 클래스를 가진것만 뽑으라는 명령
    #print(span)
    print(span.text)# span 태그에서 text만 뽑아내는 부분
결과:
 

6. 네이버 뉴스 제목 가져오기
=>네이버 뉴스의 오늘의 기사 제목 가져오기
 
 

=>뉴스 페이지 불러오기
'# naver_news.py import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
print(bs_obj)
결과:
 

=> 뉴스 제목 위치 찾기
[크롬] 메뉴에서 [···버튼 → 도구 더보기 → 개발자 도구 → 왼쪽위 화살표버튼]
 

=> HTML 구조 분석하기
 
HTML 구조를 분석해 보면, <li>안에 <a>가 들어 있고, <a>안에 <strong>이 들어 있고, <strong>안에 뉴스 제목이 있는 형태임.
개발자 도구에서 선택된 부분은 <ul>안에 위의 구조가 반복되고, <li>가장 안쪽에 <strong>이 있고 거기에 기사 제목이 들어 있는 구조임.
• 선택한 범위는 ul이고, class는 ‘mlist2 no_bg’임.
 

=> class로 ul 태그 찾기
import bs4
import urllib.request

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
'#print(bs_obj)
mlist2_no_bg = bs_obj.find("ul", {"class": "mlist2 no_bg"})
'#bs_obj에서 class가 ‘mlist2 no_bg’ 인 ul 태그를 찾음
print(mlist2_no_bg)
결과:
 

=> .findAll( )로 li들 뽑아내기
import bs4
import urllib.request

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
'#print(bs_obj)
mlist2_no_bg = bs_obj.find("ul", {"class": "mlist2 no_bg"})
'#bs_obj에서 class가 ‘mlist2 no_bg’ 인 ul 태그를 찾음
'#print(mlist2_no_bg)
lis = mlist2_no_bg.findAll("li")
'#lis 변수를 선언하고, ‘mlist2 no_bg’ 에서 li 태그들을
'#리스트[ ] 형태로 담으라는 명령
for li in lis:# for 문을 이용해 lis에 있는 li들을 하나씩 꺼내서 출력
    print(li)
결과:
 

=> strong 태그와 그 안에 있는 기사 제목 뽑아내기
import bs4
import urllib.request

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
'#print(bs_obj)
mlist2_no_bg = bs_obj.find("ul", {"class": "mlist2 no_bg"})
'#bs_obj에서 class가 ‘mlist2 no_bg’ 인 ul 태그를 찾음
'#print(mlist2_no_bg)
lis = mlist2_no_bg.findAll("li")
'#lis 변수를 선언하고, ‘mlist2 no_bg’ 에서 li 태그들을
'#리스트[ ] 형태로 담으라는 명령
for li in lis:# for 문을 이용해 lis에 있는 li들을 하나씩 꺼내서 출력
    #print(li)
    strong = li.find("strong")
    print(strong)
결과:
 

=> Text 뽑아내기
import bs4
import urllib.request

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
'#print(bs_obj)
mlist2_no_bg = bs_obj.find("ul", {"class": "mlist2 no_bg"})
'#bs_obj에서 class가 ‘mlist2 no_bg’ 인 ul 태그를 찾음
'#print(mlist2_no_bg)
lis = mlist2_no_bg.findAll("li")
'#lis 변수를 선언하고, ‘mlist2 no_bg’ 에서 li 태그들을
'#리스트[ ] 형태로 담으라는 명령
for li in lis:# for 문을 이용해 lis에 있는 li들을 하나씩 꺼내서 출력
    #print(li)
    strong = li.find("strong")
    #print(strong)
    print(strong.text)
결과:
 

===========20191220
=>네이버 헤드라인 뉴스
#naver_headlinenews.py
import urllib.request
import bs4
import time
import os
while True:
    url = "https://news.naver.com/"
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    ul = bs_obj.find("ul", {"class": "hdline_article_list"})
    div = ul.findAll("div", {"class": "hdline_article_tit"})

    #print(lis)
    for i in range(0, len(div)):
        a_tag = div[i].find("a")
        print(a_tag.text.strip())

    time.sleep(5)
    os.system("cls")
결과:
 

=>네이버 중간 메뉴 뽑아보기
'#naver_menu_middle.py
import urllib.request
import bs4
url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

div = bs_obj.find("div", {"class": "rolling-container"})

lis = div.findAll("li")
'#print(lis)

for i in range(0, len(lis)):
    a_tag = lis[i].find("a")
#    span_tag = a_tag.find("span", {"class": "an_txt"})
    print(a_tag.text)
결과:
 

=>네이버 메뉴 오른쪽 
#naver_menu_right.py
import urllib.request
import bs4
url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
ul = bs_obj.find("ul", {"id": "PM_ID_serviceNavi"})
lis = ul.findAll("li")
'#print(lis)
for i in range(0, len(lis)):
    a_tag = lis[i].find("a")
    span_tag = a_tag.find("span", {"class": "an_txt"})
    print(span_tag.text)
결과:
 

프로젝트 명 : 뉴스 빅데이터 분석 시스템 구축
1.데이터베이스 구축
데이터베이스 생성 : naverDB
테이블 생성 : news
=>테이블 생성
'#db_create.py
import sqlite3

con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

cur.execute("DROP TABLE news")#테이블 있으면 삭제하고 해야 한다.
#위에것 최초생성시 주석 처리한다.
cur.execute("CREATE TABLE news (div char(10), title char(100), writer char(10))")

con.commit()
con.close()
=>테이블 생성 및 인덱스 생성
'#db_create2.py
import sqlite3

con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

#cur.execute("DROP TABLE news1")
cur.execute("CREATE TABLE news1 (wrdt data,div char(20),title char(100),writer char(20))")
cur.execute("create index wrdt on news1 (wrdt)")

con.commit()
con.close()

2.네이버 뉴스(정치) 데이터 수집
DB 테이블 저장 : news
파일 저장 : news.txt
'#naver_news_db2.py
import urllib.request
import bs4
import time
import sqlite3

'## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3 = "", "", ""
sql = ""

'# 메인 코드 부분 ##
while True:
    url = "http://news.naver.com/"
    html = urllib.request.urlopen(url)

    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    hdline_article_list = bs_obj.find("ul", {"class":"hdline_article_list"})
    lis = hdline_article_list.findAll("li")

    con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
    cur = con.cursor()

    for li in lis:
        a = li.find("a")
        a.text.strip()

        data1 = "정치"  # 뉴스 구분
        data2 = a.text.strip()
        data2 = data2.replace("'", "\"")  # 뉴스 제목
        data3 = "ydgil"  # 작성자

        sql = "INSERT INTO news1 VALUES(datetime(), '" + data1 + "', '" + data2 + "', '" + data3 + "')"
        cur.execute(sql)

    con.commit()
    con.close()
    time.sleep(3600)

==>헤드라인 뉴스 뽑아보기
'#naver_news_database.py
import urllib.request
import bs4
import time
import os
import sqlite3

con, cur = None, None
data1, data2, data3 = "", "", ""
sql = ""

con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

while True:
    url = "https://news.naver.com/"
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    ul = bs_obj.find("ul", {"class": "hdline_article_list"})
    div = ul.findAll("div", {"class": "hdline_article_tit"})

    # print(lis)

    for i in range(0, len(div)):
        a_tag = div[i].find("a")
        print(a_tag.text.strip())

        data1 = "헤드라인"
        data2 = a_tag.text.strip()
        data2 = data2.replace("'","\"")
        data3 = "SHee28"
        sql = "INSERT INTO news VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "')"
        #print(sql)
        cur.execute(sql)
    # print(sql)
    

    con.commit()
    con.close()

    # time.sleep(5)
    # os.system("cls")

3.네이버 뉴스(전체) 데이터 수집
파일 저장 : news.csv
=>전체 뉴스 일기
'#naver_news_db.py
import urllib.request
import bs4
import time
import os
import sqlite3

con, cur = None, None
data1, data2, data3 = "", "", ""
sql = ""

con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

while True:
    url = "https://news.naver.com/"
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")
    #div = bs_obj.findAll("div",{"class":"mtype_list_wide"})
    #print(div)
    first_h = bs_obj.find("ul", {"class": "hdline_article_list"})
    lis = first_h.findAll("li")
    # print(lis)

    #헤드라인 뉴스 검색
    for i in range(len(lis)):
        a = lis[i].find("a")

        data1 = "헤드라인 뉴스"  # 뉴스 구분
        data2 = a.text.strip()
        data2 = data2.replace("'", "\"")  # 뉴스 제목
        data3 = "hhh"  # 작성자
        sql = "INSERT INTO news1 VALUES(datetime('now','localtime'),'" + data1 + "', '" + data2 + "', '" + data3 + "')"
        print(sql)
        cur.execute(sql)

    #기타 뉴스 검색
    first_a_list = bs_obj.findAll("ul",{"class":"mlist2 no_bg"})
    title = bs_obj.findAll("h4")#title가져오기

    for i in range(len(first_a_list)):
        lis = first_a_list[i].findAll("li")

        for li in lis:
            a = li.find("a")
            writer= li.find("span",{"class":"writing"}).text

            data1 = title[i+1].text #뉴스 구분
            data2 = a.text.strip()
            data2 = data2.replace("'", "\"")#뉴스 제목
            data3 = writer#작성자
            sql = "INSERT INTO news1 VALUES(datetime('now','localtime'),'" + data1 + "', '" + data2 + "', '" + data3 + "')"
            print(sql)
            cur.execute(sql)

    con.commit()
    con.close()
    time.sleep(3600)#한시간 마다 들어간다.
    # os.system("cls")

=>텍스트 파일 읽기
'#naver_news_db_write_file.py
import urllib.request
import bs4
import time
import os
import sqlite3

con, cur = None, None
data0,data1, data2, data3 ="", "", "", ""
row = None
sql = ""
result = ""
con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

cur.execute("select * from news1")
f = open("news.txt",'w')
while True:
    row = cur.fetchone()
    if row == None:
        break
    data0 = row[0]
    data1 = row[1]
    data2 = row[2]
    data3 = row[3]
    result = data0+"|"+data1+"|"+data2+"|"+data3+"\n"
    f .write(result)

f.close()
결과:
 

=>csv파일 읽ㄱ
'#naver_all_urllib.request
import bs4
import time
import os
import sqlite3
import csv

con, cur = None, None
data0,data1, data2, data3 ="", "", "", ""
row = None
sql = ""
result = ""
con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

cur.execute("select * from news1")
f = open("news.csv",'w',encoding="UTF-8")#경로 바꿀 수 있음
list = []

while True:
    row = cur.fetchone()
    if row == None:
        break
    #list = []
    #list.insert(0,row[0])
    #list.insert(1, row[1])
    #list.insert(2, row[2])
    #list.insert(3, row[3])
    #wr = csv.writer(f)
    #wr.writerow(list)
    result = ""
    data0 = row[0].strip()
    data1 = row[1].strip()
    data2 = row[2].replace(",", ".")
    data3 = row[3]

    result = "%s, %s, %s, %s\n" % (data0,data1,data2,data3)
    print(result)
    #result = data0+","+ data1+","+data2+","+ data3+"\n"
    f.write(result)

con.close()
f.close()
결과: utf-8로 해서 오류가 난다.
 

4.뉴스 빅데이터 분석
3번파일 텍스트 마이닝
막대 그래프
워드 클라우드
# datamining.R
rm(data)
#뉴스만 분석 R에서 하기

library(ggplot2)
library(dplyr)
library(rJava)
library(memoise)
library(KoNLP)
library(stringr)
library(data.table)
'#data <- fread("c:/crawl/news1.csv",header = F,encoding = "UTF-8")#UTF-8
''#data <- read.csv("c:/crawl/news1.csv",header = F)
data <- fread("c:/crawl/news1.csv",header = F)
''#read.csv원하는 값 이상하게 들어옴
data
head(data)

txt <- str_replace_all(data$V3,"//w","")#특수문자 제거
'#txt1 <- str_replace_all(data$V3,"\\w","")#특수문자 제거->오류
txt
str(txt)

nouns <- extractNoun(txt)
nouns

wordCount <- table(unlist(nouns))
wordCount

df_word <- as.data.frame(wordCount,stringsAsFactors = F)
df_word  <- rename(df_word,word = Var1,freq =Freq)
df_word <- filter(df_word,nchar(word)>= 2)
top_20 <- df_word %>% 
    arrange(desc(freq)) %>% 
    head(20)
top_20

library(wordcloud)
library(RColorBrewer)

pal <- brewer.pal(8,"Dark2")
''#pal <- brewer.pal(9,"Blues")[5:9]
#
set.seed(1201)
wordcloud(words= df_word$word, 
          freq = df_word$freq,
          min.freq = 2,
          max.words = 200,
          random.order = F,
          rot.per = .1,
          scale = c(4,0.3),
          colors = pal)
'#set.seed(1202)
'#set.seed(Sys.time())

wordcloud(words= df_word$word, 
          freq = df_word$freq,
          min.freq = 2,
          max.words = 200,
          random.order = F,
          rot.per = .1,
          scale = c(4,0.3),
          colors = pal)

top_20$word
data_y <- top_20$freq
names(data_y) <- top_20$word
barplot(data_y,main="word",ylab="frequency")

ggplot(data = top_20,aes(x= word,y = freq,fill=word))+geom_bar(stat = 'identity')
5.다음…

=>다움 뉴스
import urllib.request
import bs4
import time
import os
import sqlite3

con, cur = None, None
data1, data2, data3 = "", "", ""
sql = ""

con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

while True:
    url = "https://media.daum.net/"
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")
    first_div = bs_obj.find("div",{"class":"box_headline"})
    first_ul_list = first_div.findAll("ul",{"class":"list_headline"})
    #ul
    for first_ul in first_ul_list:
        #li
        first_li_list = first_ul.findAll("li")
        for j in range(1,len(first_li_list)):
            strong_tag = first_li_list[j].find("strong",{"class":"tit_g"})
            a_tag = strong_tag.find("a",{"class":"link_txt"})
            writer = strong_tag.find("span", {"class": "info_news"})
            if a_tag != None:
                data1 = "daum"  # 뉴스 구분
                data2 = a_tag.text.strip()
                data2 = data2.replace("'", "\"")  # 뉴스 제목
                data3 = writer.text  # 작성자
                sql = "INSERT INTO news1 VALUES(datetime('now','localtime'),'" + data1 + "', '" + data2 + "', '" + data3 + "')"
                print(sql)
                cur.execute(sql)

    con.commit()
    con.close()
    time.sleep(3600)  # 한시간 마다 들어간다.



=>구글 실패 
암호화 등 내용이 많아서 
import urllib.request
import bs4
import time
import os
import sqlite3

con, cur = None, None
data1, data2, data3 = "", "", ""
sql = ""

con = sqlite3.connect("../sqlite-tools-win32-x86-3300100/naverDB")
cur = con.cursor()

while True:
    url = "https://news.google.com/?hl=ko&tab=rn1&gl=KR&ceid=KR:ko"
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")
    div_list = bs_obj.findAll("div",{"class":"xrnccd F6Welf R7GTQ keNKEd j7vNaf"})

    title_list = bs_obj.findAll("a",{"class":"wmzpFf"})

    #ul
    title=""
    for i in range(len(div_list)):
        #li
        a_list = div_list[i].findAll("a",{"class":"DY5T1d"})
        for i in range(len(a_list)):
            writer = div_list[i].findAll("a",{"class":"wEwyrc AVN2gc uQIVzc Sksgp"})[i]

            data1 = "google"  # 뉴스 구분
            data2 = a_list[i].text.strip()
            data2 = data2.replace("'", "\"").replace("\u2027","")  # 뉴스 제목
            print(data2)
            data3 = writer.text  # 작성자
            sql = "INSERT INTO news1 VALUES(datetime('now','localtime'),'" + data1 + "', '" + data2 + "', '" + data3 + "')"
            print(sql)
            cur.execute(sql)


    con.commit()
    con.close()
    time.sleep(3600)  # 한시간 마다 들어간다.




