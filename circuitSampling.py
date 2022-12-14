from picamera import PiCamera
from motor import forward, backward, left, right, stop, sleepWithStop
from makePhoto import makePhoto
import json
import os

camera = PiCamera()

seqJson = {"sequence": []}

sequencesPath = "./sequences/"

if(os.path.exists(sequencesPath) == False):
  os.mkdir(sequencesPath)

currentSeqPath = sequencesPath + "sequence_" + str(len(next(os.walk(sequencesPath))[1])+1) + "/"
os.mkdir(currentSeqPath)

while 1:
    cmd = input()
    print(cmd)
    print(seqJson["sequence"])
    currentIteration = {}
    currentIteration["photo"] = makePhoto(currentSeqPath, camera)
    if(cmd == 'w'):
        currentIteration["action"] = 'forward'
        forward()
        sleepWithStop(1)
    if(cmd == 's'):
        currentIteration["action"] = 'backward'
        backward()
        sleepWithStop(0.5)
    if(cmd == 'a'):
        currentIteration["action"] = 'left'
        left()
        sleepWithStop(0.5)
    if(cmd == 'd'):
        currentIteration["action"] = 'right'
        right()
        sleepWithStop(0.5)
    if(cmd == 'x'):
        stop()
    if(cmd == 'z'):
        with open(currentSeqPath + "sequence.json", "w") as outfile:
          outfile.write(json.dumps(seqJson, indent=4))
        break
    seqJson["sequence"].append(currentIteration)
    