import cv2
import matplotlib.pyplot as plt

snow = cv2.imread("snow.jpeg", 0)
cat = cv2.imread("cat.jpg", 0)
snow = cv2.resize(snow, (600,600))
cat = cv2.resize(cat, (600,600))

print(snow.shape)
print(cat.shape)
ret, thresh = cv2.threshold(snow, 100, 255, cv2.THRESH_BINARY_INV)
#final_image = cv2.addWeighted(snow, 0.3, cat, 0.3, 0)
cv2.imshow("final_image", thresh)
cv2.waitKey(0)