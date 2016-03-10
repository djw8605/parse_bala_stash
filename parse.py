#!/usr/bin/python

import re
import csv
import sys

#2016-03-09:   1457556301
#Number of dirs at stash-public= 1
#Number of dirs at cvmfs-public= 1
#difference in number of dirs between stash and cvmfs
#difference in number of dirs= 0, unixtime= 1457556301
#Number of files at stash-public= 4
#Number of files at cvmfs-public= 1
#difference in number of files between stash and cvmfs
#difference in number files= 3, unixtime= 1457556301


input_file = sys.argv[1]
output_file = sys.argv[2]
csv_f = open(output_file, 'w')

fieldnames = [ 'seconds', 'date', 'difference' ]
csv_out = csv.DictWriter(csv_f, fieldnames = fieldnames)
csv_out.writeheader()

def dump_line(run):
    if not run:
        return
    csv_out.writerow(run)

# First, grab the date and seconds
date_re = re.compile("^(\d{4}\-\d{2}\-\d{2}):\s+(\d+)$")
difference_re = re.compile("^difference in number files=\s+(\d+),.*")
f = open(input_file, 'r')
run = {}
for line in f:
    match = date_re.search(line)
    if match:
        # This is the first line, so dump the previous
        dump_line(run)
        print match.groups()
        run['date'] = match.group(1)
        run['seconds'] = match.group(2)

    match = difference_re.search(line)
    if match:
        print match.groups()
        run['difference'] = match.group(1)

# also, dump the last line
dump_line(run)

