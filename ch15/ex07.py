import random

class TempSensor:
    def __init__(self):
        self.value = 5

    def read_temp(self):
        self.value += random.uniform(-1.0, 1.0)  # -1.0 ~ 1.0
        return self.value

class Boiler:
    def on(self):
        print('보일러가 켜집니다.')

    
class Controller:
    def __init__(self, base, func): # 주입: injection
        self.base = base
        # self.boiler = Boiler()
        self.func = func    # 함수의 참조값 복사  
        self.temp = 10 

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if value < self.base:
            # self.boiler.on()
            self.func() # 함수를 실행하겠다(호출)
        
        self._temp = value

tsensor = TempSensor()
boiler = Boiler()

def light_on():
    print("전등을 켭니다.")

#controller = Controller(5, boiler.on)
controller = Controller(5, light_on)

import time 

# 1초 간격으로 온도를 측정 
while True:
    controller.temp = tsensor.read_temp()
    print(controller.temp)
    time.sleep(1)   # 1초 간격이여서 1 