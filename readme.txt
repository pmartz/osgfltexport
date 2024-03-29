This is the regression test suite for OSG OpenFlight export plugin.
Copyright(c) 2008 Skew Matrix Software LLC and Blue Newt Software LLC.

Requirements:
 * OSG current SVN head installed and runnable on your system.
 * Python.
 * PIL (Python Imaging Library).

Build:
 * Use CMake to generate project files for your platform.
 * Build everything in the project.

   Finding OSG in CMake:
   This project uses a custom CMake script to aid in building the project with different OSG binaries. The CMake variable *OSGInstallType* can be set one of three ways:
    * Default Installation: CMake will use OSG installed into the default location on your system.
    * Alternate Install Location: Select this option, then provide the install location root directory, to use OSG from a non-default install location.
    * Source And Build Tree: Select this option, then provide the OSG source and build directories, to use OSG built from a source tree.

Run:
This project uses CTest:
http://www.vtk.org/Wiki/CMake_Testing_With_CTest

In Visual Studio, build the RUN_TESTS project.

From a Linux/Unix shell:
    make test

The regression test suite uses the grabScreen executable to load various .osg/.flt files and capture a screenshot. Then it invokes the convertToFlt executable to export the scene graph as a FLT file. It again uses grabScreen to load the converted FLT file and capture its image. Finally, it uses the PSNR function in PIL to compare the images. If they are significantly different, the test fails, and otherwise passes.

Upon failure, the exported FLT file nd both .png screenshots are left in the output directory so that they may be examined to determine the cause of the failure. If the tests pass, these files are automatically deleted.

To comment on the test suite or request modifications, please email pmartz@skew-matrix.com.

CREDITS
The following people contributed to this regression test suite by writing the framework, creating tests, or contributing data:
 * Jason Daly
 * Dr. Neil Hughes / Logicom Computer Services, UK
 * Bob Kuehne
 * Paul Martz
 * Katharina Plugge
 * Dave Wolfe
