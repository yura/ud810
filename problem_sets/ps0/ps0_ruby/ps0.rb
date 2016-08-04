#!/usr/bin/env ruby
require 'opencv'
include OpenCV

# Problem Set 0: Images as Functions
# https://docs.google.com/document/d/1PO9SuHMYhx6nDbB38ByB1QANasP1UaEiXaeGeHmp3II/pub


# 1: Input images

# a. Find two interesting images to use. They should be color, rectangular in shape (NOT square). Pick one that is wide and one tall.
#    You might find some classic vision examples here. Or take your own. Make sure the image width or height do not exceed 512 pixels.
#    Output: Store the two images as ps0-1-a-1.png and ps0-1-a-2.png inside the output folder

img1 = CvMat.load('input/girl.png', CV_LOAD_IMAGE_COLOR)
img1.save_image('output/ps0-1-a-1.png')

img2 = CvMat.load('input/fruits.png', CV_LOAD_IMAGE_COLOR)
img2.save_image('output/ps0-1-a-2.png')


# 2: Color  planes

# a. Swap the red and blue pixels of image 1
#    Output: Store as ps0-2-a-1.png in the output folder
img1_blue, img1_green, img1_red = img1.split
swapped = Cv.merge([ img1_red, img1_green, img1_blue ])
swapped.save('output/ps0-2-a-1.png')

# b. Create a monochrome image (img1_green) by selecting the green channel of image 1
#    Output: ps0-2-b-1.png
img1_green.save("output/ps0-2-b-1.png")

# c. Create a monochrome image (img1_red) by selecting the red channel of image 1
#    Output: ps0-2-c-1.png
img1_red.save("output/ps0-2-c-1.png")

# 3: Replacement of pixels (Note: For this, use the better channel from 2-b/2-c as monochrome versions.)

# a. Take the inner center square region of 100x100 pixels of monochrome version of image 1 and insert them into the center of monochrome version of image 2
#    Output: Store the new image created as ps0-3-a-1.png
width = img1.cols
height = img1.rows
x_offset = (width - 100) / 2
y_offset = (height - 100) / 2

img_with_center = img1_green.clone
(0...100).each do |i|
  (0...100).each do |j|
    img_with_center[i + y_offset, j + x_offset] = img1_red[i + y_offset, j + x_offset]
  end
end

img_with_center.save("output/ps0-3-a-1.png")

# 4: Arithmetic and Geometric operations

# a. What is the min and max of the pixel values of img1_green? What is the mean? What is the standard deviation?  And how did you compute these?

# Min
green_pixels = (0...img1_green.rows).map { |i| (0...img1_green.cols).map { |j| img1_green[i,j][0] } }.flatten
green_min = green_pixels.min
puts "Min: #{green_min}"

# Max
green_max = green_pixels.max
puts "Max: #{green_max}"

# To have possibility to calculate mean and standard deviation, better to path Enumerable module:
require './enumerable_patch'

# Mean

green_mean = green_pixels.mean
puts "Mean: #{green_mean}"

# Standard deviation

green_std = green_pixels.standard_deviation
puts "Standard deviation: #{green_std}"

# b. Subtract the mean from all pixels, then divide by standard deviation, then multiply by 10 (if your image is 0 to 255) or by 0.05 (if your image ranges from 0.0 to 1.0). Now add the mean back in.
#    Output: ps0-4-b-1.png
all_pixels = (0...img1.rows).map { |i| (0...img1.cols).map { |j| img1[i,j].to_a[0..2] } }.flatten
mean = all_pixels.mean
std = all_pixels.standard_deviation

puts "All mean: #{mean}"
puts "All std: #{std}"

# looks like ruby-opencv has a bug:
# https://github.com/ruby-opencv/ruby-opencv/issues/82
(img1 - mean).save("output/test.png")

#((img1 - mean) / std * 10 + mean).save("output/ps0-4-b-1.png")

=begin
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

=end
