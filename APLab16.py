import cv2 as cv
import matplotlib.pyplot as pp
import sys
img = cv.imread(r"C:\Users\miriy\OneDrive\Pictures\Camera Roll\WIN_20221120_19_54_25_Pro.jpg",1)
if img is None:
 sys.exit("Could not read the image.")
cv.imshow(r"Image",img)