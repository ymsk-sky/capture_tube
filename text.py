# -*- coding: utf-8 -*-

import cv2
import sys
import numpy as np

nm1 = 'trained_classifierNM1.xml'
nm2 = 'trained_classifierNM2.xml'

src = 'test.mp4'
video = cv2.VideoCapture(src)
if not video.isOpened():
    sys.exit()

fps = int(video.get(cv2.CAP_PROP_FPS))

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    channels = cv2.text.computeNMChannels(frame)
    cn = len(channels) - 1
    for c in range(cn):
        channels.append((255 - channels[c]))

    for channel in channels:
        erc1 = cv2.text.loadClassifierNM1(nm1)
        er1 = cv2.text.createERFilterNM1(erc1, 16, 0.00015, 0.13, 0.2, True, 0.1)

        erc2 = cv2.text.loadClassifierNM2(nm2)
        er2 = cv2.text.createERFilterNM2(erc2, 0.5)

        regions = cv2.text.detectRegions(channel, er1, er2)

        rects = cv2.text.erGrouping(frame, channel, [r.tolist() for r in regions])

        for r in range(np.shape(rects)[0]):
            rect = rects[r]
            cv2.rectangle(frame, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), (0, 0, 0), 2)
            cv2.rectangle(frame, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), (255, 255, 255), 1)

    cv2.imshow('Text detection', frame)

    key = cv2.waitKey(fps)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
