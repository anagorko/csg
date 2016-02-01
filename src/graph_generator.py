#!/usr/bin/env python

import argparse, sys, os, sqlite3

###
### Command line
###

parser = argparse.ArgumentParser()
parser.add_argument('--quiet', '-q', action='store_true')
parser.add_argument('--directory', help='output directory', action='store', default='../experiments')
args = parser.parse_args()

directory = args.directory + '/'

if not args.quiet:
    print "\033[1;34mGraph Generator\033[0m"
    print ""
    print "   Directory: \033[1;33m", directory, "\033[0m"

###
### Connect to the database
###

conn = sqlite3.connect(directory + '/csg_problems.db')
conn.isolation_level = None

###
### Enable math extensions
###

conn.enable_load_extension(True)
conn.load_extension("src/libsqlite_math.so")

cur = conn.cursor()

###
### Read data
###

cur.execute('select * from problems')

row = cur.fetchall()

