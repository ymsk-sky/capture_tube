# -*- coding: utf-8 -*-

import cv2

video = cv2.VideoCapture('test.mp4')
if not video.isOpened():
    return

fps = int(video.get(cv2.CAP_PROP_FPS))

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 境界検出
    contours = cv2.findContours()

video.release()
cv2.destroyAllWindows()
