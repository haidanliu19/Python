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
