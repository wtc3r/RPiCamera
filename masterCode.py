#master script

#import libraries
    #general libraries:
from masterFunctions import *
from time import sleep

    #Temperatuur sensor:
from SenseTemperature import *
# print(read_temp())

    #take_photo:
from take_photo import *
# preview(2)
# snap("test01.jpg")

    #OLED scherm:
from OLEDbaseCode import *
# writeText("Hello")
# showImage("test01.jpg")
# sleep(2)
# emptyOLED()

    #numpadInput:
from numpadInput import numpadInput
# print(numpadInput())

## START CODE ##
active = True
sleep_time = 0.05
class Menu():
    def item_1(self):
        print('1')
        sleep(sleep_time)
        return True
    def item_2(self):
        print('2')
        sleep(sleep_time)
        return True
    def item_3(self):
        print('3')
        sleep(sleep_time)
        return True
    def item_4(self):
        print('4')
        sleep(sleep_time)
        return True
    def item_5(self):
        print('5')
        sleep(sleep_time)
        return True
    def item_6(self):
        print('6')
        sleep(sleep_time)
        return True
    def item_7(self):
        print('7')
        sleep(sleep_time)
        return True
    def item_8(self):
        print('8')
        sleep(sleep_time)
        return True
    def item_9(self):
        print('9')
        sleep(sleep_time)
        return True
    def item_10(self):
        print('10')
        sleep(sleep_time)
        return True
    def item_11(self):
        print('11')
        sleep(sleep_time)
        return True
    def item_12(self):
        print('12')
        return False
    def getItem(self,no):
        name_of_item="item_"+str(no)
        method=getattr(self,name_of_item,lambda :'Invalid input')
        return method()

mo = Menu()
active = True
last_num = 0
while(active):
    num = numpadInput()
    if num != last_num:
        active = mo.getItem(num) 
    last_num = num
