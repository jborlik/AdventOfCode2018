
import re
import numpy as np

re_parseClaim =re.compile(r'#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)')

class Claim:
    def __init__(self, lineToParse):
        self.left = 0
        self.top = 0
        self.width = 0
        self.height = 0
        self.id = ''
        bunch1 = re_parseClaim.match(lineToParse)
        self.id = bunch1[1]
        self.left = int(bunch1[2])
        self.top = int(bunch1[3])
        self.width = int(bunch1[4])
        self.height = int(bunch1[5])
        pass

    def __str__(self):
        return "{},{} {}x{}\n".format(self.left, self.top, self.width, self.height)        


with open('day3.dat') as datafile:
    alldata = [Claim(x.strip()) for x in datafile.readlines()]

# TEST:  num>2 = 4
#testdata = ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4','#3 @ 5,5: 2x2']
#alldata = [Claim(x) for x in testdata]

CLOTHSIZE=1000
wholecloth = np.zeros( (CLOTHSIZE,CLOTHSIZE), dtype=int)

for aclaim in alldata:
    for i in np.arange(aclaim.width):
        for j in np.arange(aclaim.height):
            wholecloth[aclaim.left+i,aclaim.top+j] += 1

numgreaterthan2 = wholecloth[ np.where(wholecloth >= 2) ].size
print("Num > 2: ",numgreaterthan2)
#print(wholecloth)
#print(wholecloth[ np.where(wholecloth >= 2) ])

for aclaim in alldata:
    unique = True
    for i in np.arange(aclaim.width):
        for j in np.arange(aclaim.height):
            if (wholecloth[aclaim.left+i,aclaim.top+j] != 1):
                unique = False
    if (unique):
        print("UNIQUE: id=",aclaim.id)
