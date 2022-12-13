# AI-project

## General description
This project is an Self driving car designed to drive around user created tracks (basicly adhesive tape slapped onto the floor) based on raspberry pi and tensorflow CNN network.

## Parts used
1. Raspberry Pi 4B
2. 7" LCD Screen
3. PiCamera V2
4. Generic USB speaker
5. L298N Two channel motor driver
6. 4 Motors powered by 9V batteries
7. Redmi 18W Fast powerbank 2A 5V
8. bodykit + wheels

## Setup
If you wish to train your own model you should follow these steps:
1. Run circuitSampling.py and drive through your track a couple of times. The more tracks and more sessions on each track the more accurate the model will be!

circuitSampling.py commands:
- w -> drive forward
- a -> turn left
- d -> turn right
- z -> save session

2. After saving your sessions run the jupyter notebook in the model_training dir to train the model.
3. The model should be saved in the model directory
4. Run the autodrive.py to let the beast loose
