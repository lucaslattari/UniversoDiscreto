import struct 
import json

INT_SIZE        = 4
TEXTURE_SIZE    = 64 + 4 + 4
PLANE_SIZE      = 4 * 3 + 4
FACE_SIZE       = 104
VERTEX_SIZE     = 44
MESHVERTEX_SIZE = 4

class BSPData:
    def __init__(self, fPointer, header):
        allBSPData =  self.getBSPData(fPointer)

        #entities#
        self.entities = allBSPData[header.ENTITIES_OFFSET : header.ENTITIES_OFFSET + header.ENTITIES_LENGTH].decode('utf8')
        
        #textures#
        self.totalOfTextures = int(header.TEXTURES_LENGTH / (TEXTURE_SIZE))
        self.textures = []
        for i in range(0, self.totalOfTextures):
            textureName = allBSPData[header.TEXTURES_OFFSET + i * TEXTURE_SIZE : header.TEXTURES_OFFSET + 64 + i * TEXTURE_SIZE].decode('utf8').rstrip('\x00')
            textureFlags = int.from_bytes(allBSPData[header.TEXTURES_OFFSET + 64 + i * TEXTURE_SIZE : header.TEXTURES_OFFSET + 68 + i * TEXTURE_SIZE], byteorder='little')
            textureContents = int.from_bytes(allBSPData[header.TEXTURES_OFFSET + 68 + i * TEXTURE_SIZE : header.TEXTURES_OFFSET + 72 + i * TEXTURE_SIZE], byteorder='little')

            self.textures.append([textureName, textureFlags, textureContents])
            
        #planes#
        self.totalOfPlanes = int(header.PLANES_LENGTH / (PLANE_SIZE))
        self.planes = []
        for i in range(0, self.totalOfPlanes):
            normalX = struct.unpack('f', allBSPData[header.PLANES_OFFSET + i * PLANE_SIZE : header.PLANES_OFFSET + 4 + i * PLANE_SIZE])
            normalY = struct.unpack('f', allBSPData[header.PLANES_OFFSET + 4 + i * PLANE_SIZE : header.PLANES_OFFSET + 8 + i * PLANE_SIZE])
            normalZ = struct.unpack('f', allBSPData[header.PLANES_OFFSET + 8 + i * PLANE_SIZE : header.PLANES_OFFSET + 12 + i * PLANE_SIZE])
            dist = struct.unpack('f', allBSPData[header.PLANES_OFFSET + 12 + i * PLANE_SIZE : header.PLANES_OFFSET + 16 + i * PLANE_SIZE])
        
            self.planes.append([normalX, normalY, normalZ, dist])

        #faces
        self.totalOfFaces = int(header.FACES_LENGTH / (FACE_SIZE))
        self.faces = []
        for i in range(0, self.totalOfFaces):
            #textureIndex    = int.from_bytes(allBSPData[header.FACES_OFFSET + i * FACE_SIZE : header.FACES_OFFSET + 4 + i * FACE_SIZE], byteorder='little')
            #effectIndex     = int.from_bytes(allBSPData[header.FACES_OFFSET + 4 + i * FACE_SIZE : header.FACES_OFFSET + 8 + i * FACE_SIZE], byteorder='little')
            faceType        = int.from_bytes(allBSPData[header.FACES_OFFSET + 8 + i * FACE_SIZE : header.FACES_OFFSET + 12 + i * FACE_SIZE], byteorder='little')
            firstVertex     = int.from_bytes(allBSPData[header.FACES_OFFSET + 12 + i * FACE_SIZE : header.FACES_OFFSET + 16 + i * FACE_SIZE], byteorder='little')
            totalVertices   = int.from_bytes(allBSPData[header.FACES_OFFSET + 16 + i * FACE_SIZE : header.FACES_OFFSET + 20 + i * FACE_SIZE], byteorder='little')
            
            #firstMeshVertex = int.from_bytes(allBSPData[header.FACES_OFFSET + 20 + i * FACE_SIZE : header.FACES_OFFSET + 24 + i * FACE_SIZE], byteorder='little')
            #totalMeshVerts  = int.from_bytes(allBSPData[header.FACES_OFFSET + 24 + i * FACE_SIZE : header.FACES_OFFSET + 28 + i * FACE_SIZE], byteorder='little')
            
            #lightmapIndex   = int.from_bytes(allBSPData[header.FACES_OFFSET + 28 + i * FACE_SIZE : header.FACES_OFFSET + 32 + i * FACE_SIZE], byteorder='little')
            
            #xOriginLightmapImage  = int.from_bytes(allBSPData[header.FACES_OFFSET + 32 + i * FACE_SIZE : header.FACES_OFFSET + 36 + i * FACE_SIZE], byteorder='little')
            #yOriginLightmapImage  = int.from_bytes(allBSPData[header.FACES_OFFSET + 36 + i * FACE_SIZE : header.FACES_OFFSET + 40 + i * FACE_SIZE], byteorder='little')
            #xsizeLightmapImage  = int.from_bytes(allBSPData[header.FACES_OFFSET + 40 + i * FACE_SIZE : header.FACES_OFFSET + 44 + i * FACE_SIZE], byteorder='little')
            #ysizeLightmapImage  = int.from_bytes(allBSPData[header.FACES_OFFSET + 44 + i * FACE_SIZE : header.FACES_OFFSET + 48 + i * FACE_SIZE], byteorder='little')

            self.faces.append([faceType, firstVertex, totalVertices])

        #vertexes
        self.totalOfVertices = int(header.VERTEXES_LENGTH / (VERTEX_SIZE))
        self.vertexes = []
        for i in range(0, self.totalOfVertices):
            posX = struct.unpack('f', allBSPData[header.VERTEXES_OFFSET + i * VERTEX_SIZE : header.VERTEXES_OFFSET + 4 + i * VERTEX_SIZE])
            posY = struct.unpack('f', allBSPData[header.VERTEXES_OFFSET + 4 + i * VERTEX_SIZE : header.VERTEXES_OFFSET + 8 + i * VERTEX_SIZE])
            posZ = struct.unpack('f', allBSPData[header.VERTEXES_OFFSET + 8 + i * VERTEX_SIZE : header.VERTEXES_OFFSET + 12 + i * VERTEX_SIZE])

            normalX = struct.unpack('f', allBSPData[header.VERTEXES_OFFSET + 28 + i * VERTEX_SIZE : header.VERTEXES_OFFSET + 32 + i * VERTEX_SIZE])
            normalY = struct.unpack('f', allBSPData[header.VERTEXES_OFFSET + 32 + i * VERTEX_SIZE : header.VERTEXES_OFFSET + 36 + i * VERTEX_SIZE])
            normalZ = struct.unpack('f', allBSPData[header.VERTEXES_OFFSET + 36 + i * VERTEX_SIZE : header.VERTEXES_OFFSET + 40 + i * VERTEX_SIZE])
            
            self.vertexes.append([posX, posY, posZ, normalX, normalY, normalZ])

        #meshverts
        self.totalOfMeshVerts = int(header.MESHVERTS_LENGTH / (MESHVERTEX_SIZE))
        self.meshverts = []
        for i in range(0, self.totalOfMeshVerts):
            offset = int.from_bytes(allBSPData[header.MESHVERTS_OFFSET + i * MESHVERTEX_SIZE : header.MESHVERTS_OFFSET + 4 + i * MESHVERTEX_SIZE], byteorder='little')
            
            self.meshverts.append([offset])

        self.data = []
        self.data.append([self.faces, self.vertexes])

    def getBSPData(self, fPointer):
        fPointer.seek(0, 0)
        return fPointer.read()

    def writeBSPDataAsJsonFile(self, filename):
        with open(filename, "w") as outfile:
            json.dump(self.data, outfile)

