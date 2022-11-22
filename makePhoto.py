from picamera import PiCamera
import datetime

photosPath = "./photos/"

def makePhoto(path = photosPath):
    camera = PiCamera()
    fileName = "/" + path + str(datetime.datetime.now()) + ".jpg"
    camera.capture(fileName)
    return fileName