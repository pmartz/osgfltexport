import struct
import sys
from os.path import basename

# TODO: Need to figure out differences between 15.7, 15.8, and 16.1 OpenFlight
# versions and make sure all required opcodes are represented...
class Flt(object):
    RecordType = {
         0 :  'Invalid',
         1 :  'Header',
         2 :  'Group',
         4 :  'Object',
         5 :  'Face',
        10 :  'PushLevel',
        11 :  'PopLevel',

        14 :  'DegreeOfFreedom',

        19 :  'PushSubface',
        20 :  'PopSubface',
        21 :  'PushExtension',
        22 :  'PopExtension',
        23 :  'Continuation',

        31 :  'Comment',
        32 :  'ColorPalette',
        33 :  'LongId',

        49 :  'Matrix',
        50 :  'Vector',
        52 :  'Multitexture',
        53 :  'UvList',

        55 :  'BinarySeparatingPlane',

        60 :  'Replicate',
        61 :  'InstanceReference',
        62 :  'InstanceDefinition',
        63 :  'ExternalReference',
        64 :  'TexturePalette',
        67 :  'VertexPalette',
        68 :  'VertexWithColor',
        69 :  'Vertex-C-N',
        70 :  'Vertex-C-N-UV',
        71 :  'Vertex-C-UV',
        72 :  'VertexList',
        73 :  'LevelOfDetail',
        74 :  'BoundingBox',

        76 :  'RotateAboutEdge',
        77 :  'Scale',
        78 :  'Translate',
        79 :  'NonuniformScale',
        80 :  'RotateAboutPoint',
        81 :  'RotateScaleToPoint',
        82 :  'PutTransform',
        83 :  'EyepointAndTrackplanePalette',
        84 :  'Mesh',
        85 :  'LocalVertexPool',
        86 :  'MeshPrimitive',
        87 :  'Road_segment',
        88 :  'RoadZone',
        89 :  'MorphVertexList',
        90 :  'LinkagePalette',
        91 :  'Sound',
        92 :  'RoadPath',
        93 :  'SoundPalette',
        94 :  'GeneralMatrix',
        95 :  'Text',
        96 :  'Switch',
        97 :  'LineStylePalette',
        98 :  'ClipRegion',

       100 :  'Extension',
       101 :  'LightSource',
       102 :  'LightSourcePalette',

       105 :  'BoundingSphere',
       106 :  'BoundingCylinder',
       107 :  'BoundingConvexHull',
       108 :  'BoundingVolumeCenter',
       109 :  'BoundingVolumeOrientation',
       110 :  'HistogramBoundingVolume',
       111 :  'LightPoint',
       112 :  'TextureMappingPalette',
       113 :  'MaterialPalette',
       114 :  'NameTable',
       115 :  'Cat',
       116 :  'CatData',

       119 :  'BoundingHistogram',

       122 :  'PushAttribute',
       123 :  'PopAttribute',

       125 :  'AdaptiveAttribute',
       126 :  'CurveNode',
       127 :  'RoadConstruction',
       128 :  'LightPointAppearancePalette',
       129 :  'LightPointAnimationPalette',
       130 :  'IndexedLightPoint',
       131 :  'LightPointSystem',
       132 :  'IndexedString',
       133 :  'ShaderPalette',
         3 :  'ObsoleteLOD',
         7 :  'ObsoleteAbsoluteVertex',
         8 :  'ObsoleteShadedVertex',
         9 :  'Obsoletenormal_vertex',
        40 :  'ObsoleteTranslate',
        41 :  'ObsoleteRotateAboutPoint',
        42 :  'ObsoleteRotateAboutEdge',
        43 :  'ObsoleteScale',
        44 :  'ObsoleteTranslate2',
        45 :  'ObsoleteNonuniformScale',
        46 :  'ObsoleteRotateAboutPoint2',
        47 :  'ObsoleteRotateScaleToPoint',
        48 :  'ObsoletePutTransform',
        51 :  'ObsoleteBoundingBox',
        65 :  'ObsoleteEyepointPalette',
        66 :  'ObsoleteMaterialPalette',
    }

    @staticmethod
    def MaterialPalette(fileBuf, idx, level):
        (opcode, length, index, name, flags, ar, ag, ab, dr, dg, db, sr, sg, sb, er, eg, eb, shininess) = struct.unpack('>hHl12sl13f', fileBuf[idx:idx+76])
        print level * '  ' + "MaterialPalette: Index = %d" % index
        print level * '  ' + "   ambient: %.3f, %.3f, %.3f" % (ar, ag, ab)
        print level * '  ' + "   diffuse: %.3f, %.3f, %.3f" % (dr, dg, db)
        print level * '  ' + "  specular: %.3f, %.3f, %.3f" % (sr, sg, sb)
        print level * '  ' + "  emissive: %.3f, %.3f, %.3f" % (er, eg, eb)

    
    @staticmethod
    def VertexList(fileBuf, idx, level):
        (opcode, length) = struct.unpack('>hH', fileBuf[idx:idx+4])
        idx += 4
        numVertices = (length - 4)/4
        vertices = []
        for i in range(numVertices):
            (offset,) = struct.unpack('>l', fileBuf[idx:idx+4])
            idx += 4
            vertices.append(offset)
            
        print level * '  ' + "VertexList: %d" % numVertices
        #print level * '  ' + '  ' + str(vertices)
        
    @staticmethod
    def EyepointAndTrackplanePalette(fileBuf, idx, level):
        """ IGNORED """
        pass

    @staticmethod
    def VertexPalette(fileBuf, idx, level):
        (opcode, headerLen, paletteLen) = struct.unpack('>hHl', fileBuf[idx:idx+8])
        idx += 8

        numVertices = 0
        bytesLeft = paletteLen - headerLen

        while bytesLeft:
            (opcode, length) = struct.unpack('>hH', fileBuf[idx:idx+4])
            idx += length
            bytesLeft -= length
            numVertices += 1

        print level * '  ' + "VertexPalette:", numVertices

    @staticmethod
    def Face(fileBuf, idx, level):
        (opcode, length, dontcare, index) = struct.unpack('>hH26sh',
                                                       fileBuf[idx:idx+32])
        print level * '  ' + "Face: MaterialIndex = %d" % index

    @staticmethod
    def LevelOfDetail(fileBuf, idx, level):
        (opcode,
         length,
         id,
         reserved,
         switchInDist,
         switchOutDist,
         specialEffect1,
         specialEffect2,
         flags,
         centerX,
         centerY,
         centerZ,
         transitionRange,
         significantSize) = struct.unpack('>hH8sl2d2hl5d', fileBuf[idx:idx+80])
        id = id.rstrip('\x00')
        print level * '  ' + 'LOD: "%s"' % id
        print level * '  ' + "  Reserved           = %d" % reserved
        print level * '  ' + "  Switch-in Dist     = %.2f" % switchInDist
        print level * '  ' + "  Switch-out Dist    = %.2f" % switchOutDist
        print level * '  ' + "  Special effect ID1 = %d" % specialEffect1
        print level * '  ' + "  Special effect ID2 = %d" % specialEffect2
        print level * '  ' + "  Flags              = 0x%x" % flags

        print level * '  ' + "  Center(x, y, z)    = (%f, %f, %f)" % (centerX,
                                                                   centerY,
                                                                   centerZ)
        print level * '  ' + "  Transition range   = %.2f" % transitionRange
        print level * '  ' + "  Significant size   = %.2f" % significantSize


    @staticmethod
    def LongId(fileBuf, idx, level):
        (opcode, length) = struct.unpack('>hH', fileBuf[idx:idx+4])
        (id,) = struct.unpack(str(length-4) + 's', fileBuf[idx+4:idx+length])
        id = id.rstrip('\x00')
        print level * '  ' + 'LongId: "%s"' % id


    @staticmethod
    def DegreeOfFreedom(fileBuf, idx, level):
        (opcode,
         length,
         id,
         reserved1,
         originX,
         originY,
         originZ,
         xRefX,
         xRefY,
         xRefZ,
         xyRefX,
         xyRefY,
         xyRefZ,
         minZ,
         maxZ,
         currZ,
         incrZ,
         minY,
         maxY,
         currY,
         incrY,
         minX,
         maxX,
         currX,
         incrX,
         minPitch,
         maxPitch,
         currPitch,
         incrPitch,
         minRoll,
         maxRoll,
         currRoll,
         incrRoll,
         minYaw,
         maxYaw,
         currYaw,
         incrYaw,
         minZScale,
         maxZScale,
         currZScale,
         incrZScale,
         minYScale,
         maxYScale,
         currYScale,
         incrYScale,
         minXScale,
         maxXScale,
         currXScale,
         incrXScale,
         flags,
         reserved2) = struct.unpack('>hH8sl45d2l', fileBuf[idx:idx+384])
        
        id = id.rstrip('\x00')
        print level * '  ' + 'DOF: "%s"' % id
        print level * '  ' + "  Reserved1      = 0x%x" % reserved1
        print level * '  ' + "  Origin         = (%.3f, %.3f, %.3f)" % (originX, originY, originZ)
        print level * '  ' + "  XRefPoint      = (%.3f, %.3f, %.3f)" % (xRefX, xRefY, xRefZ)
        print level * '  ' + "  XYRefPoint     = (%.3f, %.3f, %.3f)" % (xyRefX, xyRefY, xyRefZ)
        print level * '  ' + "  Min z          = %.3f" % minZ
        print level * '  ' + "  Max z          = %.3f" % maxZ
        print level * '  ' + "  Curr z         = %.3f" % currZ
        print level * '  ' + "  Incr z         = %.3f" % incrZ
        print level * '  ' + "  Min y          = %.3f" % minY
        print level * '  ' + "  Max y          = %.3f" % maxY
        print level * '  ' + "  Curr y         = %.3f" % currY
        print level * '  ' + "  Incr y         = %.3f" % incrY
        print level * '  ' + "  Min x          = %.3f" % minX
        print level * '  ' + "  Max x          = %.3f" % maxX
        print level * '  ' + "  Curr x         = %.3f" % currX
        print level * '  ' + "  Incr x         = %.3f" % incrX
        print level * '  ' + "  Min pitch      = %.3f" % minPitch
        print level * '  ' + "  Max pitch      = %.3f" % maxPitch
        print level * '  ' + "  Curr pitch     = %.3f" % currPitch
        print level * '  ' + "  Incr pitch     = %.3f" % incrPitch
        print level * '  ' + "  Min roll       = %.3f" % minRoll
        print level * '  ' + "  Max roll       = %.3f" % maxRoll
        print level * '  ' + "  Curr roll      = %.3f" % currRoll
        print level * '  ' + "  Incr roll      = %.3f" % incrRoll
        print level * '  ' + "  Min yaw        = %.3f" % minYaw
        print level * '  ' + "  Max yaw        = %.3f" % maxYaw
        print level * '  ' + "  Curr yaw       = %.3f" % currYaw
        print level * '  ' + "  Incr yaw       = %.3f" % incrYaw
        print level * '  ' + "  Min Z scale    = %.3f" % minZScale
        print level * '  ' + "  Max Z scale    = %.3f" % maxZScale
        print level * '  ' + "  Curr Z scale   = %.3f" % currZScale
        print level * '  ' + "  Incr Z scale   = %.3f" % incrZScale
        print level * '  ' + "  Min Y scale    = %.3f" % minYScale
        print level * '  ' + "  Max Y scale    = %.3f" % maxYScale
        print level * '  ' + "  Curr Y scale   = %.3f" % currYScale
        print level * '  ' + "  Incr Y scale   = %.3f" % incrYScale
        print level * '  ' + "  Min X scale    = %.3f" % minXScale
        print level * '  ' + "  Max X scale    = %.3f" % maxXScale
        print level * '  ' + "  Curr X scale   = %.3f" % currXScale
        print level * '  ' + "  Incr X scale   = %.3f" % incrXScale
        print level * '  ' + "  Flags          = 0x%x" % flags
        print level * '  ' + "  Reserved2      = 0x%x" % reserved2

    @staticmethod
    def IndexedString(fileBuf, idx, level):
        (opcode, length, index) = struct.unpack('>hHL', fileBuf[idx:idx+8])
        (string,) = struct.unpack(str(length-8) + 's', fileBuf[idx+8:idx+length])
        string = string.rstrip('\x00')
        print level * '  ' + 'IndexedString: %d = "%s"' % (index, string)

    @staticmethod
    def ExternalReference(fileBuf, idx, level):
        (opcode, length, filename, reserved1, flags, viewAsBoundingBox,
         reserved2) = struct.unpack('>hH200sLLhh', fileBuf[idx:idx+216])

        filename = filename.rstrip('\x00')
        print level * '  ' + 'External reference: "%s"' % filename
        print level * '  ' + '              Flags = 0x%x' % flags
        print level * '  ' + '  ViewAsBoundingBox = %d' % viewAsBoundingBox


if len(sys.argv) < 2:
  print "Usage: %s <fltFileName>" % basename(sys.argv[0])
  sys.exit(-1)


try:
    f = file(sys.argv[1], 'rb')
    fileBuf = f.read()
    fileLen = len(fileBuf)

    idx = 0
    level = 0
    while idx < fileLen:
        (opcode, length) = struct.unpack('>hH', fileBuf[idx:idx+4])
        recType = Flt.RecordType[opcode]

        if hasattr(Flt, recType):
            getattr(Flt, recType)(fileBuf, idx, level)
        else:
            print level * '  ' + "%s" % (recType,)

        if recType == 'PushLevel':
            level += 1
        elif recType == 'PopLevel':
            level -= 1

        idx += length


except IOError, e:
    print e
    sys.exit(-1)

