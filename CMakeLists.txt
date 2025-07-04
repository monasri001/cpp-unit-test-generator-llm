cmake_minimum_required(VERSION 3.10)
project(UnitTestGenerator)

set(CMAKE_CXX_STANDARD 17)

# Include GoogleTest
include_directories(/usr/src/googletest/googletest/include)
link_directories(/usr/src/googletest/lib)

# Add the test source file
add_executable(unit_tests tests/test_main_refined.cpp src/main.cpp)

# Link GoogleTest libraries
target_link_libraries(unit_tests gtest gtest_main pthread)
