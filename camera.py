import cv2
import numpy as np
import torch
from yolov5.detect import run
                
model = torch.hub.load('yolov5','custom', path='model.pt', force_reload=True, source='local')
model.conf = 0.35  # confidence threshold (0-1)

class VideoCamera(object):
    def __init__(self):
       # Setting Video captyure to be webcam
        self.video = cv2.VideoCapture(2)

    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()

        # Passing image into the model and reciving results
        results = model(image)
        a = np.squeeze(results.render())

        # Encode the result image as JPEG
        ret, jpeg = cv2.imencode('.jpg', image)

        # Return the JPEG bytes
        return jpeg.tobytes()