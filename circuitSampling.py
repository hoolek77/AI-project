from motor.py import forward, backward, left, right, stop
from main.py import makePhoto
import json
from time import sleep
import os

seqJson = {"sequence": []}

sequencesPath = "./sequences/"

if(os.path.exists(sequencesPath) == False):
  os.mkdir(sequencesPath)

currentSeqPath = sequencesPath + "sequence_" + str(len(next(os.walk(sequencesPath))[1])+1)
os.mkdir(currentSeqPath)

while 1:
    cmd = input()
    print(cmd)
    print(seqJson["sequence"])
    currentIteration = {}
    currentIteration["photo"] = makePhoto(currentSeqPath)
    if(cmd == 'w'):
        currentIteration["action"] = 'w'
        forward()
    if(cmd == 's'):
        currentIteration["action"] = 's'
        backward()
    if(cmd == 'a'):
        currentIteration["action"] = 'a'
        left()
    if(cmd == 'd'):
        currentIteration["action"] = 'd'
        right()
    if(cmd == 'z'):
        with open(currentSeqPath + "/sequence.json", "w") as outfile:
          outfile.write(json.dumps(seqJson, indent=4))
        break
    seqJson["sequence"].append(currentIteration)
    