import cv2
import numpy as np

arr = np.ones(100)
img = cv2.imread("Data\\amx.jpg")

resized = cv2.resize(img, (600, 400))

cv2.imshow("Output", resized)

if cv2.waitKey(0) & 0xFF == ord("q"):
    exit(0)
