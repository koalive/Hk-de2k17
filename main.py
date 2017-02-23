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
# X becomes the storage in each cache server
X = [X]*C

# Size of each video in Mb
S = np.array([int(i) for i in input_file[1].split()])

# Endpoint description
parser = 2
LD = np.empty(E, dtype='int16')
K = np.empty(E, dtype='int16')
connections = [] # For each endpoint, each connections, formatted as [cache ID, latency]
for i in range(E):
	LD[i], K[i] = [int(i) for i in input_file[parser].split()]
	parser += 1
	assert LD[i] <= 4000 and LD[i] >= 2
	latmat = np.empty([K[i], 2], dtype='int16')
	for j in range(K[i]):
		c, LC = [int(i) for i in input_file[parser].split()]
		parser += 1
		assert c >= 0 and c <= C
		assert LC >= 1 and LC <= 500
		latmat[j] = [c, LC]
	latsort = latmat[latmat[:,1].argsort()]
	connections.append(latsort)

# Request description
Rmat = np.empty([R,3], dtype='int16')
for i in range(R):
	Rv, Re, Rn = [int(i) for i in input_file[parser].split()]
	parser += 1
	assert Rv >= 0 and Rv < V
	assert Re >= 0 and Re < E
	assert Rn >= 0 and Rn <= 10000
	Rmat[i] = [Rv, Re, Rn]

Rsort = Rmat[Rmat[:,2].argsort()]

output = [list([]) for i in range(C)]

"""
#print(Rmat[0])
# Video 0 for endpoint 85, 1614 times
req = 0
#print(connections[85]) 
# Fastest connection to node 44
cac = 44"""

for i in reversed(range(R)):
#for i in reversed(range(R-10, R)):
	req = Rsort[i,0]
	e = Rsort[i,1]
	c = connections[e]
	for j in range(K[e]):
#	for j in range(10):
		cac = c[j,0]
		# requested video req
		# cache index cac
		if req not in output[cac]:
			if S[req] <= X[cac]:
				output[cac].append(req)
				X[cac] -= S[req]
				break

res = ""
nb_cache_used = 0
for i in range(C):
	if output[i]:
		res += str(i)+" "+" ".join([str(j) for j in output[i]])+"\n"
		nb_cache_used += 1
print(nb_cache_used)
print(res[:-1])
