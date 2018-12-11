import re
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
import itertools
#from blist import blist
# conda install blist


re_parsePt =re.compile(r'position=<\s?([-\d]+),\s+([-\d]+)> velocity=<\s?([-\d]+),\s+([-\d]+)>')

class Point:
    def __init__(self,inputstring):
        m = re_parsePt.search(inputstring)
        self.x = int(m[1])
        self.y = int(m[2])
        self.xdot = int(m[3])
        self.ydot = int(m[4])
        self.xstart = self.x
        self.ystart = self.y
        self.neighbors = 0
    def __str__(self):
        return "[x={},{} v={},{} n={}]".format(self.x, self.y, self.xdot, self.ydot, self.neighbors)        
    def __repr__(self):
        return "[x={},{} v={},{} n={}]".format(self.x, self.y, self.xdot, self.ydot, self.neighbors)
    def calcPointAtTime(self,time):
        return (self.xstart + self.xdot*time, self.ystart + self.ydot*time)
    def incrementTime(self, seconds):
        self.x += self.xdot*seconds
        self.y += self.ydot*seconds
        self.neighbors = 0
    def isAdjacent(self, anotherPt):
        if (self.x == anotherPt.x) and (abs(self.y-anotherPt.y)<=1):
            return True
        if (self.y == anotherPt.y) and (abs(self.x - anotherPt.y)<=1):
            return True
        return False



with open('day10.dat') as datafile:
    alldata = [ Point(x.strip()) for x in datafile.readlines()]

testdatastring= """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""

testdata = [ Point(x.strip()) for x in testdatastring.splitlines()]

#alldata = testdata

def countNeighbors(allpts):
    hist  = {}
    xmin = 100
    ymin = 100
    xmax = 0
    ymax = 0
    for pt in allpts:
        hist[pt.neighbors] = hist.get(pt.neighbors,0) + 1
        if (pt.x < xmin):
            xmin = pt.x
        if (pt.x > xmax):
            xmax = pt.x
        if (pt.y < ymin):
            ymin = pt.y
        if (pt.y > ymax):
            ymax = pt.y

    return hist, xmin, xmax, ymin, ymax

#start in the middle somewhere
STARTTIME = 10000
for pt in alldata:
    pt.incrementTime(STARTTIME-1)

xbounds_last = 10000000000
ybounds_last = 10000000000

MAXTIME = 15000
for itime in range(STARTTIME,MAXTIME):
    for aPt in alldata:
        aPt.incrementTime(1)
    
    for (pt1,pt2) in itertools.permutations(alldata,2):
        if pt1.isAdjacent(pt2):
            pt1.neighbors += 1
            pt2.neighbors += 1

    (neighborcount,xstart,xmax,ystart,ymax) = countNeighbors(alldata)
    xbounds = xmax-xstart
    ybounds = ymax-ystart
    print("Time={} xbounds={} NeighborDist={}".format(itime,xbounds,neighborcount))
    #if not (0 in neighborcount) or neighborcount[0]==0:
    #if (xbounds < xbounds_best):
    if (xbounds > xbounds_last):
        print("POTENTIAL MESSAGE AT TIME ",itime-1)
        xstart -= 1
        ystart -= 1
        xmax += 1
        ymax += 1
        print("     range=[{}-{}, {}-{}]".format(xstart,xmax,ystart,ymax))
        displayarray = np.zeros( (ymax-ystart, xmax-xstart), dtype=int)
        for pt in alldata:
            (myx,myy) = pt.calcPointAtTime(itime-1)
            displayarray[myy-ystart,myx-xstart] = 1

        plt.pcolor(displayarray)
        plt.show()
        exit()
    xbounds_last = xbounds
    ybounds_last = ybounds

#print(alldata)

#fig, ax = plt.subplots()
#displayarray = np.zeros((40,40), dtype=int)
#plt.pcolor(displayarray,animated=True)


#def plot_update(frame):
#    xstart = -15
#    ystart = -15
#    time = int(frame)
#    displayarray = np.zeros((40,40), dtype=int)
#    for pt in alldata:
#        displayarray[pt.x-xstart + pt.xdot*time,pt.y-ystart + pt.ydot*time] = 1
#    dis = plt.pcolor(displayarray,animated=True)
#    return dis,


#ani = FuncAnimation(fig,plot_update,frames=range(5), blit=True)
#plt.show()
