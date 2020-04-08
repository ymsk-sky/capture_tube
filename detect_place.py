# -*- coding: utf-8 -*-

import cv2
import numpy as np

file = './scene.png'
img = cv2.imread(file)

# グレースケール
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ガウシアンフィルタ（境界を曖昧にする）
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# ラプラシアンフィルタで勾配検出
lap = cv2.Laplacian(blur, cv2.CV_8UC1)
# 大津の手法で二値化
_, th2 = cv2.threshold(lap, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# モルフォロジー変換（クロージング）
kernel = np.ones((20, 20), np.uint8)
closing = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel)

cv2.imshow('test', closing)

cv2.waitKey(0)

cv2.destroyAllWindows()
