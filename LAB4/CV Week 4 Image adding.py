import numpy as np
import cv2

# Load an color image in grayscale
img1 = cv2.imread('sample1.jpg', 1)
img2 = cv2.imread('sample2.jpg', 1)

# addWeighted

dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow('dst', dst)

# adding two photos
AddedPhoto = img1 + img2
cv2.imshow('AddedPhoto', AddedPhoto)

# removing one photo from other
RemovedPhoto = img1 - img2
cv2.imshow('RemovedPhoto', RemovedPhoto)

cv2.waitKey(0)
cv2.destroyAllWindows()
