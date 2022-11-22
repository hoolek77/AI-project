from motor.py import forward, backward, left, right, stop
from main.py import makePhoto
import json
from time import sleep

sequence = {}

while 1:
    cmd = input()
    print(sequence)
    currentIteration = []
    currentIteration.append(makePhoto())
    if(cmd == 'w'):
        currentIteration.append('w')
        forward()
        sleep(1)
    if(cmd == 's'):
        currentIteration.append('s')
        backward()
        sleep(1)
    if(cmd == 'a'):
        currentIteration.append('a')
        left()
        sleep(1)
    if(cmd == 'd'):
        currentIteration.append('d')
        right()
        sleep(1)
    if(cmd == 'z'):
        currentIteration.append('x')
        with open("sequence.json", "w") as outfile:
          outfile.write(json.dumps(sequence, indent=4))
    sequence.append[currentIteration]
    