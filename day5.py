import re


with open('day5.dat') as datafile:
    alldata = datafile.readline().strip()

# test:  results in 'dabCBAcaDA' len=10
#alldata = 'dabAcCaCBAcCcaDA'


def collapse(theString):   
    sData = list(theString)

    i = 0
    while i+1 < len(sData):
        c1 = sData[i]
        c2 = sData[i+1]
        if abs(ord(c1)-ord(c2)) == 32:
            # found one, remove them and start over
            sData.pop(i+1)
            sData.pop(i)
            i = 0
        else:
            i += 1
            
    print("Resulting stringlen=",len(sData)) #,' string=',''.join(sData))

#print("PART 1")
#collapse(alldata)

for removechar in range(65,91):
    removechars = chr(removechar) + '|' + chr(removechar+32)
    newstring = re.sub(removechars, '', alldata)

    print("Removing:",removechars) #," from:",newstring)
    collapse(newstring)




