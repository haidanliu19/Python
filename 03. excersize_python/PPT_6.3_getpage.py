def getTotalPage(m,n):
    return m //n +1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))

#실패 케이스 해결하기
def getTotalPage(m,n):
    if m % n ==0:
        return m // n
    else:
        return m // n +1
    
print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))
