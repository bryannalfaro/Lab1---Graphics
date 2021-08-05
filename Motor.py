'''
Universidad del Valle de Guatemala
Graficas por computadora - Bryann Alfaro
'''
from gl import Renderer

#division by zero
#out of range
r =  Renderer()
r.glInit()
r.glCreateWindow(800,800)
r.glViewPort(0,0,3,3)
r.glClearColor(1,0.75,0.80)
r.glColor(0.85,0.125,0.125)



r.line(165,380,185,360)
r.line(185,360,180,330)
r.line(180, 330, 207,345)
r.line(207,345,233,330)
r.line(233,330,230,360)
r.line(230,360,250,380)
r.line(250,380,220,385)
r.line(220,385,205,410)
r.line(205,410,193,383)
r.line(193,383,165,380)
r.fill()

r.glColor(0.25,0.125,0.125)

r.line(321,335,288,286)
r.line(288,286,339,251)
r.line(339,251,374,302)
r.line(374,302,321,335)
r.fill()

r.glColor(0.16,0.79,0.56)

r.line(377,249,411,197)
r.line(411,197,436,249)
r.line(436,249,377,249)
r.fill()

r.line(682,175,708,120)
r.line(708,120,735,148)
r.line(735,148,739,170)
r.line(739,170,682,175)
r.fill()
r.glColor(0.43,0.125,0.125)

r.line(413,177,448,159)
r.line(448,159,502,88)
r.line(502,88,553,53)
r.line(553,53,535,36)
r.line(535,36,676,37)
r.line(676,37,660,52)
r.line(660,52,750,145)
r.line(750,145,761,179)
r.line(761, 179,672,192)
r.line(672,192,659,214)
r.line(659,214,615,214)
r.line(615,214,632,230)
r.line(632,230,580,230)
r.line(580, 230,597,215)
r.line(597,215,552,214)
r.line(552,214,517,144)
r.line(517,144,466,180)
r.line(466,180,413,177)
r.fill()

r.glFinish("output.bmp")