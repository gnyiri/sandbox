project(serialization-examples)

cmake_minimum_required(VERSION 3.9)

set(CMAKE_PREFIX_PATH
  "${CMAKE_PREFIX_PATH}:\
  /packages/protobuf-install/:\
  /packages/googletest-install/")

find_package(Protobuf REQUIRED)

set(GTEST_ROOT "/packages/googletest-install/")
find_package(GTest REQUIRED)

message(STATUS ${PROTOBUF_INCLUDE_DIR})
message(STATUS ${PROTOBUF_LIBRARIES})
message(STATUS ${GTEST_BOTH_LIBRARIES})

