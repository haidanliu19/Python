import bs4
import urllib.request

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
#print(bs_obj)
mlist2_no_bg = bs_obj.find("ul", {"class": "mlist2 no_bg"})
#bs_obj에서 class가 ‘mlist2 no_bg’ 인 ul 태그를 찾음
#print(mlist2_no_bg)
lis = mlist2_no_bg.findAll("li")
#lis 변수를 선언하고, ‘mlist2 no_bg’ 에서 li 태그들을
#리스트[ ] 형태로 담으라는 명령
for li in lis:# for 문을 이용해 lis에 있는 li들을 하나씩 꺼내서 출력
    #print(li)
    strong = li.find("strong")
    #print(strong)
    print(strong.text)
