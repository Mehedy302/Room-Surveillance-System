from ObjectDetector import Detector
from PIL import Image
from camera_opencv import Camera
import time
from ObjectDetector import Detector
 
import io
from PIL import Image
from flask import send_file
from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine, Document
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, Length, InputRequired
from werkzeug.security import generate_password_hash, check_password_hash
import numpy as np
import cv2
import threading
import atexit
import os
from termcolor import colored
import ctypes
LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11


from importlib import import_module
import os
os.system('set CAMERA=opencv')
from flask import Flask, render_template, Response,request, redirect
 
# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera
 
app = Flask(__name__)

detector = Detector()




os.system('cls')

os.system('cls')
os.system('cls')
 

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
os.system('mode con: cols=63 lines=30')
os.system('color')
print(colored('______________________________________________________________\n','red'))
print(colored('##############################################################\n','green'))
font.dwFontSize.X = 11
font.dwFontSize.Y = 18
font.FontFamily = 54
font.FontWeight = 1000
font.FaceName = "Lucida Console"
 

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(True), ctypes.pointer(font))
print('\x1b[6;30;42m' + '              WELCOME TO HOME SERVALANCE SYSTEM                ' + '\x1b[0m '+'\n')
print(colored('##############################################################\n','green'))
print(colored('______________________________________________________________\n','red'))
print('\n')

f = open("email.txt", "r")
email = f.read()
print(colored('Now You Are Using Email Address : ','green')+colored(email,'red'))
f.close()

 
choice = input(colored('Do You Want To Change Your Email ? ','red')+'('+colored('y','red')+'/'+colored('n','green')+')'+' : ')

flag = True
while(flag): 
    if choice=='y':
        email = input(colored('Enter Your Email : ','green'))
        f = open("email.txt","w")
        f.write(email)
        f.close()
        flag = False
    elif choice=='n':
        print(colored('Server Will Start Using : ','green')+colored(email,'red'))
        flag = False
    else:
        choice = input(colored('Please Select The Correct Input : ','red'))


print('\n\n')

 



@app.route("/")
def upload():
        while(True):
              
            
            img = detector.detectObject(Image.open("img.jpg"))
            
            return send_file(io.BytesIO(img),attachment_filename='image.jpg',mimetype='image/jpg')
            



@app.route('/live')

def index():
    """Video streaming home page."""
    
 
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
     
    while True:
 
         
         
        frame = camera.get_frame()
        
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
 
         

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


 


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True,debug=True)
         







        
    

    

 

 