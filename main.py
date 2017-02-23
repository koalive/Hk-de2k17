#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################### Help ####################################
"""Hash code 2017
Usage:
  main.py <file>
  main.py --help

Options:
  -h --help          Show this screen.

"""
################################### Imports ###################################
from docopt import docopt
import numpy as np

################################### Objects ###################################

################################## Functions ##################################

##################################### Main ####################################
arguments = docopt(__doc__)

input_file = open(arguments["<file>"], "r").read().splitlines()

# V = nb of videos
# E = nb of endpoints
# R = nb of requests
# C = nb of cache servers
# X = capacity of each server in Mb
V, E, R, C, X = [int(i) for i in input_file[0].split()]

# Size of each video in Mb
S = np.array([int(i) for i in input_file[1].split()])

# Endpoint description
parser = 2
LD = np.empty(E, dtype='int16')
K = np.empty(E, dtype='int16')
connectionsDicts = [{} for i in range(E)]
for i in range(E):
	LD[i], K[i] = [int(i) for i in input_file[parser].split()]
	parser += 1
	assert LD[i] <= 4000 and LD[i] >= 2
	for j in range(K[i]):
		c, LC = [int(i) for i in input_file[parser].split()]
		parser += 1
		assert c >= 0 and c <= C
		assert LC >= 1 and LC <= 500
		connectionsDicts[i][c] = LC

# Request description
Rmat = np.empty([R,3], dtype='int16')
for i in range(R):
	Rv, Re, Rn = [int(i) for i in input_file[parser].split()]
	parser += 1
	assert Rv >= 0 and Rv < V
	assert Re >= 0 and Re < E
	assert Rn >= 0 and Rn <= 10000
	Rmat[i] = [Rv, Re, Rn]
