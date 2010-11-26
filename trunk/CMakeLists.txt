cmake_minimum_required(VERSION 2.8)
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
FIND_PACKAGE( OpenSceneGraph 2.8.3 REQUIRED COMPONENTS OpenThreads osg osgDB osgViewer )
IF(OSG_FOUND)
    # define shortcuts
    SET( OSG_INCLUDE_DIRS ${OSG_INCLUDE_DIR} ${OSGDB_INCLUDE_DIR} ${OSGVIEWER_INCLUDE_DIR} ${OPENTHREADS_INCLUDE_DIR} )
    SET( OSG_LIBRARIES ${OSG_LIBRARIES} ${OSGDB_LIBRARIES} ${OSGVIEWER_LIBRARIES} ${OPENTHREADS_LIBRARIES} )
ENDIF()

INCLUDE_DIRECTORIES( ${OSG_INCLUDE_DIRS} )



ADD_SUBDIRECTORY(test)
