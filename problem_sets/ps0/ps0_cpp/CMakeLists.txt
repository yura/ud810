cmake_minimum_required(VERSION 2.8)
project( ps0 )
set ( OpenCV_DIR   "/Users/yura/tools/opencv-3.1.0/build")
find_package( OpenCV 3.0 REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( ps0 ps0.cpp )
target_link_libraries( ps0 ${OpenCV_LIBS} )

