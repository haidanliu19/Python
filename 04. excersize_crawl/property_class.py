import bs4
html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="replay">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul", {"class":"replay"})
#.find()는 첫 번째로 만나는 ul 태그만을 리턴함.
#class 속성을 필터링 조건에 추가해서 추출함.
print(ul)