cmake_minimum_required(VERSION 2.8)
project( <project_name> )
find_package( OpenCV REQUIRED )
add_executable( <project_name> <project_name>.cpp )
target_link_libraries( <project_name> ${OpenCV_LIBS} )

