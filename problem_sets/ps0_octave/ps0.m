% Q1: Input images
%
% a. Output: Store the two images as ps0-1-a-1.png and ps0-1-a-2.png 
%    inside the output folder
image1 = imread("input/girl.png");
imwrite(image1, "output/ps0-1-a-1.png");

image2 = imread("input/fruits.png");
imwrite(image2, "output/ps0-1-a-2.png");

% Q2: Color  planes
%
% a. Swap the red and blue pixels of image 1
%    Output: Store as ps0-2-a-1.png in the output folder
swapped = image1;
red = swapped(:, :, 1);
blue = swapped(:, :, 3);
swapped(:, :, 1) = blue;
swapped(:, :, 3) = red;
imwrite(swapped, "output/ps0-2-a-1.png");