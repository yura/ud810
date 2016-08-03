cmake_minimum_required(VERSION 2.8)
project( <ps#> )
find_package( OpenCV REQUIRED )
add_executable( <ps#> <ps#>.cpp )
target_link_libraries( <ps#> ${OpenCV_LIBS} )

