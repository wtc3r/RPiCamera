# functions used in masterCode.py
from SenseTemperature import *
from take_photo import *
from OLEDbaseCode import *
from numpadInput import numpadInput

def videoFeed():
#'direct' feed on OLED screen:
    active = True
    count = 0
    while(active):
    #     snap("test01.jpg")
        showImageDirect("test01.jpg")
        count += 1
        if count > 50:
            active = False
            
    emptyOLED()
    return True
