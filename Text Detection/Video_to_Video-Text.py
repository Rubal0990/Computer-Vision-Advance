# Importing Libraries
import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract

# Reading video
cap = cv2.VideoCapture(0)

# Resize video window
cap.set(3, 640)
cap.set(4, 480)


# User-defined function to capture a screen
def captureScreen(bbox=(300, 300, 1500, 1000)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr


while True:
    timer = cv2.getTickCount()
    _, img = cap.read()

    # Detecting Characters
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
        cv2.putText(img, b[0], (x, hImg - y + 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    # Displaying the output video
    cv2.imshow("Result", img)
    cv2.waitKey(1)
