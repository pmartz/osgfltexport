This is the regression test suite for OSG OpenFlight export plugin.
Copyright(c) 2008 Skew Matrix Software LLC and Blue Newt Software LLC.

Requirements:
 * OSG current SVN head installed and runnable on your system.
 * Python.
 * PIL (Python Imaging Library).

Build:
 * Use CMake to generate project files for your platform.
 * Build everything in the project.

Run:
Build the RUN_TESTS project.

The regression test suite uses the grabScreen executable to load various .osg/.flt files and capture a screenshot. Then it invokes the convertToFlt executable to export the scene graph as a FLT file. It again uses grabScreen to load the converted FLT file and capture its image. Finally, it uses the PSNR function in PIL to compare the images. If they are significantly different, the test fails, and otherwise passes.

Upon failure, the exported FLT file nd both .png screenshots are left in the output directory so that they may be examined to determine the cause of the failure. If the tests pass, these files are automatically deleted.

To comment on the test suite or request modifications, please email pmartz@skew-matrix.com.

CREDITS
The following people contributed to this regression test suite by writing the framework, creating tests, or contributing data:
 * Jason Daly
 * Dr. Neil Hughes / Logicom Computer Services, UK
 * Bob Kuehne
 * Paul Martz
 * Dave Wolfe
