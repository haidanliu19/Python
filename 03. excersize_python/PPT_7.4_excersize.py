#1
a = "a:b:c:d"
b = a.split(":")
"#".join(b)

#2
a = {'A':90,'B':80}
#a['C']
a.get('C',70)

#3
a = [1,2,3]
a = a + [4,5]
a

a = [1,2,3]
a.extend([4,5])
a

#4
A= [20,55,67,82,45,33,90,87,100,25]
sum = 0
for i in A:
    if i >= 50:
       sum += i
print(sum)#481

#5
def fibo1(n):
    if n == 0 : return 0
    elif n == 1: return 1
    else:
        return fibo1(n-1) +fibo1(n-2)

for i in range(10):
    fibo1(i)

#6
user_input = input("숫자를 입력하여 주십시요.")
# 65,45,2,3,45,8
user_input = user_input.split(",")
sum = 0
for i in user_input:
    sum += int(i)
print(sum)
    
#7
user_input = int(input("숫자를 입력하여 주십시요."))
for i in range(1,10):
    print(i * user_input,end =" ")

#8
f = open("abc.txt",'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open("abc.txt",'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()

#9
f = open("sample.txt",'r')
lines = f.readlines()
f.close()

f = open("result.txt",'w')
sum = 0
for i in lines:
    sum += int(i)
f.write(str(sum/len(lines)))
f.close()

#10
class Calculator():
    def __init__(self,numberlist):
        self.numberlist = numberlist
    def sum(self):
        result = 0
        for num in self.numberlist:
            result += num
        return result
    def avg(self):
        total = self.sum()
        return total/len(self.numberlist)
    
cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()

#11
#import sys
#sys.path.append("c:\doit")
#import mymod

#12
result = 0
try:
    [1,2,3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 1
except IndexError:
    result += 1
finally:
    result += 4

print(result)

#13
a = "4546793"
import re
pat = re.compile("(\d{3})(\d{2})(\d{1})(\d{1})")
#454-*67-9-3
print(pat.sub("\g<1>-*\g<2>-\g<3>-\g<4>",a))

#14
def compress_string(s):
    _c = ""
    cnt = 0
    result =""
    for c in s:
        if c!= _c:
            _c = c
            if cnt :result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt +=1
    if cnt : result += str(cnt)
    return result

print(compress_string("aaabbcccccca"))

#15
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(s)
        else:
            return false
    return len(result) == 10

print(chkDupNum("0123456789"))
print(chkDupNum("01234"))
print(chkDupNum("01234567890"))
print(chkDupNum("6789012345"))
print(chkDupNum("012322456789"))

#16

dic = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G"
       ,"....":"H","I":"..",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N"
       ,"---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T"
       ,"..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z"}
def morse(src):
    result = []
    for word in src.split(" "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)

print(morse(".... ... .-.. . . .--. ... . .- .-.. -.--"))

#17
import re
p = re.compile("a[.]{3,}b")
print(p.search("acccb"))
print(p.search("a....b"))
print(p.search("aaab"))
print(p.search("a.cccb"))

#18
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
m.start()+m.end()

#19
data = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
import re
p = re.compile("(\d{3}[-]+\d{4}[-])\d{4}")
print(p.sub(r"\g<1>-####",data))

#20
import re
pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pankey@gmail.com"))
print(pat.match("kim@daum.com"))
print(pat.match("lee@myhome.com"))

