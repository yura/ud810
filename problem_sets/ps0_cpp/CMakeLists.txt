cmake_minimum_required(VERSION 2.8)
project( ps0 )
find_package( OpenCV REQUIRED )
add_executable( ps0 ps0.cpp )
target_link_libraries( ps0 ${OpenCV_LIBS} )

