#!/usr/bin/env python

import argparse, sys
from mtzdd import MTZDD
from constraint import Constraint
        
###
### Command line arguments
###

parser = argparse.ArgumentParser()
parser.add_argument('--quiet', '-q', action='store_true')
parser.add_argument('input', default=sys.stdin, type=argparse.FileType('r'), 
                    nargs='?', help='input filename')
parser.add_argument('-o', '--output', default=sys.stdout, type=argparse.FileType('w'), 
                    nargs='?', help='output filename')
parser.add_argument('--type', default='egalitarian', choices=['egalitarian', 'elitist', 'minmaxmin'],
                    help='problem type')
args = parser.parse_args()

if not args.quiet:
    print "\033[1;34mCSG MIP Problem Generator for MTZDD Representation\033[0m"
    print ""
    print "           Input file: \033[1;33m", args.input.name, "\033[0m"
    print "          Output file: \033[1;33m", args.output.name, "\033[0m"
    print "          File format: \033[1;33m", args.format, "\033[0m"
    print "         Problem type: \033[1;33m", args.type, "\033[0m"
    print ""


###
### Read input file
###

ifile = args.input
line = ifile.read()
mtzdd = MTZDD.fromString(line)
ifile.close()

###
### Generate constraints
###

constr = []

obj = "objective"
    
###
### Write output
###
    
ofile = args.output

ofile.write(obj)
ofile.write("\n")
ofile.write("Subject To\n")

for c in constr:
    ofile.write(str(c) + '\n')

ofile.write("Binary\n")


ofile.close()
