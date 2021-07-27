import cv2 as cv
import numpy as np
import os as os
img_dog = cv.imread('photos/dog.jpg')

# image dimensions (in pixels)
dimensions = img_dog.shape

# image height, width, number of channels
height = img_dog.shape[0]
width = img_dog.shape[1]
channels = img_dog.shape[2]

print("\nMetadata (Note: Number of Channels (3) represent RGB channels.):")
print("Dimensions: ", dimensions)
print("Height: ", height)
print("Width: ", width)
print("Channels: ", channels)

# imshow() takes 2 args: name of window to display and matrix of pixels to display
# Note: image displayed in new window
cv.imshow('Dog1', img_dog)
# time in milliseconds for any key press (0 = infinite amount of time)
cv.waitKey(0)