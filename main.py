import pyfirmata
from pyfirmata import Arduino,util
import time
import cv2
import numpy as np
import os

# Sensor Part
board=Arduino("COM3")
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')

time.sleep(2)
analog_value = analog_input.read()
print(analog_value)
if (analog_value<=0.3):
    camera=cv2.VideoCapture(0)
    return_value,image=camera.read()
    img_name="opencv_frame_.png".format(str(0))
    cv2.imwrite(img_name,image) 
    del(camera)
# os.remove(img_name)