
import serial
import time
import os
from flask import Flask
import testcan

import time



#The following line is for serial over GPIO
port = 'COM9'


ard = serial.Serial(port,9600)
i = 0

f = open('data.csv', 'w')
msg =""
while (0 < 1):
    # Serial read section
    lastm = msg
    msg = ard.readline()
    msg = msg.strip()
    msg = msg.rstrip()
    msg = msg.decode()
    bool = 0
    if(i > 10):

        #f.write(msg)
        if (lastm == "n" or lastm == 'n') and (msg == 's' or msg == "s") :

            os.system("start webcam.html")
            a = testcan.prediction()
            if(not a):
                #timeout = time.time() + 1
                #while True:
                ard.write(b'c')
                    #print("c")
                    #if(time.time() > timeout):
                        #break;

                bool = 1
            i = -50
        print(msg,lastm)
    i = i + 1
    if(bool == 0):
        ard.write(b'd')



else:
    print ("Exiting")
    f.close()



exit()
