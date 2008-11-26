#include <iostream>
#include <osg/Node>
#include <osg/Group>
#include <osg/Texture2D>
#include <osgDB/ReadFile> 
#include <osgDB/WriteFile> 
#include <osgViewer/Viewer>

struct GrabberCallback : public osg::Camera::DrawCallback
{
    GrabberCallback(osgViewer::Viewer& viewer, osg::ref_ptr<osg::Image> image,
                    std::string const& outputFileName,
                    int width, int height, int x=0, int y=0)
      : viewer_(viewer)
      , image_(image)
      , outputFileName_(outputFileName)
      , width_(width)
      , height_(height)
      , x_(x)
      , y_(y) { }

    virtual void operator () (const osg::Camera& camera) const
    {
        static int count = 0;
        if ( ++count == 1 )
        {
            // Problem was an empty RGB file on Mac.
            // Doesn't help (and doesn't lik). Problem solved on Mac by nusing PNG instead of RGB.
            //glReadBuffer( GL_FRONT );
            //glFlush();
            image_->readPixels(x_, y_, width_, height_, GL_RGB,GL_UNSIGNED_BYTE);
            osgDB::writeImageFile(*image_, outputFileName_ );
            viewer_.setDone( true );
        }
    }
    
    osg::ref_ptr<osg::Image> image_;
    osgViewer::Viewer& viewer_;
    std::string outputFileName_;
    int width_, height_, x_, y_;
};


int main(int argc, char* argv[])
{
    if (argc != 3)
    {
        osg::notify(osg::FATAL)
            << "Usage: grabScreen <inputModelFileName> <outputImageFileName>"
            << std::endl;
        return -1;
    }

    std::string inputFile = argv[1];
    std::string outputFile = argv[2];
    
    osgViewer::Viewer viewer;
    viewer.setThreadingModel( osgViewer::Viewer::SingleThreaded );

    osgDB::ReaderWriter::Options* opt = new osgDB::ReaderWriter::Options;
    //opt->setOptionString( "preserveObject preserveFace" );
    osg::ref_ptr<osg::Node> root = osgDB::readNodeFile( inputFile, opt );
    if (!root.valid())
    {
        osg::notify(osg::FATAL) << "Unable to load data file "
                                   "(is OSG_FILE_PATH set?)";
        return -1;
    }

    viewer.setSceneData( root.get() );

    int width = 400, height = 300;
    viewer.setUpViewInWindow( 10, 10, width, height );

    osg::ref_ptr<osg::Image> image = new osg::Image;
    viewer.getCamera()->setPostDrawCallback(new GrabberCallback(viewer, image, outputFile,
                                                             width, height));

    viewer.run();

    return 0;
}
