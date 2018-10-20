

import serial
import time
import os
import testcan
from flask import Flask

app = Flask(__name__)
@app.route("/output")
def output():
    os.system("start webcam.html")
for  i in range(100):
    if(i%100 == 0):
        os.system("start webcam.html")
        testcan.prediction()
