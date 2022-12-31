import sys
from makePhoto import makePhoto
from motor import forward, left, right, sleepWithStop
import numpy as np
from picamera import PiCamera
from keras.models import load_model
import cv2, os

camera = PiCamera()

drivePath = "./drive/"

if(os.path.exists(drivePath) == False):
  os.mkdir(drivePath)

currentDriveSeqPath = drivePath + "drive_" + str(len(next(os.walk(drivePath))[1])+1) + "/"
os.mkdir(currentDriveSeqPath)

def img_preprocess(image):
    height, _, _ = image.shape
    image = image[int(height/2):,:,:]  # remove top half of the image, as it is not relavant for lane following
    image = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)  # Nvidia model said it is best to use YUV color space
    image = cv2.GaussianBlur(image, (3,3), 0)
    image = cv2.resize(image, (200,66)) # input image size (200,66) Nvidia model
    image = image / 255 # normalizing, the processed image becomes black for some reason.  do we need this?
    return image

model = load_model('model_training/model/lane_navigation_check_v2.h5')

def predict(image)->int:
    Y_pred = model.predict([image])
    for y in Y_pred:
        print(y)
        if (y < 1.4):
            return 1
        elif (y >= 1.4 and y < 2.4):
            return 2
        elif (y >= 2.4):
            return 3
        else:
            return int(y)

def imread(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

debug = False

if (len(sys.argv) > 1):
    arg = sys.argv[1]
    if ("debug" in arg):
        debug = True

print(f"Debug mode: {debug}")

direction = {
    1: "forward",
    2: "left",
    3: "right"
}

while 1:
    path = makePhoto(currentDriveSeqPath, camera)
    photo = img_preprocess(imread(path))
    cmd = predict(np.array([photo]))
    if (debug == True):
        debugPath = 'debug'
        if (os.path.exists(debugPath) == False):
            os.mkdir(debugPath)

        index = len(next(os.walk(debugPath))[2])
        debugPath = debugPath + "/" + str(index + 1)  + "_" + direction[cmd] + "_" + str(cmd) + ".jpg"
        camera.capture(debugPath)

    print('command: {0} = {1}'.format(cmd, direction[cmd]))
    if(cmd == 1):
        forward()
        sleepWithStop(0.5)
    if(cmd == 2):
        left()
        sleepWithStop(0.5)
    if(cmd == 3):
        right()
        sleepWithStop(0.5)
