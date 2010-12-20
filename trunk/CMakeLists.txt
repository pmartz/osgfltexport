cmake_minimum_required(VERSION 2.8)
project(OpenFlightWriter)

# Add path containing our custom CMake modules
set( CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/CMakeModules;${CMAKE_MODULE_PATH}" )


# Put all libraries and executable in the top-level 'bin' dir
set( LIBRARY_OUTPUT_PATH
    ${OpenFlightWriter_BINARY_DIR}/bin CACHE PATH
    "Single directory for all libraries.")

set( EXECUTABLE_OUTPUT_PATH ${OpenFlightWriter_BINARY_DIR}/bin CACHE PATH
    "Single directory for all executables.")

mark_as_advanced( LIBRARY_OUTPUT_PATH )
mark_as_advanced( EXECUTABLE_OUTPUT_PATH )

# Enable ctest hooks
enable_testing()


#
# dependencies
#   OSG
include( FindOSGHelper )
include_directories( ${OSG_INCLUDE_DIRS} )

#   Python
find_package( PythonInterp REQUIRED )

#   PIL (Python Image Library
if( PYTHONINTERP_FOUND )
    get_filename_component( _pyDir ${PYTHON_EXECUTABLE} PATH )
    if( NOT EXISTS ${_pyDir}/Lib/site-packages/PIL/Image.py )
        message( FATAL " Could not find PIL (Python Image Library)." )
    endif()
endif()


add_subdirectory( test )