class BSPHeader:
    def __init__(self, fPointer):
        self.magic = fPointer.read(INT_SIZE)
        self.version = fPointer.read(INT_SIZE)
        
        #entities#
        self.ENTITIES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.ENTITIES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        
        #textures#
        self.TEXTURES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.TEXTURES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #PLANES#
        self.PLANES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.PLANES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #NODES#
        self.NODES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.NODES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #LEAVES#
        self.LEAVES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.LEAVES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #LEAFFACES#
        self.LEAFFACES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.LEAFFACES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #LEAFBRUSHES#
        self.LEAFBRUSHES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.LEAFBRUSHES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #MODELS#
        self.MODELS_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.MODELS_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #BRUSHES#
        self.BRUSHES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.BRUSHES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #BRUSHSIDES#
        self.BRUSHSIDES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.BRUSHSIDES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #VERTEXES#
        self.VERTEXES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.VERTEXES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #MESHVERTS#
        self.MESHVERTS_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.MESHVERTS_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #EFFECTS#
        self.EFFECTS_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.EFFECTS_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

        #FACES#
        self.FACES_OFFSET = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')
        self.FACES_LENGTH = int.from_bytes(fPointer.read(INT_SIZE), byteorder='little')

class BSPLoader:    
    def __init__(self, filename):
        self.filename = filename
        self.loadBSPFile()
        
    def loadBSPFile(self):
        f = open(self.filename, 'rb')
        self.loadBSPHeader(f)
        self.loadBSPData(f, self.header)
        
    def loadBSPHeader(self, f):
        self.header = BSPHeader(f)
        
    def loadBSPData(self, f, h):
        self.data = BSPData(f, h)

if __name__ == "__main__":
    bsp = BSPLoader("test1.bsp")
    bsp.data.writeBSPDataAsJsonFile("bspdata.json")