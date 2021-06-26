# Importing Libraries
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Reading Image
img = cv2.imread('1.png')

# Reading the file with authorized person's name
with open('myDataFile.txt') as f:
    myDataList = f.read().splitlines()

# Reading the QR-Code
for barcode in decode(img):
    myData = barcode.data.decode('utf-8')
    print(myData)

    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (255, 0, 255), 5)
    pts2 = barcode.rect
    cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (255, 0, 255), 2)

# Displaying the output Image
cv2.imshow('Result', img)
cv2.waitKey(1)
