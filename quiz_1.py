import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('test_image.jfif')

# Separate the RGB channels
b,g,r = cv2.split(img)

# Calculate the histograms
hist_r = cv2.calcHist([r],[0],None,[256],[0,256])
hist_g = cv2.calcHist([g],[0],None,[256],[0,256])
hist_b = cv2.calcHist([b],[0],None,[256],[0,256])

# Plot the histograms
plt.subplot(2,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(2,2,2)
plt.plot(hist_r, color='r')
plt.title('Red Channel Histogram')

plt.subplot(2,2,3)
plt.plot(hist_g, color='g')
plt.title('Green Channel Histogram')

plt.subplot(2,2,4)
plt.plot(hist_b, color='b')
plt.title('Blue Channel Histogram')

plt.tight_layout()
plt.show()

# Find the dominant color
max_r = np.argmax(hist_r)
max_g = np.argmax(hist_g)
max_b = np.argmax(hist_b)

if max_r > max_g and max_r > max_b:
    print("The dominant color is red")
elif max_g > max_r and max_g > max_b:
    print("The dominant color is green")
else:
    print("The dominant color is blue")

# Convert the image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Apply histogram equalization to the V channel
hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])

# Convert the image back to BGR color space
equalized = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Display the original and equalized images
cv2.imshow('Original', img)
cv2.imshow('Equalized', equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()