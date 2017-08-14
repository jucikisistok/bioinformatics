#!/usr/bin/env python3

"""
Input: txt file containing a protein string P

Output: txt file containing the total weight of P

Usage: python <filename.py> <input_file.txt>
"""

import sys

"""
This dictionary contains the mass of each possible amino acid residue.
The value of the mass used is the monoisotopic mass of each residue.
"""
monoisotopicMass = {
	"A" : 71.03711, "C" : 103.00919,
	"D" : 115.02694, "E" : 129.04259,
	"F" : 147.06841, "G" : 57.02146, 
	"H" : 137.05891, "I" : 113.08406, 
	"K" : 128.09496, "L" : 113.08406, 
	"M" : 131.04049, "N" : 114.04293, 
	"P" : 97.05276, "Q" : 128.05858, 
	"R" : 156.10111, "S" : 87.03203, 
	"T" : 101.04768, "V" : 99.06841, 
	"W" : 186.07931, "Y" : 163.06333,
}

def proteinMass(P):
	"""
	This calculates the total weight of a given protein.
	"""
	masses = []
	for i in range(len(P)):
		masses.append(monoisotopicMass[P[i]])
	return sum(masses)

dataset = open(sys.argv[1])
P = dataset.read().strip()
with open("result_" + sys.argv[1], "w") as f:
	print(proteinMass(P), file = f)
	f.close()
dataset.close()
