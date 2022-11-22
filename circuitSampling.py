from motor import forward, backward, left, right, stop
from makePhoto import makePhoto
import json
import os

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
    currentIteration["photo"] = makePhoto(currentSeqPath)
    if(cmd == 'w'):
        currentIteration["action"] = 'forward'
        forward()
    if(cmd == 's'):
        currentIteration["action"] = 'backward'
        backward()
    if(cmd == 'a'):
        currentIteration["action"] = 'left'
        left()
    if(cmd == 'd'):
        currentIteration["action"] = 'right'
        right()
    if(cmd == 'x'):
        stop()
    if(cmd == 'z'):
        with open(currentSeqPath + "sequence.json", "w") as outfile:
          outfile.write(json.dumps(seqJson, indent=4))
        break
    seqJson["sequence"].append(currentIteration)
    