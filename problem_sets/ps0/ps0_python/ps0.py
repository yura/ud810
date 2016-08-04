#!/usr/bin/env python

import cv2
import numpy as np

# Problem Set 0: Images as Functions
# https://docs.google.com/document/d/1PO9SuHMYhx6nDbB38ByB1QANasP1UaEiXaeGeHmp3II/pub

# 1: Input images

# a. Find two interesting images to use. They should be color, rectangular in shape (NOT square). Pick one that is wide and one tall.
#    You might find some classic vision examples here. Or take your own. Make sure the image width or height do not exceed 512 pixels.
#    Output: Store the two images as ps0-1-a-1.png and ps0-1-a-2.png inside the output folder
img1 = cv2.imread("input/girl.png")
cv2.imwrite("output/ps0-1-a-1.png", img1)

img2 = cv2.imread("input/fruits.png")
cv2.imwrite("output/ps0-1-a-2.png", img2)

# 2: Color  planes

# a. Swap the red and blue pixels of image 1
#    Output: Store as ps0-2-a-1.png in the output folder

img1_blue, img1_green, img1_red = cv2.split(img1)
swapped = cv2.merge((img1_red, img1_green, img1_blue))
cv2.imwrite("output/ps0-2-a-1.png", swapped)

# b. Create a monochrome image (img1_green) by selecting the green channel of image 1
#    Output: ps0-2-b-1.png
cv2.imwrite("output/ps0-2-b-1.png", img1_green)

# c. Create a monochrome image (img1_red) by selecting the red channel of image 1
#    Output: ps0-2-c-1.png
cv2.imwrite("output/ps0-2-c-1.png", img1_red)

# 3: Replacement of pixels (Note: For this, use the better channel from 2-b/2-c as monochrome versions.)

# a. Take the inner center square region of 100x100 pixels of monochrome version of image 1 and insert them into the center of monochrome version of image 2
#    Output: Store the new image created as ps0-3-a-1.png
height, width = img1.shape[:2]
x_offset = (width - 100)/2;
y_offset = (height - 100)/2;

img_with_center = img1_green.copy()
center = img1_red[y_offset:y_offset+100, x_offset:x_offset+100]
img_with_center[y_offset:y_offset+100, x_offset:x_offset+100] = center
cv2.imwrite("output/ps0-3-a-1.png", img_with_center)

# 4: Arithmetic and Geometric operations

# a. What is the min and max of the pixel values of img1_green? What is the mean? What is the standard deviation?  And how did you compute these?

# Min
green_min = img1_green.min()
print("Min: ", green_min)

# Max
green_max = img1_green.max()
print("Max: ", green_max)

# Mean
green_mean = img1_green.mean()
print("Mean: ", green_mean)

# Standard deviation
green_std = img1_green.std()
print("Standard deviation: ", green_std)

# b. Subtract the mean from all pixels, then divide by standard deviation, then multiply by 10 (if your image is 0 to 255) or by 0.05 (if your image ranges from 0.0 to 1.0). Now add the mean back in.
#    Output: ps0-4-b-1.png
calculated = (img1 - img1.mean()) / img1.std() * 10 + img1.mean()
# it looks better than octave's result because it casts type to float64
cv2.imwrite("output/ps0-4-b-1.png", calculated)

# c. Shift img1_green to the left by 2 pixels.
#    Output: ps0-4-c-1.png
# TODO: how to use filter2D to shift?
#shift_filter = np.zeros((5, 5), np.uint8)
#shift_filter[2, 4] = 1
#shifted_green = cv2.filter2D(img1_green, -1, shift_filter)
#cv2.imwrite("output/ps0-4-c-1.png", shifted_green)

shift_filter = np.float32([[1, 0, -2], [0, 1, 0]])
shifted_green = cv2.warpAffine(img1_green, shift_filter, (width, height))
cv2.imwrite("output/ps0-4-c-1.png", shifted_green)

# d. Subtract the shifted version of img1_green from the original, and save the difference image.
#    Output: ps0-4-d-1.png (make sure that the values are legal when you write the image so that you can see all relative differences), text response: What do negative pixel values mean anyways?

# TODO: can't just (img1_green - shifted_green) + (shifted_green - img1_green)?
diff = np.zeros(img1_green.shape, np.uint8)
for i in range(height):
  for j in range(width):
    if img1_green[i][j] > shifted_green[i][j]:
      diff[i][j] = img1_green[i][j] - shifted_green[i][j]
    else:
      diff[i][j] = shifted_green[i][j] - img1_green[i][j]

cv2.imwrite("output/ps0-4-d-1.png", diff)

# 5: Noise

# a. Take the original colored image (image 1) and start adding Gaussian noise to the pixels in the green channel. Increase sigma until the noise is somewhat visible.
#    Output: ps0-5-a-1.png, text response: What is the value of sigma you had to use?
noised_green = np.array(img1.copy(), dtype=np.float64)
noise = np.random.normal(0, 1, img1_green.shape[:2]) * 7
noised_green[:, :, 1] += noise
cv2.imwrite('output/ps0-5-a-1.png', noised_green)

# b. Now, instead add that amount of noise to the blue channel.
#    Output: ps0-5-b-1.png
noised_blue = np.array(img1.copy(), dtype=np.float64)
noised_blue[:, :, 0] += noise
cv2.imwrite('output/ps0-5-b-1.png', noised_blue)

# c. Which looks better? Why?
#    Output: Text response
