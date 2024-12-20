#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import LightSensor, ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sound import Sound
from BotCode.drive import *

SPEED = -20  # negativ because the motors are mounted backwards -__-
LIGHTOFFSET = 8  # offset because sonsors are not calibrated very well by lego -__-
WALLDISTANCE = 10  # at which distance should the bot react to a wall

coursCompleted = False
eventCounter = 1  # counts to events on the track

leftSensor = LightSensor(INPUT_1)
middleSensor = LightSensor(INPUT_2)
rightSensor = LightSensor(INPUT_3)
distanceSensor = UltrasonicSensor(INPUT_4)
sound = Sound()

sound.beep()

while not coursCompleted:
    leftLight = leftSensor.reflected_light_intensity
    rightLight = rightSensor.reflected_light_intensity
    leftLightCompare = leftLight + LIGHTOFFSET
    rightLightCompare = rightLight + LIGHTOFFSET

    # we are trying to catch an error where the sensors return strings if the sun is very bright
    if type(leftLight) is not float or type(rightLight) is not float:
        print(leftLight, rightLight)

    if distanceSensor.distance_centimeters <= WALLDISTANCE and eventCounter == 1:
        turn180()
        eventCounter += 1
        continue

    if (leftLight < rightLightCompare and rightLight < leftLightCompare) and ((leftLight + rightLight) / 2) > (middleSensor.reflected_light_intensity + LIGHTOFFSET):
        forward(SPEED)
        continue
    elif rightLight > leftLightCompare:
        turnLeft(SPEED, SPEED)
        continue
    elif rightLightCompare < leftLight:
        turnRight(SPEED, SPEED)
        continue
    else:
        forward(SPEED)
        continue

# Sunaa Risu
