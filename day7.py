#import re
#import numpy as np

with open('day7.dat') as datafile:
    alldata = [ (x[5],x[36]) for x in datafile.readlines()]

steptimebase = 60


# test:   CABDFE
testdata = [ ('C','A'), ('C','F'),('A','B'),('A','D'),('B','E'),('D','E'),('F','E')]
workers = [ [0,0], [0,0] ] # for test

#steptimebase = 0
#alldata = testdata

class Worker:
    def __init__(self):
        self.currentNode = None
        self.remainingTime = 0
    def __repr__(self):
        if self.currentNode == None:
            return "[No work]"
        else:
            return "[Working. Node={} remaining time={}]".format(self.currentNode.name,self.remainingTime)

workers = [ Worker(), Worker(), Worker(), Worker(), Worker() ]
#workers = [ Worker(), Worker() ]

class Node:
    def __init__(self,sname):
        self.name = sname
        self.parents = {}
        self.children = {}
        self.value = ord(sname[0]) - ord('A') + 1
    def addParent(self,parentNode):
        self.parents[parentNode.name] = parentNode
        parentNode.children[self.name] = self
    def __str__(self):
        return "{}: parents={} children={}\n".format(self.name, self.parents, self.children)        
    def __repr__(self):
        return "{}".format(self.name)        

nodes = {}
def getOrCreateNode(sName,nodes):
    if sName in nodes:
        return nodes[sName]
    newnode = Node(sName)
    nodes[sName] = newnode
    return newnode


for aIns in alldata:
    sourceNode = getOrCreateNode(aIns[0],nodes)
    destNode = getOrCreateNode(aIns[1],nodes)
    destNode.addParent(sourceNode)

# we now have the connected network of steps

def solvePart1():
    startNodes = []
    for _,aNode in nodes.items():
        if len(aNode.parents) == 0:
            startNodes.append(aNode)

    order = []
    while len(startNodes) > 0:
        startNodes = sorted(startNodes, key=lambda x: x.name)
        print(startNodes)
        aNode = startNodes.pop(0)
        order.append(aNode)
        for _, childNode in aNode.children.items():
            del childNode.parents[aNode.name]
            if len(childNode.parents) == 0:
                startNodes.append(childNode)

    orderstringlist = []
    for aNode in order:
        orderstringlist.append(aNode.name)

    orderstring = "".join(orderstringlist)

    print("orderstring=",orderstring)

def workersAreComplete(workerlist):
    for aworker in workerlist:
        if aworker.currentNode != None:
            return False
    return True

def loadWorkers(workerlist, availablenodes):
    for aWorker in workerlist:
        if aWorker.currentNode == None:  # no current assignment
            if len(availablenodes) > 0:
                aNode = availablenodes.pop(0)
                aWorker.currentNode = aNode
                aWorker.remainingTime = steptimebase + aNode.value # remaining time

def incrementTime(workerlist, availablenodes):
    for aWorker in workerlist:
        if aWorker.currentNode != None:
            aWorker.remainingTime -= 1
            if aWorker.remainingTime == 0:
                for _, childNode in aWorker.currentNode.children.items():
                    del childNode.parents[aWorker.currentNode.name]
                    if len(childNode.parents) == 0:
                        availablenodes.append(childNode)
                aWorker.currentNode = None
                
def solvePart2():
    startNodes = []

    for _,aNode in nodes.items():
        if len(aNode.parents) == 0:
            startNodes.append(aNode)

    loadWorkers(workers,startNodes)

    # we now have available nodes and workers
    # start incrementing the clock
    time = 0
    
    while (not workersAreComplete(workers)) or len(startNodes) > 0:
        print("Time {}: {}".format(time,workers))
        incrementTime(workers,startNodes)
        time += 1
        startNodes = sorted(startNodes, key=lambda x: x.name)
        loadWorkers(workers,startNodes)

    print("Time to completion: ", time)

#solvePart1()
solvePart2()

