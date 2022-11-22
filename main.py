from time import sleep
import os
from rekognition import recognize_img
from makePhoto import makePhoto
from tts import speak

lastPhotos = []

photosPath = "./photos/"

if(os.path.exists(photosPath) == False):
  os.mkdir(photosPath)
    
while( True ):
    if(len(lastPhotos) >=10):
        os.remove(photosPath + lastPhotos[0])
        lastPhotos.pop(0)
    
    lastPhotos.append(makePhoto())
    
    result = recognize_img(lastPhotos[-1])
    print(result)
    for res in result:
        speak(res)

    sleep(5)
