#master script

#import libraries
    #general libraries:
from masterFunctions import *
from time import sleep
from datetime import datetime

    #Temperatuur sensor:
from SenseTemperature import *
# print(read_temp())

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
# first show a start screen
# Initialize time
t0 = datetime.now()

showImage('7Kgn.gif')
sleep(2)
emptyOLED()


active = True
sleep_time = 0.05
class Menu():
    def item_1(self):
        takePhotoInterval()
        sleep(sleep_time)
        return True
    def item_2(self):
        print(datetime.now() - t0)
        sleep(sleep_time)
        return True
    def item_3(self):
        print('3')
        videoFeed()
        sleep(sleep_time)
        return True
    def item_4(self):
        print('4')
        emptyOLED()
        sleep(sleep_time)
        return True
    def item_5(self):
        print('5')
        showImage('7Kgn.gif')
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

# prepare vars
active = True
num = 0
last_num = 0
nPress = 0

while(active):
    num, nPress = numpadInput(num,nPress)
    active = mo.getItem(num)
#close & clean up
emptyOLED()
