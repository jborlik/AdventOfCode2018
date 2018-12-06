#import re
import numpy as np

with open('day6.dat') as datafile:
    alldata = [x.replace(" ","").strip().split(",") for x in datafile.readlines()]

for pt in alldata:
    pt[0] = int(pt[0])
    pt[1] = int(pt[1])

testdata = [[1,1], [1,6], [8,3], [3,4], [5,5], [8,9]]

#alldata = testdata

maxx = 0
maxy = 0
for pt in alldata:
    if pt[0] > maxx:
        maxx = pt[0]+1
    if pt[1] > maxy:
        maxy = pt[1]+1

print("Array sizes: ",maxx,maxy)

def distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

locations = np.zeros((maxx,maxy), dtype=int)

# loop over the whole array
it = np.nditer(locations, flags=['multi_index'], op_flags=['readwrite'])
while not it.finished:
    minid = 0
    minval= 1000
    for (ipt,pt) in enumerate(alldata):
#       if (it.multi_index[0] == pt[0]) and (it.multi_index[1] == pt[1]):
#           minid = ipt
        dpt = distance(it.multi_index[0], it.multi_index[1], pt[0], pt[1])
        if dpt < minval:
            minid = ipt
            minval = dpt
        elif dpt == minval:
            minid = -1
    it[0] = minid
    it.iternext()

# okay, now each location has its closest point
print(locations)

# filter out the pts on the border
finitespaces = list(range(0,len(alldata)))
for ix in range(0,maxx):
    try:
        finitespaces.remove(locations[ix,0])
    except:
        pass
    try:
        finitespaces.remove(locations[ix,maxy-1])
    except:
        pass
for iy in range(0,maxy):
    try:
        finitespaces.remove(locations[0,iy])
    except:
        pass
    try:
        finitespaces.remove(locations[maxx-1,iy])
    except:
        pass
    
print("finitespaces:",finitespaces)

maxspacevalue = 0
maxspaceid = 0
for aspace in finitespaces:
    aspacecount = (locations == aspace).sum()
    if aspacecount > maxspacevalue:
        maxspacevalue = aspacecount
        maxspaceid = aspace

print("Max count=",maxspacevalue," for ID=",maxspaceid)


print("PART TWO!")

locations = np.zeros((maxx,maxy), dtype=int)

# loop over the whole array
it = np.nditer(locations, flags=['multi_index'], op_flags=['readwrite'])
while not it.finished:
    sumdist = 0
    for (ipt,pt) in enumerate(alldata):
        dpt = distance(it.multi_index[0], it.multi_index[1], pt[0], pt[1])
        sumdist += dpt
    if sumdist < 10000:
        it[0] = 1
    it.iternext()

print("Locations < 10000:", locations.sum())