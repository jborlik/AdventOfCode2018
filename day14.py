
maxreceipes = 190221
#maxreceipes = 2018
maxreceipes_str='190221'
#maxreceipes_str='19022' # 5.8M rounds
#maxreceipes_str='59414'
#maxreceipes_str='704321'

receipes = [3,7]
elf_current = [0,1]

round = 1
#while len(receipes) < maxreceipes+10:
while maxreceipes_str not in "".join(str(x) for x in receipes[-10:]):#True:
#    if len(receipes)>(len(maxreceipes_str)+1):
#        lastseven= "".join(str(x) for x in receipes[-(len(maxreceipes_str)+1):])
#        if lastseven[-(len(maxreceipes_str)):] == maxreceipes_str:
#            break
#        if lastseven[1:] == maxreceipes_str:
#            break

    round += 1
    sumdigs = receipes[elf_current[0]] + receipes[elf_current[1]]
    if sumdigs >= 10:
        receipes.append(1)  # tens
    receipes.append(sumdigs % 10)  # ones digit
    
    elf_current[0] = (elf_current[0] + 1 + receipes[elf_current[0]]) % len(receipes)
    elf_current[1] = (elf_current[1] + 1 + receipes[elf_current[1]]) % len(receipes)

    if (round % 100000 == 0):
        print("Round=",round)
    #print("t={} e1={} e2={}:  {}".format(round,elf_current[0],elf_current[1], " ".join(str(x) for x in receipes)))

print("".join(str(x) for x in receipes[-10:]))

print("Round={} len={}".format(round,len(receipes)))
print("{} receipes before {}".format(len(receipes)-len(maxreceipes_str), maxreceipes_str))

# 20268577 receipes before 190221
