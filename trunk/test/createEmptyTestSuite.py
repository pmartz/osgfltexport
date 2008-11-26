#!/bin/env python
'''
  This script creates a skeleton test suite for a module.  You just pass it
  the name of the class/module you want to test, and it writes all the
  boilerplate setup to a file.  If you say:

    createsEmptyTestSuite.py MyModule

  the output will be sent to the file 'testMyModule.h'.

'''

import sys
import os.path
from string import Template

if len(sys.argv) != 2:
    print "\nUsage:  %s <ModuleName>\n" % os.path.basename(sys.argv[0])
    sys.exit(-1)

fileName = 'test' + sys.argv[1] + '.h'
if os.path.exists(fileName):
    yesOrNo = raw_input(fileName + " already exists! Overwrite? [y/n] ")
    if yesOrNo != 'y':
        print "Aborting..."
        sys.exit(-1)
 

s = Template("""#include <cxxtest/TestSuite.h>
// Add other #include's here as needed...

class ${Module}TestSuite : public CxxTest::TestSuite
{
  public:
    static ${Module}TestSuite* createSuite()
    {
        globalSetUp();
        return new ${Module}TestSuite;
    }

    static void destroySuite(${Module}TestSuite* suite)
    {
        globalTearDown();
        delete suite;
    }

    static void globalSetUp();
    static void globalTearDown();

    void setUp();
    void tearDown();

    // Sample tests---delete me
    void testFoo();
    void testBar();
};


namespace test${Module} {


    // Any helper classes or global variables needed by the test suite
    // should be defined here.  They need to be in a separate namespace to
    // prevent clashes with definitions in other suites using the same test
    // runner.  As a general rule, the first line of any test should be:
    // 
    //   using namespace test${Module};


}  // End namespace test${Module}


void ${Module}TestSuite::globalSetUp()
{
    using namespace test${Module};

    // Use this function to do any setup that needs to happen once
    // for the whole test suite...
}

void ${Module}TestSuite::globalTearDown()
{
    using namespace test${Module};

    // Use this function to do any teardown that needs to happen once
    // for the whole test suite...
}


void ${Module}TestSuite::setUp()
{
    using namespace test${Module};

    // Use this function to do any setup that needs to be be done
    // for each test...
}

void ${Module}TestSuite::tearDown()
{
    using namespace test${Module};

    // Use this function to do any teardown that needs to be be done
    // for each test...
}


void ${Module}TestSuite::testFoo()
{
    using namespace test${Module};
    TS_ASSERT(1 == 1);
}

void ${Module}TestSuite::testBar()
{
    using namespace test${Module};
    TS_ASSERT(1 == 0);
}
""")

f = file(fileName, 'w')
f.write(s.substitute(Module=sys.argv[1]))
f.close()
