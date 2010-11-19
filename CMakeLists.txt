cmake_minimum_required(VERSION 2.6)
PROJECT(OpenFlightWriter)

# Add path containing our custom CMake modules
SET(CMAKE_MODULE_PATH
    "${PROJECT_SOURCE_DIR}/CMakeModules;${CMAKE_MODULE_PATH}")

# Put all libraries and executable in the top-level 'bin' dir
SET(LIBRARY_OUTPUT_PATH
    ${OpenFlightWriter_BINARY_DIR}/bin CACHE PATH
    "Single directory for all libraries.")

SET(EXECUTABLE_OUTPUT_PATH ${OpenFlightWriter_BINARY_DIR}/bin CACHE PATH
    "Single directory for all executables.")

MARK_AS_ADVANCED(LIBRARY_OUTPUT_PATH)
MARK_AS_ADVANCED(EXECUTABLE_OUTPUT_PATH)

# Enable ctest hooks
ENABLE_TESTING()

# Locate OpenSceneGraph libraries and headers
FIND_PACKAGE(OSG)

INCLUDE_DIRECTORIES(${OSG_INCLUDE_DIR} /usr/X11R6/include)
LINK_DIRECTORIES(${OSG_LIBRARIES_DIR})



ADD_SUBDIRECTORY(test)
