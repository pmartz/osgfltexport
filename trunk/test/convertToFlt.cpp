#include <iostream>
#include <osg/notify>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>

int main(int argc, char* argv[])
{
    if (argc != 3)
    {
        osg::notify(osg::FATAL)
            << "Usage: convertToFlt <inputFileName> <outputFileName>"
            << std::endl;
        return -1;
    }

    std::string inputFile = argv[1];
    std::string outputFile = argv[2];

    osg::ref_ptr<osgDB::ReaderWriter::Options> opts = 
        new osgDB::ReaderWriter::Options;

    // Set any required loader options here...
    //opts->setOptionString("preserveFace preserveObject readObjectRecordData");

    osg::ref_ptr<osg::Node> sg =
        osgDB::readNodeFile(inputFile, opts.get() );

    if (!sg.valid())
    {
        osg::notify(osg::FATAL)
            << "Unable to load data file '"
            << "cone-mat.flt"
            << "', aborting (is OSG_FILE_PATH set?)..."
            << std::endl;

        return -1;
    }

    bool writeSucceeded = osgDB::writeNodeFile( *(sg.get()), outputFile);

    if (!writeSucceeded)
    {
        return -1;
    }

    return 0;
}
