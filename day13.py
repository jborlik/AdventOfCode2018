#import re
#import numpy as np
#import collections

#import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
#import itertools
#from blist import blist
# conda install blist
#re_parseRule = re.compile(r'(.)(.)(.)(.)(.) => (.)')

def printmap(themap):
    for row in themap:
        #print("X",end='')
        print("".join(row))#,end='')
        #print("X")


with open('day13.dat') as datafile:
    themap = [ list(x) for x in datafile.readlines()]

testmapstr = r"""/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """
testmap = [ list(x) for x in testmapstr.splitlines()]

#themap = testmap
#printmap(themap)

#                 N      E      S       W
directions = [ (-1,0), (0,1), (1,0), (0,-1) ] 
def turn(curRowDir,curColDir,turnDir):
    iwhich = directions.index( (curRowDir,curColDir) )
    inew = (iwhich + (turnDir-1) + 4) % 4
    return directions[inew] 


# cart: 0=row, 1=col, 2=rowdirection, 3=coldirection, 
#       4=next intersection choice (0=left,1=straight,2=right)
#       5=True/False is alive
carts = []
for irow,row in enumerate(themap):
    for icol,spot in enumerate(row):
        if spot=='^':
            carts.append( (irow,icol,-1,0,0,True) )
            themap[irow][icol] = '|'
        elif spot=='>':
            carts.append( (irow,icol,0,1,0,True))
            themap[irow][icol] = '-'
        elif spot=='v':
            carts.append( (irow,icol,1,0,0,True))
            themap[irow][icol] = '|'
        elif spot=='<':
            carts.append( (irow,icol,0,-1,0,True))
            themap[irow][icol] = '-'

PARTTWO = True
#printmap(themap)
print(carts)

def checkForCollisions(icart,inewrow,inewcol, carts):
    for iOtherCart,othercart in enumerate(carts):
        if othercart[5]==False:
            continue
        if iOtherCart != icart:
            if (othercart[0]==inewrow) and (othercart[1]==inewcol):
                return (True,iOtherCart)
    return (False,0)

for tick in range(1000000):
    carts = sorted(carts, key=lambda cart: cart[0]) # sort by row

    for icart,cart in enumerate(carts):
        if (cart[5] == False):
            continue
        newrow = cart[0] + cart[2]
        newcol = cart[1] + cart[3]
        newrowdir = cart[2]
        newcoldir = cart[3]
        newinterchoice = cart[4]
        newisalive = cart[5]
        newchar = themap[newrow][newcol]
        (didCollide,iothercart) = checkForCollisions(icart,newrow,newcol,carts)
        if didCollide:
            # CRASH
            print("CRASH at tick ",tick,' cart=',icart, ' at ', newcol, newrow)
            if not PARTTWO:
                exit()
            newisalive = False
            carts[iothercart] = (0,0,0,0,0,False)
        elif newchar == '|':
            pass
        elif newchar == '-':
            pass
        elif newchar == '\\':
            if cart[2] != 0: # if heading north/south, turn left
                (newrowdir,newcoldir) = turn(cart[2],cart[3],0)
            else:  #if heading east/west, turn right
                (newrowdir,newcoldir) = turn(cart[2],cart[3],2)
            
        elif newchar == '/':
            if cart[2] != 0: # if heading north/south, turn right
                (newrowdir,newcoldir) = turn(cart[2],cart[3],2)
            else:  #if heading east/west, turn left
                (newrowdir,newcoldir) = turn(cart[2],cart[3],0)

        elif newchar == '+':
            # intersection
            (newrowdir,newcoldir) = turn(cart[2],cart[3],cart[4])
            newinterchoice = (cart[4] + 1) % 3

        else:
            print("new position not recognized...cart={} at ({},{})=\'{}\'".format(icart,newrow, newcol,newchar))

        carts[icart] = (newrow,newcol,newrowdir,newcoldir,newinterchoice,newisalive)
        
        print(carts)

    if PARTTWO:
    # count alive carts
        countalive = 0
        ialivecart = 0
        for i,cart in enumerate(carts):
            countalive += int(cart[5])
            if cart[5]:
                ialivecart = i
        if countalive == 1:
            cart = carts[ialivecart]
            print("Last cart {}, tick={}, pos=({},{})".format(ialivecart,tick,cart[1], cart[0]))
            exit()
    


