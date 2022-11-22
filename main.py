from picamera import PiCamera
from time import sleep
import datetime
import os
from rekognition import recognize_img
from tts import speak

camera = PiCamera()
lastPhotos = []

def makePhoto():
    fileName = "./photos/" + str(datetime.datetime.now()) + ".jpg"
    camera.capture(fileName)
    return fileName

while( True ):
    if(len(lastPhotos) >=10):
        os.remove(lastPhotos[0])
        lastPhotos.pop(0)
    
    lastPhotos.append(makePhoto())
    
    result = recognize_img(lastPhotos[-1])
    print(result)
    for res in result:
        speak(res)

    sleep(5)
