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

################################### Objects ###################################

################################## Functions ##################################

##################################### Main ####################################
arguments = docopt(__doc__)

input_file = open(arguments["<file>"], "r").read().splitlines()
V, E, R, C, X = [int(i) for i in input_file[0].split()]
