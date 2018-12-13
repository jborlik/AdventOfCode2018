import re
import numpy as np
import collections

#import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
#import itertools
#from blist import blist
# conda install blist
#re_parsePt =re.compile(r'position=<\s?([-\d]+),\s+([-\d]+)> velocity=<\s?([-\d]+),\s+([-\d]+)>')
re_parseRule = re.compile(r'(.)(.)(.)(.)(.) => (.)')

def charToBin(aChar):
    if aChar == '#':
        return 1
    return 0

class Rule:
    def __init__(self, inputstring):
        m = re_parseRule.match(inputstring)
        self.rule = [m[1], m[2], m[3], m[4], m[5]]
        self.result = charToBin(m[6])
        for ichar,achar in enumerate(self.rule):
            self.rule[ichar] = charToBin(achar)
    def __str__(self):
        return "{} => {}".format(self.rule, self.result)
    def __repr__(self):
        return "{} => {}".format(self.rule, self.result)


def printstate(stateArr, zeroindex, time):
    print("Time={}, zero={}: ".format(time,zeroindex),end='')
    for v in stateArr:
        print(v,end='')
    print("")

def arrsEqual(arr1,arr2):
    if len(arr1) != len(arr2):
        print("ARRAYS DIFFERENT SIZES",len(arr1),len(arr2))
        exit()
    for i,a1 in enumerate(arr1):
        if a1 != arr2[i]:
            return False
    return True

# I modified the input file to only contain the rules
with open('day12.dat') as datafile:
    rulesdata = [ Rule(x.strip()) for x in datafile.readlines()]

initialstate_str = '###.#..#..##.##.###.#.....#.#.###.#.####....#.##..#.#.#..#....##..#.##...#.###.#.#..#..####.#.##.#'

testrules = """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""
testrulesdata = [ Rule(x.strip()) for x in testrules.split("\n") ]
test_initialstate_str = "#..#.#..##......###...###"

#initialstate_str = test_initialstate_str
#rulesdata = testrulesdata

state = collections.deque()
zeroindex = 0
for iLoc,aChr in enumerate(initialstate_str):
    state.append(charToBin(aChr))

printstate(state, zeroindex, 0)

def getvalue(stateArr, index):
    if (index < 0):
        return 0
    if (index >= len(stateArr)):
        return 0
    return stateArr[index]

def sumPlants(stateArr, zeroindex):
    sum = 0
    for index,item in enumerate(stateArr):
        if (item):
            sum += index - zeroindex
    return sum


# iterate over time
maxtime = 50000000000  # part1=20
for time in range(1,maxtime+1):
    # apply the rules
    newstate = state.copy()
    newzero = zeroindex
    if (arrsEqual([newstate[0], newstate[1]], [0,0])):
        newstate.popleft()
        newstate.popleft()
        newzero -= 2
    if (newstate[0]==1) and (newstate[1]==1):
        newstate.insert(0,0)
        newzero += 1
    if (newstate[len(newstate)-1]==1):
        newstate.append(0)

    for index,theItem in enumerate(newstate):
        oldindex = index + zeroindex - newzero
        neighbors = [getvalue(state, oldindex-2), getvalue(state, oldindex-1), 
                    theItem, 
                    getvalue(state, oldindex+1), getvalue(state, oldindex+2)]
        gotit = False
        for aRule in rulesdata:
            if arrsEqual(aRule.rule, neighbors):
                newstate[index] = aRule.result
                gotit = True
                break
        if not gotit:
            newstate[index] = 0
    state = newstate
    zeroindex = newzero
    if (time % 10000)==0:
        printstate(state,zeroindex,time)
        sum = sumPlants(state,zeroindex)
        print("Sum plants=",sum)

    
sum = sumPlants(state,zeroindex)
print("Sum plants=",sum)



