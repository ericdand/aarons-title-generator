#!/usr/bin/env python

import argparse, random

parser = argparse.ArgumentParser(description="Generates the name of the next GiSHWheS hybridized mascot animal.")
parser.add_argument(("-f", "--file"), nargs=1, action='store')

animals = [
		"bear",
		"el>e<phant",
		"oct>o<pus",
		"pig",
		"cat",
		"din>o<saur",
		"mite",
		"wolf",
		"r>oo<ster"]

left = random.choice(animals)
right = left
while (right == left):
	right = random.choice(animals)

if ('<' in left):
	left = left.replace('>', '').split('<')[0]
elif ('|' in left):
	parts = left.split('|')
	index = random.randint(0, len(parts))
	left = ''.join(parts[:index])

if ('>' in right):
	right = right.replace('<', '').split('>')[1]
if ('|' in right):
	parts = right.split('|')
	index = random.randint(0, len(parts))
	right = ''.join(parts[index:])

print("{}{}".format(left, right))

