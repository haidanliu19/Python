import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)# html이라는 변수 안에는 웹에서 받은 텍스트가 들어감

bs_obj = bs4.BeautifulSoup(html,"html.parser")
#bs4.BeautifulSoup() 에 웹에서 받은 텍스트를
#넣으면, 파이썬에서 가공할 수 있는 html 형태의
#텍스트가 bs_obj에 들어감
ul = bs_obj.find("ul",{"class":"an_l"})# ul 태그 중에서 class가 an_l인 ul을 찾음
#print(ul)
#for li in ul:
#    print(li)
lis = ul.findAll("li")# ul 안에 있는 모든 li를 찾으라는 명령
# ul를 바로 for문을 사용하여 출력하면 중간에 빈칸이 뽑히는 경우가 있음
#print(lis)
for li in lis:
    #print(li)# lis 안에 있는 li들을 하나씩 꺼내서 출력
    a_tag = li.find("a")
    # li안에 있는 a태그를 뽑아서 a_tag라는 변수에 넣으라는 명령(점점 세밀하게 필요한 내용에 접근 )
    #print(a_tag)
    span = a_tag.find("span",{"class":"an_txt"})
    # span 태그 중에서 an_txt 클래스를 가진것만 뽑으라는 명령
    #print(span)
    print(span.text)# span 태그에서 text만 뽑아내는 부분