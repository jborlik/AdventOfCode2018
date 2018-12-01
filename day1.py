

with open('day1.dat') as datafile:
    alldata = [int(x.strip()) for x in datafile.readlines()]

frequency = 0

for a in alldata:
    frequency += a

print("Part 1: Resulting frequency=",frequency)

#alldata = [1,-1]  #test1, freq 0
#alldata = [3,3,4,-2,-4]  #test2, freq 10
#alldata = [-6,3,8,5,-6] # test3, freq 5
#alldata = [7,7,-2,-7,-4] # test4, freq 14

frequencies = {0: 1}
frequency = 0
iters = 0
while True:
    for a in alldata:
        frequency += a
        iters += 1
        if (frequency in frequencies):
            print("Part 2:  Duplicated frequency at: ", frequency, " after ", iters," iterations")
            exit()
        frequencies[frequency] = 1


