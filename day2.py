
from collections import Counter
from itertools import combinations


with open('day2.dat') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

# Test:  checksum=12
#alldata = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']

twocount = 0
threecount = 0

for thisWord in alldata:
    counts = Counter(thisWord)
    has2 = 0
    has3 = 0
    if 2 in counts.values():
        has2 = 1
    if 3 in counts.values():
        has3 = 1
    twocount += has2
    threecount += has3
    #print(thisWord,has2,has3)

checksum=twocount*threecount

print("PART 1")
print("2count={} 3count={} checksum={}".format(twocount,threecount,checksum))

# PART 2

# Test:  fghij differ fguij by 1
#alldata =['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']

def countDifferences(s1, s2):
    """ 
    Counts the numbers of characters that are different between two equal-length strings
    """
    different = 0
    for aloc in zip(s1,s2):
        if aloc[0] != aloc[1]:
            different += 1
    return different

for apair in combinations(alldata, 2):
    diffs = countDifferences(apair[0],apair[1])
    #print(apair, diffs)
    if diffs == 1:
        print("FOUND IT")
        print(apair[0])
        print(apair[1])
        exit()
    pass

