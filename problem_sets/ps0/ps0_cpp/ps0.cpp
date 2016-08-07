/*
  Problem Set 0: Images as Functions
  https://docs.google.com/document/d/1PO9SuHMYhx6nDbB38ByB1QANasP1UaEiXaeGeHmp3II/pub
*/

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
  /*
   1: Input images

   a. Find two interesting images to use. They should be color, rectangular in shape (NOT square). Pick one that is wide and one tall.
      You might find some classic vision examples here. Or take your own. Make sure the image width or height do not exceed 512 pixels.
      Output: Store the two images as ps0-1-a-1.png and ps0-1-a-2.png inside the output folder
   */

  Mat img1, img2;
  img1 = imread("input/girl.png", CV_LOAD_IMAGE_COLOR);
  img2 = imread("input/fruits.png", CV_LOAD_IMAGE_COLOR);

  imwrite("output/ps0-1-a-1.png", img1);
  imwrite("output/ps0-1-a-2.png", img2);

  /*
   2: Color  planes

   a. Swap the red and blue pixels of image 1
      Output: Store as ps0-2-a-1.png in the output folder
   */

  Mat channels[3];
  Mat img1_red, img1_green, img1_blue, swapped;

  split(img1, channels);
  img1_red = channels[2];
  img1_green = channels[1];
  img1_blue = channels[0];

  channels[0] = img1_red;
  channels[2] = img1_blue;

  merge(channels, 3, swapped);
  imwrite("output/ps0-2-a-1.png", swapped);

  /*
   b. Create a monochrome image (img1_green) by selecting the green channel of image 1
      Output: ps0-2-b-1.png
   */
  imwrite("output/ps0-2-b-1.png", img1_green);

  /*
   c. Create a monochrome image (img1_red) by selecting the red channel of image 1
      Output: ps0-2-c-1.png
   */
  imwrite("output/ps0-2-c-1.png", img1_red);

  /*
   3: Replacement of pixels (Note: For this, use the better channel from 2-b/2-c as monochrome versions.)

   a. Take the inner center square region of 100x100 pixels of monochrome version of image 1 and insert them into the center of monochrome version of image 2
      Output: Store the new image created as ps0-3-a-1.png
   */
  int height = img1.rows;
  int width = img1.cols;
  int x_offset = (width - 100)/2;
  int y_offset = (height - 100)/2;

  Rect rect(x_offset, y_offset, 100, 100);
  Mat img_with_center = img1_green.clone();
  Mat center(img1_red, rect);

  center.copyTo(img_with_center(rect));

  imwrite("output/ps0-3-a-1.png", img_with_center);

  return 0;
}
