# C:/doit/memo.py 
import sys

option = sys.argv[1]
memo = sys.argv[2]

print(option)
print(memo)


option = sys.argv[1]

if option == 'a':
    memo = sys.argv[2]
    f= open('memo.txt','txt')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = fread()
    f.close()
    print(memo)
