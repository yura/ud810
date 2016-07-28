% Q1: Input images
%
% a. Find two interesting images to use. They should be color, rectangular in shape (NOT square). Pick one that is wide and one tall.
%    You might find some classic vision examples here. Or take your own. Make sure the image width or height do not exceed 512 pixels.
%    Output: Store the two images as ps0-1-a-1.png and ps0-1-a-2.png inside the output folder
img1 = imread("input/girl.png");
imwrite(img1, "output/ps0-1-a-1.png");

img2 = imread("input/fruits.png");
imwrite(img2, "output/ps0-1-a-2.png");

% Q2: Color  planes
%
% a. Swap the red and blue pixels of image 1
%    Output: Store as ps0-2-a-1.png in the output folder
img1_red = img1(:, :, 1);
img1_blue = img1(:, :, 3);
swapped = img1;
swapped(:, :, 1) = img1_blue;
swapped(:, :, 3) = img1_red;
imwrite(swapped, "output/ps0-2-a-1.png");

% b. Create a monochrome image (img1_green) by selecting the green channel of image 1
%    Output: ps0-2-b-1.png
img1_green = img1(:, :, 2);
imwrite(img1_green, "output/ps0-2-b-1.png");

% c. Create a monochrome image (img1_red) by selecting the red channel of image 1
%    Output: ps0-2-c-1.png
% Red channel aready got at prev part
imwrite(img1_red, "output/ps0-2-c-1.png");

% Q3: Replacement of pixels (Note: For this, use the better channel from 2-b/2-c as monochrome versions.)
%
% a. Take the inner center square region of 100x100 pixels of monochrome version of image 1 and insert them into the center of monochrome version of image 2
%    Output: Store the new image created as ps0-3-a-1.png
width = size(img1, 2);
height = size(img1, 1);
x_offset = (width - 100)/2;
y_offset = (height - 100)/2;

center = img1_red(y_offset:y_offset+100, x_offset:x_offset+100);
img1_green(y_offset:y_offset+100, x_offset:x_offset+100) = center;
imwrite(img1_green, "output/ps0-3-a-1.png");
