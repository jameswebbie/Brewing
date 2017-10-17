import Read_therm
import RPi.GPIO as GPIO
import time

""" 5V for both Relay and Sensor
Pin 24 for Relay (9th down on right)
Pin 4 for Sensor (4th on left)
"""
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
time.sleep(5)
GPIO.setup(24, GPIO.OUT)
totalTime = 0
timeOn = 0
fridgeOn = 0
while (1):
    temp = Read_therm.get_temp()
    
    if (temp > 4):
        GPIO.output(24, 1)
        fridgeOn = 1
    elif (temp < 2):
        GPIO.output(24, 0)
        fridgeOn = 0
    
    timeOn += fridgeOn
    totalTime += 1
    stringRet = str(round(temp, 2)) + ' degrees     Duty Cycle: ' + str(round(timeOn/(totalTime)  * 100, 3)) + '%'
    print(stringRet)
    time.sleep(3 * 60)