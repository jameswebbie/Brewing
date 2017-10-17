import time
import os
import glob

def get_temp():
    
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    fo = open("/sys/bus/w1/devices/28-0316a360e3ff/w1_slave", "r")
    line = fo.read(100)
    fo.close()

    index = line.find('crc') + 7
    valid = line[index : index + 3]

    if (valid == 'YES'):
        index = line.find('t=') + 2
        return int(line[index:].strip()) / 1000
        
    else:
        return -1

