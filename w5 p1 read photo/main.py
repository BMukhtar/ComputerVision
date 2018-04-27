import numpy as np
import cv2

img = cv2.imread('sample.jpg', 1)

cv2.imwrite("sample_gray.jpg", img)

# print(img.shape)

scale = 0.7
small = cv2.resize(img, None, fx=scale, fy=scale)
dim = small.shape


cv2.line(small, (0, 0), (dim[1], dim[0]), (255, 0, 0), 5)

cv2.imshow("image", small)
cv2.waitKey(0)
cv2.destroyAllWindows()


