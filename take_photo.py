from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
#camera.resolution = (128, 32)
# camera.start_preview()

def snap(name):
#     sleep(0)
    camera.capture(name)

def snapOLED(name):
    camera.resolution = (128, 32)
    camera.capture(name)
    
def preview(time):
    sleep(1)
    camera.start_preview()
    sleep(time)
    camera.stop_preview()
    
#camera.capture('test_photo.jpg',resize=(320,240))

#camera.stop_preview()
#camera.close()
