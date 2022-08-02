# functions used in masterCode.py
from time import sleep
from datetime import datetime
from SenseTemperature import *
from OLEDbaseCode import *
from numpadInput import numpadInput
from picamera import PiCamera
camera = PiCamera()
#camera.resolution = (1024, 768)
camera.resolution = (128, 32)
# camera.start_preview()
from PIL import Image

def cropImage(im,x,y):     
    # Size of the image in pixels
    # (size of original image)
    # (This is not mandatory)
    width, height = im.size
     
    # Setting the points for cropped image
    left = width / 2 - x / 2
    top = height / 2 - y / 2
    right = width / 2 + x / 2
    bottom = height / 2 + y / 2
     
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    newsize = (x, y)
    im1 = im1.resize(newsize)
     
    # Shows the image in image viewer
    im1.show()
    return im1

def takePhotoInterval():
    emptyOLED()
    writeText('Picture time!',1)
    writeText('Specify dt in min',2)
    writeText('',3)
    writeText('',4)
    num = 0
    num_final = 0
    nPress = 0
    while True:
        prev_num = num
        prev_nPress = nPress
        num, nPress = numpadInput(prev_num,prev_nPress)
        if num == 12:
            writeText('Time set to:',1)
            writeText(f'{num_final} minutes',2)
            break
        else:
            if num == 11:
                num = 0
            elif num == 10:
                pass
            num_final = num_final*10 + num
            writeText(f'{num_final} minutes',2)
    writeText('Time set!',3)
    sleep(1)
    # start to take pictures every num_final
    filename_start = 'shot'
    n = 0
    t0 = datetime.now()
    t_interval_sec = num_final*60
    print('start time:')
    print(t0)
    sleep(1)
    while True:
        dt = datetime.now() - t0
        if dt.total_seconds() >= t_interval_sec:
            filename = filename_start + {dt.strftime("%H%M%S")}
            camera.capture(filename)
        try:
            #https://medium.com/@chaoren/how-to-timeout-in-python-726002bf2291
        

def videoFeed():
#'direct' feed on OLED screen:
    active = True
    count = 0
    vf_num = 0
    filename = 'vid.jpg'
    print('f')
    while active:
        count += 1
        vf_num = numpadInput()
        print('a')
        print(count)
        if count >= 100:
            active = False
            break
        elif vf_num == 10:
            active = False
            print('videoFeed ended by numpad')
            sleep(1)
            break
        else:
            print('c')
            camera.capture(filename)
            image = Image.open(filename).convert('1')
            oled.image(image)
            oled.show()
    print('e')
    emptyOLED()
    return True
