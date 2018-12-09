#import re
#import numpy as np
import itertools
from blist import blist
# conda install blist

#with open('day9.dat') as datafile:
#    alldata = [ (x[5],x[36]) for x in datafile.readlines()]

numplayers = 452
lastmarble = 7078400

# test:  winning score=32
#testdata = []
#numplayers = 9
#lastmarble = 25

def indexOfIncrement(startIndex, thecircle):
    if len(thecircle)==startIndex+1:
        return 0
    return startIndex + 1

circle = blist([0])
currentmarble = 0
currentplayer = 0
scores = [0] * numplayers

for imarble in range(1,lastmarble+1):
    currentplayer += 1
    if (currentplayer > numplayers):
        currentplayer = 1

    if (imarble % 23)==0:
        # something special
        scores[currentplayer-1] += imarble
        removeindex = currentmarble - 7
        if (removeindex < 0):
            removeindex = len(circle) + removeindex
        scores[currentplayer-1] += circle.pop(removeindex)
        currentmarble = removeindex
    else:
        # the normal:  add marble
        iafter = indexOfIncrement(currentmarble, circle)
        ibefore = indexOfIncrement(iafter,circle)
        circle.insert(iafter+1,imarble)
        currentmarble = iafter+1

    if (len(circle) % 1000) == 0:
        print("Marbles={}.  Max score:{}".format(len(circle),max(scores)))

    
    #print("[{}] curr={}.  Circle={}".format(currentplayer,currentmarble,circle))

print("Marbles={}.  Max score:{}".format(len(circle),max(scores)))
