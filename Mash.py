import Read_therm
import time
import os

def child(pipeout):
    while (1):
        newTemp = 'trial'
#       newTemp = input('new temp?')
        print('child')
        os.write(pipeout, newTemp)
#       time.sleep(1)

def parent(pipein):
    while(1):
        print('adult')
        data = os.read(pipein, 20)
      
        if (data):
            print(data)
        # reqTemp = int(data);

        currTemp = Read_therm.get_temp();
#        if (reqTemp < currTemp):
            
        time.sleep(1)
        



reqTemp = 0
# reqTemp = int(input('Enter Mash Temp '))

rpipe, wpipe = os.pipe()

newPID = os.fork()
data = 0
# CHILD
if newPID == 0:
    child(wpipe)
    
# PARENT
else:
    parent(rpipe)
    
