FIND_PACKAGE( OpenGL REQUIRED )
FIND_PACKAGE( PythonInterp REQUIRED )

# Util program for grabbing a screen shot of a model
ADD_EXECUTABLE(grabScreen grabScreen.cpp)


# Util program for converting a model to FLT
ADD_EXECUTABLE(convertToFlt convertToFlt.cpp)


# Set some 'cheater' vars to help the convertAndCompare.py.in template
# locate the executables and data...
GET_TARGET_PROPERTY(GRAB_SCREEN_EXE grabScreen LOCATION)
SET( TEST_DATA_DIR "${CMAKE_CURRENT_SOURCE_DIR}/Data" )


# Copy before-and-after conversion/comparison script to binary dir,
# substituting variables along the way
CONFIGURE_FILE(${CMAKE_CURRENT_SOURCE_DIR}/convertAndCompare.py.in
               ${CMAKE_CURRENT_BINARY_DIR}/convertAndCompare.py
               @ONLY)

IF ( WIN32 )
    TARGET_LINK_LIBRARIES( grabScreen
                             optimized
                               osg
                             optimized
                               osgDB
                             optimized
                               osgGA
                             optimized
                               osgViewer
                             debug
                               osgd
                             debug
                               osgDBd
                             debug
                               osgGAd
                             debug
                               osgViewerd )

    TARGET_LINK_LIBRARIES( convertToFlt
                             optimized
                               osg
                             optimized
                               osgDB
                             debug
                               osgd
                             debug
                               osgDBd )

ELSE ( WIN32 )
    TARGET_LINK_LIBRARIES( grabScreen
                            ${OPENGL_LIBRARIES}
                             osg
                             osgDB
                             osgGA
                             osgSim
                             osgViewer )

    TARGET_LINK_LIBRARIES( convertToFlt
                             osg
                             osgDB
                             osgGA
                             osgSim
                             osgViewer )
ENDIF( WIN32 )


# Helper macro to clean up the test decls
MACRO(TEST_MODEL _model)
  ADD_TEST( ${_model} ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/convertAndCompare.py ${_model} )
ENDMACRO(TEST_MODEL)


# Add tests here!
TEST_MODEL( cone-comments.flt )
TEST_MODEL( cone-mat.flt )
TEST_MODEL( cone-simple.flt )
TEST_MODEL( cone-tex.flt )
TEST_MODEL( DrawElements.osg  )
TEST_MODEL( extRef.flt )
TEST_MODEL( fltTest00.osg )
TEST_MODEL( fltTest01.osg )
TEST_MODEL( fltTest02.osg )
TEST_MODEL( fltTest03.osg )
TEST_MODEL( fltTest04.osg )
TEST_MODEL( fltTestAlphaBlend.osg )
TEST_MODEL( LightPoint.flt )
TEST_MODEL( LightPointAnim.osg )
TEST_MODEL( testColor4ub.osg )
TEST_MODEL( testBillboard.osg )
TEST_MODEL( testDOF.flt )
TEST_MODEL( testLightSources.osg )
TEST_MODEL( testLOD.flt )
TEST_MODEL( testMaterialAlpha.osg )
TEST_MODEL( testMaterials.osg )
TEST_MODEL( testMultiDA.osg )
TEST_MODEL( testMultiSwitch.flt ) 
TEST_MODEL( testMultitex.osg ) 
TEST_MODEL( testNAN.osg )
TEST_MODEL( testObject.osg )
TEST_MODEL( testOsgSwitch.osg )
TEST_MODEL( testSubface.osg )
TEST_MODEL( testTexture.osg )
TEST_MODEL( textMeshMultitex.osg )
