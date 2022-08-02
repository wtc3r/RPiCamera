#https://learn.adafruit.com/monochrome-oled-breakouts/python-usage-2
#https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/image.py
import board
import busio
import adafruit_ssd1306
import digitalio
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)
# to find the i2c adress use in terminal:
# i2cdetect -y 1
oled = adafruit_ssd1306.SSD1306_I2C(128,64,i2c,addr=0x3d)

WIDTH = 128
HEIGHT = 64
BORDER = 1

i2c = board.I2C()

oled.fill(0)
oled.show()

image = Image.new("1",(oled.width,oled.height))
draw = ImageDraw.Draw(image)
draw.rectangle(
    (0,0,oled.width,oled.height)
    ,outline=255,fill=255)
draw.rectangle(
    (BORDER,BORDER,oled.width-BORDER-1,oled.height-BORDER-1),
               outline=0,fill=0)

def writeText(text,line):
    font = ImageFont.load_default()
    # text = "hoi" # fits 20 characters on each line
    (font_width, font_height) = font.getsize(text)
    if line == 1:
        line_logic = 0
    elif line == 2:
        line_logic = 1
    elif line == 3:
        line_logic = 2
    elif line == 4:
        line_logic = 3
    else:
        line_logic = 0
        print('Specify a number between 1-4 for line (in writeText)')
    draw.rectangle((5
        ,2+(font_height+2)*line_logic
        ,oled.width-5
        ,2+(font_height+2)*(line_logic+1)),outline=0,fill=0)
    draw.text(
        (5, 2 + (font_height+2)*line_logic)
        ,text,font=font,fill=255)

    oled.image(image)
    oled.show()
    return image
    
def emptyOLED():
    oled.fill(0)
    oled.show()
    
def showImage(filename):
    image = Image.open(filename).resize((WIDTH,HEIGHT), Image.ANTIALIAS).convert('1')
    oled.image(image)
    oled.show()
    return image
