#!/usr/bin/env python

"""
    A Simple template code that demonstrates video stream input
    output
"""
import numpy as np
import cv2

# For web-cam:
#video_capture = cv2.VideoCapture(0) 

# For videos:
video_capture = cv2.VideoCapture('videos/tennis-ball-video.mp4')

while True:
    ret, frame = video_capture.read()
    cv2.imshow("Video-Frame", frame)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()