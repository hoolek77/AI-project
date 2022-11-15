from picamera import PiCamera
from time import sleep
import datetime
import os
from rekognition import recognize_img
from tts import speak

camera = PiCamera()
lastPhotos = []

while( True ):
    if(len(lastPhotos) >=10):
        os.remove(lastPhotos[0])
        lastPhotos.pop(0)
    
    fileName = "./" + str(datetime.datetime.now()) + ".jpg"
    lastPhotos.append(fileName)
    camera.capture(fileName)
    
    result = recognize_img(fileName)
    print(result)
    for res in result:
        speak(res)

    sleep(5)
