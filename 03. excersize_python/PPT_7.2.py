import re
p = re.compile('ab*')

#match
import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

data=('python','3 python')
p = re.compile('[a-z]+')
for i in data:
    m = p.match(i)
    #print(m)
    #<re.Match object; span=(0, 6), match='python'>
    #None
    if m:
        print("Match Found match: ",m.group())
        print("Match Found match: ",m.start())
        print("Match Found match: ",m.end())
        print("Match Found match: ",m.span())
    else:
        print("No match match")

#search
import re
p = re.compile('[a-z]+')

m = p.search("python")
print(m)

m = p.search("3 python")
print(m)


for i in data:
    m = p.search(i)
    #print(m)
    #<re.Match object; span=(0, 6), match='python'>
    #<re.Match object; span=(2, 8), match='python'>
    
    if m:
        print("Match Found search: ",m.group())
    else:
        print("No match search")


#findall
import re
p = re.compile('[a-z]+')
result = p.findall("life is too short")
print(result)

#finditer
result = p.finditer("life is too short")
print(result)
for r in result:print(r)

#match, search 객체의 메소드 사용 예
import re
p = re.compile('[a-z]+')
m = p.match("python")
m.start()
m.end()
m.span()
m = p.search("3 python")
m.start()
m.end()
m.span()

#DOTALL,S
import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b',re.DOTALL)
m = p.match('a\nb')
print(m)

p = re.compile('a.b',re.S)
m = p.match('a\nb')
print(m)

#re.IGNORECASE 또는 re.I 옵션은 대 · 소문자에 관계 없이 매치함
p = re.compile('[a-z]',re.I)
p.match('python')
p.match('Python')
p.match('PYTHON')

#MULTILINE, M
import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""



import re
p = re.compile("^python\s\w+",re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
print(p.findall(data))

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
&[#] # Start of a numeric entity reference
(
0[0-7]+ # Octal form
| [0-9]+ # Decimal form
| x[0-9a-fA-F]+ # Hexadecimal form
)
; # Trailing semicolon
""", re.VERBOSE)

p = re.compile('\\section')
p = re.compile('\\\\section')

p = re.compile(r'\\section')
