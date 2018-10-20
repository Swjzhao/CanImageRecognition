
import serial
import time
import os
from flask import Flask

app = Flask(__name__)
@app.route("/output")
def output():
    os.system("start webcam.html")



#The following line is for serial over GPIO
port = 'COM9'


ard = serial.Serial(port,115200)
i = 0

f = open('data.csv', 'w')

while (i < 10000):
    # Serial read section
    msg = ard.readline()
    if(i > 1):
        print (msg)
        #f.write(msg)
    i = i + 1
else:
    print ("Exiting")
    f.close()
exit()
