# -*- coding: utf-8 -*-

import cv2
import sys

video = cv2.VideoCapture('test.mp4')
if not video.isOpened():
    sys.exit()

fps = int(video.get(cv2.CAP_PROP_FPS))

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

    # 境界検出
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for cont in contours:
        x, y, w, h = cv2.boundingRect(cont)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('', frame)

    key = cv2.waitKey(fps)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
