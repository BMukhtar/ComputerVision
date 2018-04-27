import cv2
import numpy as np

img = cv2.imread('chessboard.jpg', 0)
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges3 = cv2.Canny(img,50,100,apertureSize = 3)
edges7 = cv2.Canny(img,50,100,apertureSize = 7)

cv2.imshow("Canny Edges", edges3)
cv2.imshow("Canny Edges", edges7)
cv2.waitKey(0)
cv2.destroyAllWindows()
