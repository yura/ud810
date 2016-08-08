/*
  Problem Set 0: Images as Functions
  https://docs.google.com/document/d/1PO9SuHMYhx6nDbB38ByB1QANasP1UaEiXaeGeHmp3II/pub
*/

#include <opencv2/core/core.hpp>
#include "opencv2/imgproc/imgproc.hpp"
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

  /*
   4: Arithmetic and Geometric operations

   a. What is the min and max of the pixel values of img1_green? What is the mean? What is the standard deviation?  And how did you compute these?
   */

  // Min and max
  double min, max;
  minMaxLoc(img1_green, &min, &max);

  cout << "Min: " << min << endl;
  cout << "Max: " << max << endl;

  // Mean & standard deviation
  Scalar green_mean, green_std;
  meanStdDev(img1_green, green_mean, green_std);

  cout << "Mean: " << green_mean[0] << endl;
  cout << "Standard deviation: " << green_std[0] << endl;

  /*
   b. Subtract the mean from all pixels, then divide by standard deviation, then multiply by 10 (if your image is 0 to 255) or by 0.05 (if your image ranges from 0.0 to 1.0). Now add the mean back in.
      Output: ps0-4-b-1.png
   */
  Scalar all_mean, all_std;
  Mat calculated;
  meanStdDev(img1, all_mean, all_std);

  calculated = (img1 - all_mean) / all_std[0] * 10 + all_mean;
  // TODO: result is differ from octave and python
  //       1. check pixels at given position
  //       2. convert to double http://stackoverflow.com/questions/14539498/change-type-of-mat-object-from-cv-32f-to-cv-8u
  imwrite("output/ps0-4-b-1.png", calculated);

  /* 
   c. Shift img1_green to the left by 2 pixels.
      Output: ps0-4-c-1.png
   */

  /*
  // TODO: can't do that with filter2D
  Mat shiftedGreen;
  Mat kernel = Mat::zeros(5, 5, CV_8U);
  kernel.at<uchar>(2,4) = 1;
  cv::filter2D(img1_green, shiftedGreen, CV_8U, kernel);
  */

  Mat shiftFilter = (Mat_<double>(2, 3) << 1, 0, -2,
                                         0, 1, 0);
  Mat shiftedGreen;
  warpAffine(img1_green, shiftedGreen, shiftFilter, Size(width, height));

  imwrite("output/ps0-4-c-1.png", shiftedGreen);

  /*
   d. Subtract the shifted version of img1_green from the original, and save the difference image.
      Output: ps0-4-d-1.png (make sure that the values are legal when you write the image so that you can see all relative differences), text response: What do negative pixel values mean anyways?
   */
  Mat diff;
  diff = (img1_green - shiftedGreen) + (shiftedGreen - img1_green);
  imwrite("output/ps0-4-d-1.png", diff);

  /* 
   5: Noise

   a. Take the original colored image (image 1) and start adding Gaussian noise to the pixels in the green channel. Increase sigma until the noise is somewhat visible.
      Output: ps0-5-a-1.png, text response: What is the value of sigma you had to use?
   */
  Mat noised_green = img1.clone();
  noised_green.convertTo(noised_green, CV_64F);
  split(noised_green, channels);

  Mat noise(img1.size(), CV_64F);
  randn(noise, 0, 7);

  channels[1] += noise;

  merge(channels, 3, noised_green);

  imwrite("output/ps0-5-a-1.png", noised_green);

  /*
   b. Now, instead add that amount of noise to the blue channel.
      Output: ps0-5-b-1.png
   */
  Mat noised_blue = img1.clone();
  noised_blue.convertTo(noised_blue, CV_64F);
  split(noised_blue, channels);
  channels[0] += noise;
  merge(channels, 3, noised_blue);

  imwrite("output/ps0-5-b-1.png", noised_blue);

  return 0;
}
