#import re
#import numpy as np
#import collections

#import matplotlib.pyplot as plt
#import itertools
#from blist import blist
# conda install blist
#re_parseRule = re.compile(r'(.)(.)(.)(.)(.) => (.)')

from utilities import astar

# A* reference:  https://www.redblobgames.com/pathfinding/a-star/implementation.html
# More A* impl:  https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

OPENCHAR = '.'
DEBUGFLAG = False

class Creature:
    def __init__(self, achar, row, col):
        self.type = achar
        self.row = row
        self.col = col
        self.hp = 200
        self.attack = 3
        self.alive = True
    def __str__(self):
        if self.alive:
            return "({} [{},{}] hp={})".format(self.type,self.row,self.col,self.hp)
        return "DEAD"
    def __repr__(self):
        return self.__str__()
    def distanceToOther(self,anothercreature):
        return abs(self.col-anothercreature.col)+abs(self.row-anothercreature.row)
    def openNearSpots(self,themap):
        nearspots = [(-1,0),(0,1),(1,0),(0,-1)] # up, right, down, left
        openspots = []
        for adir in nearspots:
            aspot = (self.row + adir[0], self.col + adir[1])
            if aspot[0] < 0 or aspot[0] >= MAXROWS:
                continue
            if aspot[1] < 0 or aspot[1] >= MAXCOLS:
                continue
            if themap[aspot[0]][aspot[1]] != OPENCHAR:
                continue
            openspots.append(aspot)
        return openspots

    def pathToSpot(self, themap, aspot):
        # OH SWEET LADY OF PERFORMANCE PRAY FOR ME
        # up, left, right, down
        paths = [None,None,None,None]
        if themap[self.row-1][self.col] == OPENCHAR:
            paths[0] = astar(themap,(self.row-1,self.col), aspot, OPENCHAR, False)
        if themap[self.row][self.col-1] == OPENCHAR:
            paths[1] = astar(themap,(self.row,self.col-1), aspot, OPENCHAR, False)
        if themap[self.row][self.col+1] == OPENCHAR:
            paths[2] = astar(themap,(self.row,self.col+1), aspot, OPENCHAR, False)
        if themap[self.row+1][self.col] == OPENCHAR:
            paths[3] = astar(themap,(self.row+1,self.col), aspot, OPENCHAR, False)
        bestlen = 100000
        bestpath = None
        for i in range(4):
            if paths[i] != None:
                if len(paths[i]) < bestlen:
                    bestlen = len(paths[i])
                    bestpath = paths[i]
        return bestpath

        
    def makeMove(self, themap, creatures):
        """Find enemies, move if needed/possible, attack if possible"""
        # identify potential targets
        enemies = []
        for acreature in creatures:
            if acreature.alive and acreature.type != self.type:
                enemies.append(acreature)
        
        if len(enemies)==0:
            return None  # no enemies left, game is probably over

        # are any in already in range?
        target = None
        for aenemy in enemies:
            if self.distanceToOther(aenemy)==1:
                target = aenemy
                break
        
        if not target:
            # identify open spots near targets
            openspots = []
            for aenemy in enemies:
                openspots.extend(aenemy.openNearSpots(themap))

            # find pathes
            spotmap = {}
            shortestnum = 10000
            shortlist = []
            for aspot in openspots:
                if DEBUGFLAG:
                    print("Checking {} against openspot {}".format(self,aspot))
                pathtospot = self.pathToSpot(themap,aspot)
                if pathtospot == None:
                    continue  # no path to item
                if len(pathtospot) == shortestnum:
                    shortlist.append(aspot)
                    spotmap[aspot] = pathtospot
                if len(pathtospot) < shortestnum:
                    shortestnum = len(pathtospot)
                    shortlist = [aspot]
                    spotmap.clear()

                    # Hopefully this gets "reading order" right
                    # temporarily backtrack from destination
                    #themap[self.row][self.col] = OPENCHAR
                    #pathtospot = astar(themap,aspot,(self.row,self.col), OPENCHAR, False)
                    #themap[self.row][self.col] = self.type
                    #pathtospot.reverse()

                    spotmap[aspot] = pathtospot
            # we should now have a list of the shortest (possibly ties)
            # sort spots by "reading order" for this round
            if len(shortlist)==0:
                # no paths to the living targets = no move
                return Creature("N",self.row,self.col)


            shortlist.sort(key=lambda c: c[0]*MAXCOLS+c[1])

            # move
            chosenpath = spotmap[shortlist[0]]
            firststep = chosenpath[0]  # yes, astar returns path with starting at 0, but we've checked the first step already for "reading order"

            if DEBUGFLAG:
                print("{} moving to {} destination {}".format(self,firststep,shortlist[0]))

            themap[self.row][self.col] = OPENCHAR
            self.row =firststep[0]
            self.col =firststep[1]
            themap[self.row][self.col] = self.type

            target = Creature('X',shortlist[0][0],shortlist[0][1])  # kind of a dummy
            target.alive = False

        # attack phase
        # We need to recheck to see which are in range, as we will use a different selection criteria
        adjacentenemies = []
        for aenemy in enemies:
            if self.distanceToOther(aenemy)==1:
                adjacentenemies.append(aenemy)
        if len(adjacentenemies) > 0:
            adjacentenemies.sort(key=lambda c: c.hp*MAXCOLS*MAXROWS + c.row*MAXCOLS + c.col)

            target = adjacentenemies[0]

            if DEBUGFLAG:
                print("{} attacking {} for {}!".format(self,target,self.attack))

            # actually attack
            target.hp -= self.attack

            # death test
            if (target.hp <= 0):
                target.alive = False
                print("** KILLED {} at ({},{})!".format(target.type,target.row,target.col))
                themap[target.row][target.col] = OPENCHAR

               

        return target



def printmap(amap, creatures):
    for ir,row in enumerate(amap):
        print("".join(row),end='')
        print([c for c in creatures if c.alive and c.row==ir])

    
with open('day15.dat') as datafile:
    themap = [ list(x.strip()) for x in datafile.readlines()]

#testmap_str = """#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#   
#######"""  # 27730

testmap_str = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#   
#######"""  # 36334

#testmap_str = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#   
#######"""  # 39514

#testmap_str = """#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######"""  # 27755

#testmap_str = """#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""   # G 28944

testmap_str = """#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########"""   # G 18740

testmap = [ list(x) for x in testmap_str.splitlines()]

#themap = testmap

MAXROWS = len(themap)
MAXCOLS = len(themap[0])

# initialize array of creatures
creatures = []
for irow,row in enumerate(themap):
    for icol, achar in enumerate(row):
        if achar=='G' or achar=='E':
            creatures.append(Creature(achar,irow,icol))

#if DEBUGFLAG:
printmap(themap,creatures)

#print(creatures)

round = 0
while round < 1000:
    round += 1
    # sort creatures by "reading order" for this round
    creatures.sort(key=lambda c: c.row*MAXCOLS+c.col)

    for creature in creatures:
        if creature.alive:
            targetcreature = creature.makeMove(themap,creatures)
            if targetcreature == None:
                print("ALL ENEMIES ARE DEAD")
                lastcompleteround = round-1
                sumhp = 0
                for c in creatures:
                    if c.alive:
                        sumhp += c.hp
                print("{} wins.  Last complete round={}".format(creature.type, round-1))
                print("Sum hp=",sumhp," outcome=",sumhp*lastcompleteround)
                exit()

    print("AFTER ROUND ", round)
#    if DEBUGFLAG:
    printmap(themap,creatures)
            


