from datetime import datetime,timedelta
import re
import operator
import numpy as np

#re_parsedate =re.compile(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\]')
re_parseguard = re.compile(r'Guard #(\d+)')


with open('day4.dat') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]
alldata.sort()

testdata = [
'[1518-11-01 00:00] Guard #10 begins shift',
'[1518-11-01 00:05] falls asleep',
'[1518-11-01 00:25] wakes up',
'[1518-11-01 00:30] falls asleep',
'[1518-11-01 00:55] wakes up',
'[1518-11-01 23:58] Guard #99 begins shift',
'[1518-11-02 00:40] falls asleep',
'[1518-11-02 00:50] wakes up',
'[1518-11-03 00:05] Guard #10 begins shift',
'[1518-11-03 00:24] falls asleep',
'[1518-11-03 00:29] wakes up',
'[1518-11-04 00:02] Guard #99 begins shift',
'[1518-11-04 00:36] falls asleep',
'[1518-11-04 00:46] wakes up',
'[1518-11-05 00:03] Guard #99 begins shift',
'[1518-11-05 00:45] falls asleep',
'[1518-11-05 00:55] wakes up' ]
testdata.sort()

#alldata = testdata

activeguard = ''
isasleep = False
sleepstart = datetime.now()

guards = {}
guardminute = {}

for event in alldata:
    timestamp = datetime.strptime(event[1:17],'%Y-%m-%d %H:%M')

    if event.endswith('begins shift'):
        # new guard
        m = re_parseguard.search(event)
        activeguard = m[0]
        sleepstart = 0
        if not (activeguard in guards):
            guards[activeguard] = 0
            guardminute[activeguard] = np.zeros(60)
    elif event.endswith('wakes up'):
        sleeptime = timestamp - sleepstart
        guards[activeguard] += int(sleeptime.total_seconds()/60)
        print("Guard {} slept {} (total {})".format(activeguard,int(sleeptime.total_seconds()/60),guards[activeguard]))
        startmin = sleepstart.minute
        endmin = timestamp.minute
        guardminute[activeguard][startmin:endmin] += 1
        pass
    elif event.endswith('falls asleep'):
        sleepstart = timestamp
        pass
    else:
        print("what?", event)
        exit()

sleepguard = max(guards.items(), key=operator.itemgetter(1))[0]

print("Guard with the most sleeptime: ", sleepguard, " for ", guards[sleepguard])

for (v1,v2) in zip(np.arange(0,60), guardminute[sleepguard]):
    print("Minute {}: {}".format(v1,v2))

print("Maximum sleep minute for guard ",sleepguard,": ", np.argmax(guardminute[sleepguard]))

highestguard = ''
highestminute = 0
highesttimes = 0

for aGuard in guards.keys():
    thishighmin = np.argmax(guardminute[aGuard])
    thishightimes = guardminute[aGuard][thishighmin]
    if (thishightimes > highesttimes):
        highestguard = aGuard
        highestminute = thishighmin
        highesttimes = thishightimes

print("Guard {} slept on min {} most ({} times)".format(highestguard,highestminute,highesttimes))
