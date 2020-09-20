import os
import cv2
from base_camera import BaseCamera
import time

def __init__(self, src=0):
    # initialize the video camera stream and read the first frame
    # from the stream
    print("init")
    self.stream = cv2.VideoCapture(src)
    (self.grabbed, self.frame) = self.stream.read()

    # initialize the variable used to indicate if the thread should
    # be stopped
def read(self):
    # return the frame most recently read
    return self.frame



class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')
        timei = 0      
        while True:
            # read current frame
            _, img = camera.read()
            
             
            
            # encode as a jpeg image and return it
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
            yield cv2.imencode('.jpg', img,encode_param)[1].tobytes()
            if timei % 66  == 0:
                cv2.imwrite("img.jpg", img)
            timei = timei + 1
             
