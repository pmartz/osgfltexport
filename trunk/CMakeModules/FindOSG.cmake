# Find OpenSceneGraph headers and libs
#
# This module defines:
#    OSG_INCLUDE_DIR - Directory containing the osg headers
#
#  OSG_LIBRARIES_DIR - The path containing ${OSG_LIBRARY}
#
# OSG_ROOT is an environment or CMake variable that would correspond to the
# './configure --prefix=$OSG_ROOT' step typical of autoconf-based projects
#
# To be useful, this script requires OSG_ROOT to be set.  If set in the
# environment, CMake will pick it up from there.  Alternately, you can set it
# on the cmake commandline using syntax like the following:
#
#  cmake -DOSG_ROOT=/home/dwolfe/OpenSceneGraph-2.2.0  ../../MyProject 
#
# If OSG_ROOT is set on the commandline, it overrides any setting in the
# environment.
# 
#
#
FIND_PATH(OSG_INCLUDE_DIR
            osg/Node
          ${OSG_ROOT}/include
          $ENV{OSG_ROOT}/include)

FIND_LIBRARY(OSG_LIBRARY
    NAMES
      osg
    PATHS
      ${OSG_ROOT}/lib
      ${OSG_ROOT}/build/lib
      $ENV{OSG_ROOT}/lib
      $ENV{OSG_ROOT}/build/lib)

# Hide OSG_LIBRARY in the GUI, since most users can just ignore it
MARK_AS_ADVANCED(OSG_LIBRARY)


# OSG_LIBRARY should contain the absolute path to the core OSG library;
# Set OSG_LIBRARIES_DIR to the directory containing this lib
GET_FILENAME_COMPONENT(OSGLIB_DIR ${OSG_LIBRARY} PATH)
GET_FILENAME_COMPONENT(OSGLIB_NAME ${OSG_LIBRARY} NAME)
FIND_PATH(OSG_LIBRARIES_DIR ${OSGLIB_NAME} ${OSGLIB_DIR})


SET(OSG_FOUND "NO")
IF(OSG_INCLUDE_DIR AND OSG_LIBRARIES_DIR)
    SET(OSG_FOUND "YES")
ENDIF(OSG_INCLUDE_DIR AND OSG_LIBRARIES_DIR)
