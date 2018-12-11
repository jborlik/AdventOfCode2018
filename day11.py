import numpy as np

# code input
GRIDSERIAL = 9005


def findPower(ix,iy, gridserial):
    """power at coordinate (ix/iy are one based)"""
    rackID = ix + 10
    powerlevel = rackID*iy + gridserial
    powerlevel *= rackID
    hundreddigit = int((powerlevel % 1000) / 100.0)
    return hundreddigit - 5

print("test1=",findPower(122,79,57))
print("test2=",findPower(217,196,39))
print("test3=",findPower(101,153,71))


# remember that this is 0-based
grid = np.zeros((300,300),dtype=int)

it = np.nditer(grid, flags=['multi_index'], op_flags=['readwrite'])
while not it.finished:
    it[0] = findPower(it.multi_index[0]+1, it.multi_index[1]+1, GRIDSERIAL) #GRIDSERIAL) # 18) #42) #GRIDSERIAL)
    it.iternext()

# now we have the power grid, find the best 3x3

maxsum = 0
maxloc = (0,0,0)
for isize in range(1,300+1):
    print("ISIZE=",isize)
    for ix in range(1,300-isize+1):
        #print("ix=",ix," SUBGRID=\n", grid[ix-1:ix-1+isize,:])

        for iy in range(1,300-isize+1):
            subarray = grid[ix-1:ix-1+isize,iy-1:iy-1+isize] #.sum()
            thesum = np.sum(subarray)
            #print("({},{})\n = {}".format(ix,iy,subarray))
            if thesum > maxsum:
                maxsum = thesum
                maxloc = (ix,iy,isize)
                print("sum={} ({})\n = {}".format(maxsum,maxloc,subarray))

print("Largest sum=",maxsum," at ",maxloc)

