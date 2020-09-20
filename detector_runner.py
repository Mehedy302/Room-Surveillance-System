from PIL import Image
from camera_opencv import Camera
import time
from ObjectDetector import Detector
detector = Detector()
 
while(True):
    try: 
        file = Image.open("img.jpg")
         
         
        img = detector.detectObject(file)
        print("Notification sent Successfully")
        time.sleep(3) 
    except:
        print("Something went wrong!!!The system is restarting.")
        time.sleep(3)

          
     