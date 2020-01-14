#thread_car01.py
#CPU하나가 순서대로 진행한 것이다.
import time
import threading

class RacingCar:
    def __init__(self,name):
        self.carName = name
    def runCar(self):
        for i in range(0,5):
            carStr = self.carName + '-%d만 달립니다.\n' % (i+1)
            print(carStr,end="")
            time.sleep(0.1)

##매인 코드 부분
car1 = RacingCar("H자동차")        
car2 = RacingCar("K자동차")
car3 = RacingCar("D자동차")

#객체를 3개 생성한다.
th1 = threading.Thread(target = car1.runCar)
th2 = threading.Thread(target = car2.runCar)
th3 = threading.Thread(target = car3.runCar)

#스레드 시작 시키는 것 
th1.start()
th2.start()
th3.start()

#스레드 종료 시키는 것 
th1.join()
th2.join()
th3.join()
