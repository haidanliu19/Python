#thread_test.py
import time

def long_task():#5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1) #1초간 대기한다.
        print("working: %s \n" % i)

print("Start")
for i in range(5): #long_task를 5회 수행한다.
    long_task()

print("End")
#총 25초의 시간이 걸린다.

#thread_test.py
import time
import threading #스레드를 생성하기 위해서는 threading모듈이 필요하다.
def long_task():#5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1) #1초간 대기한다.
        print("working: %s \n" % i)
print("Start")

threads = []
for i in range(5): #long_task를 5회 수행한다.
    t = threading.Thread(target = long_task) #스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start() #스레드를 실행한다.
    

print("End")
#5초 걸린다.

#thread_test.py
import time
import threading #스레드를 생성하기 위해서는 threading모듈이 필요하다.
def long_task():#5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1) #1초간 대기한다.
        print("working: %s \n" % i)
print("Start")

threads = []
for i in range(5): #long_task를 5회 수행한다.
    t = threading.Thread(target = long_task) #스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start() #스레드를 실행한다.

for t in threads:
    t.join() #join으로 스레드가 종료될 때까지 기다린다.
print("End")

#join함수는 해당 스레드가 종료될 때 까지 기다리게 한다. 따라서 위와 같이 수정하면
#우리가 원하던 출력을 보게 된다.
