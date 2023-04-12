from skimage.feature import hog
import cv2
import matplotlib.p

image = cv2.imread('train.jpg')
image = cv2.resize(image, (128*4, 64*4))

fd, hog_image = hog(image, orientations=9, pixel_per_cell=(4,4), cells_per_block=(2,2), visualize=True, multichannel=True)