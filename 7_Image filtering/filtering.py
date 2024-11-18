import cv2
import sys
import numpy as np
import os

os.environ['QT_QPA_PLATFORM'] = 'xcb'
PREVIEW = 0 
BLUR = 1
FEATURES = 2 
CANNY = 3

feature_params = dict(maxCorners = 500, qualityLevel = 0.2, minDistance = 15, blockSize = 9)

s = 0

if len(sys.argv) > 1:
    s = sys.argv[1]

image_filter = PREVIEW
alive = True

win_name = 'Camera Filters'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(s)

while alive and cv2.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)