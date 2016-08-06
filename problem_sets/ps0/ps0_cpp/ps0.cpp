#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
    Mat img1, img2;
    img1 = imread("input/girl.png", CV_LOAD_IMAGE_COLOR);
    img2 = imread("input/fruits.png", CV_LOAD_IMAGE_COLOR);

    imwrite("output/ps0-1-a-1.png", img1);
    imwrite("output/ps0-1-a-2.png", img2);

    return 0;
}
