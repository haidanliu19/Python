import bs4
#BeautifulSoup(뷰티풀솝)
#뷰티풀솝은 데이터를 추출하는 데 필요한 기능이 들어 있는 라이브러리이며, 파싱 라이브러리라고도 함.
html_str = '<html><div>hello</div></html>'
#hello만 뽑아 올것이다.
#BeautifulSoup 예쁘게 나오기 위해서
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
#html_str소스 코드를 html.parser로 파싱하겠다.

print(type(bs_obj))
print(bs_obj)
print(bs_obj.find("div"))#FIND 테그에 있는 것 보여주기
print(bs_obj.find("div").text)#DIV에 있는  TEXT를 원해