# -*- coding: utf-8 -*-

import cv2
import sys

src = 'test.mp4'
video = cv2.VideoCapture(src)
if not video.isOpened():
    sys.exit()

fps = int(video.get(cv2.CAP_PROP_FPS))

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    pass

    key = cv2.waitKey(fps)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
