# AdventOfCode2018

Python code to solve daily puzzles of http://adventofcode.com/2018

Code is tested with Python 3.6.6 (Anaconda distribution) on Win10.  Developed with VSCode.

## Days
* Day 1:  Search for repeated results from an iterated list, which requires keeping track of the results.  The duplicated result was after 138573 iterations, so all of the previous values had to be kept and searched each iteration.  This required a sorted collection with an efficient search.  The dictionary object worked fine.
* Day 2:  First part involved letter frequencies, which can be easily done via collections.Counter.  The second part required comparing each pair of strings, looking for a pair that had only one diffence.  Itertools.combinations to the rescue.  
* Day 3:  Used a class to store/parse data (via regex) for a rectangle.  Used a numpy matrix to store values where the rectangles overlapped.  Iterated through that large matrix a couple of times, although it was simplified with np.where.
* Day 4:  Datetime for time differences, although this may have been overkill.  Sort and iterate over an event log, keeping track of which
minutes were spent sleeping by each individual guard.
* Day 5:  Collapsing a (very long) string by matching letters, and then (part 2) collapsing it after removing each letter of the alphabet.  I don't think that I implemented it in as time-efficient way as possible, as each "collapsing" took a couple of minutes.  But, brute force worked for a non-competitive entry.  I had started out by trying to implement something where the string/list length wouldn't be altered (i.e. replace chars with a sentinel) but abandoned it when I started converting the string to a list first.  (I wrongly thought list item removal was O(1).)
* Day 6:  On a grid, found the area of influence for a particular point (for Part 1), and the area with a total distance to all points less than a critical value.  This one
involved iterating through numpy arrays.
* Day 7:  Had to figure out a graph of process, and then the order to do the steps.  Used a class for a node (step of the process) with multiple parents and multiple children.  Part two had another structure for workers, and a simulation of parallel
work.  Took a bit longer than others.
* Day 8:  Used a little class to model a directed graph, parsed recursively and inspected recursively.
* Day 9:  Adding/removing to a list.  Part 1 finished quickly, but Part 2 was taking forever, due to the expense of Python adding/removing to the middle of a list.  (Is this a theme?)  A hint from the reddit suggested the package "blist" (i.e. "conda install blist"), and the x100 size array finished very quickly.
* Day 10:  Interesting problem to simulate particles moving and then figure out what they are writing out.  There isn't a good way for the machine to identify something as text, at least in a time-efficient way, so there needed to be a way to terminate the processing and display the results.  My first attempt was to count the number of particle neighbors... I thought that when every particle had a neighbor the text would be visible.  I counted neighbors as up/down/right/left, and maybe if I would have included diagonals it would have worked.  Based on a hint from reddit, in the next attempt I looked for the minimum bounding box... This worked.  I used matplotlib to display.
* Day 11:  Fill out a grid with computed values, and then look for the maximum submatrices.  The first part (3x3 submatrices) worked fine after I remembered some of the numpy indexing.  The second part took a while to figure out, as I was missing the examination of the last column.



## See previous work at:
* https://github.com/jborlik/AdventOfCode2015
* https://github.com/jborlik/AdventOfCode2016
* https://github.com/jborlik/AdventOfCode2017
