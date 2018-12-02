# AdventOfCode2018

Python code to solve daily puzzles of http://adventofcode.com/2018

Code is tested with Python 3.6.6 (Anaconda distribution) on Win10.  Developed with VSCode.

## Days
* Day 1:  Search for repeated results from an iterated list, which requires keeping track of the results.  The duplicated result was after 138573 iterations, so all of the previous values had to be kept and searched each iteration.  This required a sorted collection with an efficient search.  The dictionary object worked fine.
* Day 2:  First part involved letter frequencies, which can be easily done via collections.Counter.  The second part required comparing each pair of strings, looking for a pair that had only one diffence.  Itertools.combinations to the rescue.  


## See previous work at:
* https://github.com/jborlik/AdventOfCode2015
* https://github.com/jborlik/AdventOfCode2016
* https://github.com/jborlik/AdventOfCode2017
