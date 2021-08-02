import struct
from obj import Obj
"""
Bryann Alfaro 19372
SR1 - GRAFICAS POR COMPUTADORA
"""
def char(c):
    return struct.pack('=c',c.encode('ascii'))

def word(w):
    #short
    return struct.pack('=h',w)

def dword(d):
    #long
    return struct.pack('=l',d)

#setting the function to get color with bytes
def color(r,g,b):
    return bytes([b,g,r])

BLACK = color(0,0,0)
WHITE = color(255,255,255)

class Renderer(object):
    def __init__(self):
        self.default_color = color(0,0,139)
        self.cl_color = BLACK

    def point(self, x, y):
        self.framebuffer[y][x] =self.default_color



    def glInit(self):
        pass

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = []

    def glViewPort(self, x, y, width, height):
        self.vp_x = x
        self.vp_y = y
        self.vp_width = width
        self.vp_height = height

    #Fill the bitmap
    def glClear(self):
        self.framebuffer = [
            [self.cl_color for x in range(self.width)] for y in range(self.height)
            ]

    def frame(self):
        return self.framebuffer
    def glClearColor(self, r,g,b):
        self.cl_color = color(int(r*255),int(g*255),int(b*255))
        self.glClear()

    def glVertex(self,x,y):
        #formula get from microsoft glViewport function
        x_pos = int((x+1)*(self.vp_width/2)+self.vp_x)
        y_pos = int((y+1)*(self.vp_height/2)+self.vp_y)
        self.point(x_pos,y_pos)

    #change color of vertex
    def glColor(self, r,g,b):
        self.default_color = color(int(r*255),int(g*255),int(b*255))

    #Using class implementation
    def glLine(self,x0,y0,x1,y1):

        x0 = int((x0+1)*(self.vp_width/2)+self.vp_x)
        y0 = int((y0+1)*(self.vp_height/2)+self.vp_y)
        x1 = int((x1+1)*(self.vp_width/2)+self.vp_x)
        y1 = int((y1+1)*(self.vp_height/2)+self.vp_y)


        self.line(x0,y0,x1,y1)

    def line(self,x0,y0,x1,y1):

        dy = abs(y1-y0)
        dx = abs(x1-x0)

        steep = dy>dx
        #en caso de pendiente mayor a 1
        if steep:
            x0,y0 = y0,x0
            x1,y1 = y1,x1

            dy = abs(y1-y0)
            dx = abs(x1-x0)

        #en caso que el segundo valor sea menor que el primero
        if x1<x0:
            x0,x1 =x1,x0
            y0,y1 = y1,y0

            dy = abs(y1-y0)
            dx = abs(x1-x0)

        offset = 0 *2*dx
        threshold = 0.5 *2*dx
        y = y0

        points = []
        for x in range(x0,x1+1):
            if steep:
                points.append((y,x))

            else:
                points.append((x,y))

            offset += dy*2
            if offset >= threshold:

                y +=1 if y0<y1 else -1
                threshold +=1 *2* dx

            for pointf in points:
                self.point(*pointf)

    def load(self, filename, movement, scale):
        model = Obj(filename)
        for face in model.faces:
            vcount  = len(face)
            for j in range(vcount):
                f1 = face[j][0]
                f2 = face[(j+1)%vcount][0]

                v1  = model.vertices[f1-1]
                v2 = model.vertices[f2-1]

                x1 = round(((v1[0]+movement[0])*scale[0]))
                y1 = round(((v1[1]+movement[1])*scale[1]))
                x2 = round(((v2[0]+movement[0])*scale[0]))
                y2 = round(((v2[1]+movement[1])*scale[1]))

                self.line(x1,y1,x2,y2)

    def fill(self):
        contador1 = 0
        contador2 = 0
        bandera = False
        arreglo = []
        contador3 = 0
        x0,y0 = 0,0
        x1,y1 = 0,0


        for i in range(len(self.frame())): #filas

            for j in range(len(self.frame())): #cada valor fila
                #print('ban',bandera)


                if((self.cl_color[2],self.cl_color[1],self.cl_color[0]) != (self.frame()[i][j][2],self.frame()[i][j][1],self.frame()[i][j][0]) ):
                    a=self.frame()[i][j][2],self.frame()[i][j][1],self.frame()[i][j][0]

                    print('No es igual')
                    arreglo.append([1,a])
                else:
                     a=self.frame()[i][j][2],self.frame()[i][j][1],self.frame()[i][j][0]
                     arreglo.append([0,a])

            #print('arreglo',arreglo)
            for pos in range(len(arreglo)):
                #print('asld',arreglo[pos])
                if arreglo[pos][0] == 1:
                    if(bandera):
                            if(arreglo[pos][1]!=a):
                                a = arreglo[pos][1]
                                x0,y0 = pos,i
                            else:
                                x1,y1 = pos,i
                                #print(a[0]/255,a[1],a[2])
                                self.glColor(a[0]/255,a[1]/255,a[2]/255)
                                self.line(x0,y0,x1,y1)
                    else:
                        a = arreglo[pos][1]
                        x0,y0 = pos,i

                else:
                    if(x0!=0):
                        bandera = True
                    else:
                            bandera = False
            arreglo = []
            bandera = False
            x0,y0 = 0,0
            x1,y1 = 0,0
        print(contador1)
        print(contador2)


    def glFinish(self, filename):
        #bw means binary write
        f = open(filename, 'bw')
        #file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14+40+ 3*(self.width*self.height)))
        f.write(dword(0))
        f.write(dword(14+40))

        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(3*(self.width*self.height)))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        #bitmap
        for y in range(self.height):
            for x in range(self.width):
                f.write(self.framebuffer[y][x])

        f.close()