#import re
#import numpy as np
#import collections
from copy import deepcopy  # deepcopy
#import matplotlib.pyplot as plt
#import itertools
#from blist import blist
# conda install blist
#re_parseRule = re.compile(r'(.)(.)(.)(.)(.) => (.)')

def getadjacents(themap, irow, icol):
    ptradjacents = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    adjacents = []
    for ptr in ptradjacents:
        if (irow+ptr[0]) >= 0 and (icol+ptr[1]) >= 0:
            if (irow+ptr[0]) < len(themap)  and (icol+ptr[1]) < len(themap[irow]):
                adjacents.append(themap[irow+ptr[0]][icol+ptr[1]])
    return adjacents



with open('day18.dat') as datafile:
    themap = [ list(x.strip()) for x in datafile.readlines()]

testmap_str = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""
testmap = [ list(x.strip()) for x in testmap_str.splitlines()]

#themap = testmap

time = 0

fout = open('day18.out', 'w')

while time < 10000:
    time += 1

    newmap = deepcopy(themap)
    for irow, row in enumerate(themap):
        for icol, achar in enumerate(row):
            adj = getadjacents(themap,irow,icol)
            if achar=='.': # open
                if len([c for c in adj if c=='|']) >= 3:
                    newmap[irow][icol] = '|'
            elif achar=='|': # trees
                if len([c for c in adj if c=='#']) >= 3:
                    newmap[irow][icol] = '#'
            elif achar=='#': # lumberyard
                newmap[irow][icol] = '.'
                if len([c for c in adj if c=='|']) >= 1:
                    if len([c for c in adj if c=='#']) >= 1:
                        newmap[irow][icol] = '#'
    
    themap = newmap
    if time > 1000: #and time % 10000 == 0:
#        print("AT TIME ",time)
#        for row in themap:
#            print("".join(row))

        numwooded = 0
        numlumber = 0
        for row in themap:
            for spot in row:
                if spot=='#':
                    numlumber += 1
                elif spot=='|':
                    numwooded += 1
                    
        fout.write("Time={}, {} wooded, {} lumberyard = {}\n".format(time,numwooded,numlumber,numwooded*numlumber))


print("{} wooded, {} lumberyard = {}".format(numwooded,numlumber,numwooded*numlumber))

        
