import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

print(re.search('^Life','Life is too short'))
print(re.search('^Life','MyLife'))

print(re.search('short$','Life is too short'))
print(re.search('short$','Life is too short,you need python'))

p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))


p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))

p = re.compile(r'(\b\w+)\s+\1')
p.search('Paris in the the spring').group()

p = re.compile(r'(?P<name>\b\w+)\s+((\d+)[-]\d+[-]\d+)')
m = p.search("park 010-1234-1234")
print(m.group("name"))

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
p.search('Paris in the the spring').group()

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

p = re.compile('(blue|white|red)')
p.sub('colour','blue socks and red shoes')

p.sub('colour','blue socks and red shoes',count=1)

p = re.compile('(blue|white|red)')
p.subn('colour','blue socks and red shoes')

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>","park 010-1234-1234"))

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<2> \g<1>","park 010-1234-1234"))

def hexrepl(match):
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
p.sub(hexrepl,'Call 65490 for printing, 49152 for user code.')

s = '<html><head><title>Title</title>'
len(s)
print(re.match('<.*>',s).span())
print(re.match('<.*>',s).group())

print(re.match('<.*?>',s).group())
