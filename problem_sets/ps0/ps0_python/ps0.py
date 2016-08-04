#!/usr/bin/env python

import cv2

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
x_offset = (w - 100)/2;
y_offset = (h - 100)/2;

center = img1_red[y_offset:y_offset+100, x_offset:x_offset+100]
img_with_center = img1_green;
img_with_center(y_offset:y_offset+100, x_offset:x_offset+100) = center;
imwrite(img_with_center, "output/ps0-3-a-1.png");

'''
% 4: Arithmetic and Geometric operations

% a. What is the min and max of the pixel values of img1_green? What is the mean? What is the standard deviation?  And how did you compute these?

% Min

%{
% DIY version
values = img1_green(:);
green_min = values(1);
for i = values(2:1:end)';
  if (i < green_min)
    green_min = i
  endif
endfor
green_min
%}

% Lib call
green_min = min(img1_green(:));
disp("Min: "), disp(green_min);

% Max

%{
% DIY version
values = reshape(img1_green, 1, []);
green_max = values(1);
for i = values(2:1:end);
  if (i > green_max)
    green_max = i;
  endif
endfor
%}

% Lib call
green_max = max(img1_green(:));
disp("Max: "), disp(green_max);

% Mean

%{
% DIY version
green_mean = sum(img1_green(:))/length(img1_green(:));
%}

% Lib call
green_mean = mean(img1_green(:));
disp("Mean: "), disp(green_mean);

% Standard deviation

% Lib call
green_std = std(img1_green(:));
disp("Standard deviation: "), disp(green_std);

% b. Subtract the mean from all pixels, then divide by standard deviation, then multiply by 10 (if your image is 0 to 255) or by 0.05 (if your image ranges from 0.0 to 1.0). Now add the mean back in.
%    Output: ps0-4-b-1.png
imwrite(((img1 - mean(img1(:))) / std(img1(:)) * 10 + mean(img1(:))), "output/ps0-4-b-1.png");
disp("All mean:"), disp(mean(img1(:)));
disp("All std:"), disp(std(img1(:)));
imwrite(img1 - mean(img1(:)), 'output/test.png');

% c. Shift img1_green to the left by 2 pixels.
%    Output: ps0-4-c-1.png
shift_filter = zeros(5, 5);
shift_filter(3, 5) = 1;

pkg load image;
shifted_green = imfilter(img1_green, shift_filter);
imwrite(shifted_green, "output/ps0-4-c-1.png");

% d. Subtract the shifted version of img1_green from the original, and save the difference image.
%    Output: ps0-4-d-1.png (make sure that the values are legal when you write the image so that you can see all relative differences), text response: What do negative pixel values mean anyways?
imwrite(((img1_green - shifted_green) + (shifted_green - img1_green)) , "output/ps0-4-d-1.png");

% 5: Noise

% a. Take the original colored image (image 1) and start adding Gaussian noise to the pixels in the green channel. Increase sigma until the noise is somewhat visible.
%    Output: ps0-5-a-1.png, text response: What is the value of sigma you had to use?
noised_green = img1;
noise = randn(size(img1_green)) * 7;
noised_green(:,:,2) += noise;
imwrite(noised_green, 'output/ps0-5-a-1.png');

% b. Now, instead add that amount of noise to the blue channel.
%    Output: ps0-5-b-1.png
noised_blue = img1;
noised_blue(:,:,3) += noise;
imwrite(noised_blue, 'output/ps0-5-b-1.png');

% c. Which looks better? Why?
%    Output: Text response
'''
