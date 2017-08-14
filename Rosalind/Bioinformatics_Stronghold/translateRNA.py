#!/usr/bin/env python3

"""
Input: txt file containing an RNA string s corresponding to a
strand of mRNA

Output: txt file containing the protein string encoded by s

Usage (via command line): python <filename.py> <input_file.txt>
"""

import sys

"""
This dictionary contains the RNA codon table - it dictates
the details regarding the encoding of specific codons into 
the amino acid alphabet.
"""
codonDict = {
	"UUU" : "F", "UUC" : "F", "UUA" : "L", "UUG" : "L",
	"UCU" : "S", "UCC" : "S", "UCA" : "S", "UCG" : "S",
	"UAU" : "Y", "UAC" : "Y", "UAA" : "", "UAG" : "",
	"UGU" : "C", "UGC" : "C", "UGA" : "", "UGG" : "W",
	"CUU" : "L", "CUC" : "L", "CUA" : "L", "CUG" : "L",
	"CCU" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P",
	"CAU" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q",
	"CGU" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R",
	"AUU" : "I", "AUC" : "I", "AUA" : "I", "AUG" : "M",
	"ACU" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T",
	"AAU" : "N", "AAC" : "N", "AAA" : "K", "AAG" : "K",
	"AGU" : "S", "AGC" : "S", "AGA" : "R", "AGG" : "R",
	"GUU" : "V", "GUC" : "V", "GUA" : "V", "GUG" : "V",
	"GCU" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A",
	"GAU" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E",
	"GGU" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G",
}

def translateRNA(s):
	"""
	This translates the RNA string s into a protein.
	"""

	codons = [s[i:i+3] for i in range(len(s))]
	
	protein = []
	for i in range(0, len(codons), 3):
		protein.append(codonDict[codons[i]])
	return "".join(protein)

dataset = open(sys.argv[1])
s = dataset.read().strip()

with open("result_" + sys.argv[1], "w") as f:
	print(translateRNA(s), file = f)
	f.close()
dataset.close()