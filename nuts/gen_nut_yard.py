#!/usr/bin/env python3

import sys
import argparse
import random
import math

parser = argparse.ArgumentParser(
	description = 'Generates random yards of acorns given its parameters.',
	formatter_class=argparse.ArgumentDefaultsHelpFormatter
	)
parser.add_argument('-s', '--size', type = int, default = 10, help = 'Integer size and size of the yard > 1')
parser.add_argument('-f', '--fill', type = float, default = 0.15, help = 'Percentage of acorn fill (0--1] = acorn_count / cells_in_yard')
parser.add_argument('-of', '--outfile', type = argparse.FileType('w'), default = 'yard.dat', help = 'Output file name')
args = parser.parse_args()

arg_errors = False

if args.size <= 0:
	print('\nsize must be > 1')
	arg_errors = True

if args.fill <= 0.0 or args.fill > 1.0:
	print('\nfile must be (0--1]')
	arg_errors = True

if args.outfile.closed:
	print('\nThe file is closed for some reason')
	arg_errors = True

if arg_errors:
	print('')
	parser.print_help()
	sys.exit(1)

size = args.size
fill = args.fill
f = args.outfile

yard = [None] * size
for i in range(size):
	yard[i] = [0] * size

acorns = int(fill * size * size)

x = random.randint(0, size - 1)
y = random.randint(0, size - 1)

# place the squirrel randomly
yard[x][y] = -1;

for i in range(acorns):
	while 1:
		x = random.randint(0, size - 1)
		y = random.randint(0, size - 1)
		if yard[x][y] >= 0 and yard[x][y] < 9: #don't go over 1 digit
			break;
	yard[x][y] += 1;

def mark_pile(yard, size, x, y):
	if 0 <= x < size and 0 <= y < size and yard[x][y] > 0:
		yard[x][y] = 0
		mark_pile(yard, size, x-1, y)
		mark_pile(yard, size, x, y-1)
		mark_pile(yard, size, x, y+1)
		mark_pile(yard, size, x+1, y)

piles = 0

yard_copy = [yard[i][:] for i in range(size)]

for y in range(size):
	for x in range(size):
		if yard_copy[x][y] > 0:
			mark_pile(yard_copy, size, x, y)
			piles += 1

f.write('{0} {1}\n'.format('size', size))
f.write('{0} {1}\n'.format('acorns', acorns))
f.write('{0} {1}\n'.format('piles', piles))

for y in range(size):
	for x in range(size):
		cell = yard[x][y]
		if cell == 0:  f.write("."),
		elif cell > 0: f.write(str(cell)),
		else:          f.write("@"),
	f.write("\n")
