import numpy as np
import cv2

img = cv2.imread("hh.png")

img_size = img.shape[0]
border_size = 15
cell_size = int((img_size-2*border_size)/8)
cutted_img_size = cell_size + border_size
cutted = img[border_size:cutted_img_size, border_size:cutted_img_size]

attached = np.copy(img)
attached[border_size+2*cell_size:border_size+3*cell_size, border_size:cutted_img_size] = cutted
attached[border_size+3*cell_size:border_size+4*cell_size, border_size:cutted_img_size] = cutted

cv2.imshow("original", img)
cv2.imshow("cutted", cutted)
cv2.imshow("attached", attached)

cv2.imwrite("original.png", img)
cv2.imwrite("attached.png", attached)

cv2.waitKey(0)
cv2.destroyAllWindows()