from motor.py import forward, backward, left, right, stop
from main.py import makePhoto
import json
from time import sleep

sequence = []

while 1:
    cmd = input()
    print(sequence)
    currentIteration = {}
    currentIteration["photo"] = makePhoto()
    if(cmd == 'w'):
        currentIteration["action"] = 'w'
        forward()
        sleep(1)
    if(cmd == 's'):
        currentIteration["action"] = 's'
        backward()
        sleep(1)
    if(cmd == 'a'):
        currentIteration["action"] = 'a'
        left()
        sleep(1)
    if(cmd == 'd'):
        currentIteration["action"] = 'd'
        right()
        sleep(1)
    if(cmd == 'z'):
        with open("./training_sets/sequence.json", "w") as outfile:
          outfile.write(json.dumps(sequence, indent=4))
    sequence.append(currentIteration)
    