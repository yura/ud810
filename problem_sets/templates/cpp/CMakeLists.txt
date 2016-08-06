cmake_minimum_required(VERSION 2.8)
project( <ps#> )
set ( OpenCV_DIR   "/Users/yura/tools/opencv-3.1.0/build")
find_package( OpenCV 3.0 REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( <ps#> <ps#>.cpp )
target_link_libraries( <ps#> ${OpenCV_LIBS} )

