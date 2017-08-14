#!/usr/bin/env python3

"""
Input: a txt or FASTA file containing the two DNA strings of equal length,
given in FASTA format

Output: a txt or FASTA file containing the transition/transversion ratio

Usage (via command line): python <filename.py> <input_file.txt or input_file.fasta>
"""

import sys
from Bio import SeqIO

def transitionTransversionRatio(s):
	"""
	This calculates the transition/transversion ratio.
	"""

	dna1, dna2 = s[0], s[1]

	if len(dna1) != len(dna2):
		raise ValueError("Error! The two strings should be of equal length.")

	trs = ["AG", "GA", "CT", "TC"]
	trv = ["AC", "CA", "AT", "TA", "CG", "GC", "GT", "TG"]

	mismatches = [i+j for i, j in zip(dna1, dna2) if i != j]
	transitions = [1 for m in mismatches if m in trs]
	transversions = [1 for m in mismatches if m in trv]
	
	return sum(transitions) / sum(transversions)

dataset = SeqIO.parse(open(sys.argv[1]), 'fasta')
s = []
for fasta in dataset:
	s.append(str(fasta.seq))

with open("result_" + sys.argv[1], "w") as f:
	print(transitionTransversionRatio(s), file = f)
	f.close()
dataset.close()