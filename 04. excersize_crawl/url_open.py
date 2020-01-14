from urllib.request import urlopen
url = "https://www.naver.com"
html = urlopen(url)
print(html.read())
#첫페이지 크로링 결과
#bs4 를 이용해 파싱해야 한다.