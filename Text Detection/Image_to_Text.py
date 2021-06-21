# Importing Libraries
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Reading Image
img = cv2.imread('1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detecting Characters and printing in console
print(pytesseract.image_to_string(img))

# Displaying the output image
cv2.imshow('Result', img)
cv2.waitKey(0)
