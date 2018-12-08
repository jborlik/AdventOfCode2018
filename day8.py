#import re
#import numpy as np


with open('day8.dat') as datafile:
    alldata = [int(x) for x in datafile.readline().split()]

testdata = [int(x) for x in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()]

# test:  sum of metadata entries = 138
#alldata = testdata

class Node:
    def __init__(self):
        self.children = []
        self.metadata = []
    
    def parseList(self, itemlist):
        numchildren = itemlist.pop(0)
        nummeta = itemlist.pop(0)
        #print("numchildren={} nummeta={}".format(numchildren,nummeta))
        for _ in range(numchildren):
            newnode = Node()
            newnode.parseList(itemlist)
            self.children.append(newnode)
        for _ in range(nummeta):
            self.metadata.append( itemlist.pop(0) )

    def recursiveSumMetadata(self):
        thevalue = sum(self.metadata)
        for aChild in self.children:
            thevalue += aChild.recursiveSumMetadata()
        return thevalue

    def calcValue(self):
        thevalue = 0
        if len(self.children)==0:
            thevalue = sum(self.metadata)
            #print("node has no children, value=",thevalue)
        else:
            for areference in self.metadata:
                if (areference > 0) and (areference <= len(self.children)):
                    #print("   checking child ",areference-1)
                    childval = self.children[areference-1].calcValue()
                    #print("         val=",childval)
                    thevalue += childval
        return thevalue

            
parserlist = alldata
root = Node()
root.parseList(parserlist)
checksum = root.recursiveSumMetadata()

print("Checksum=",checksum)

rootvalue = root.calcValue()

print("Value=", rootvalue)
