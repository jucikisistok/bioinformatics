"""
Input: txt file containing a DNA string s

Output: txt file containing the reverse complement of the 
DNA string

Usage (via command line): python <filename.py> <input_dataset.txt>
"""

import sys

def complementDNA(s):
	"""
	This creates the reverse complement of the input string by 
	reversing the symbols of s, then taking the complement of 
	each symbol (A - T, G - C).
	"""

	reverse = s[::-1]
	complement = str.maketrans("GATC", "CTAG")
	return reverse.translate(complement)


dataset = open(sys.argv[1], "r")
s = dataset.read()
with open("result_" + sys.argv[1], "w") as f:
	print(complementDNA(s), file = f)
	f.close()
dataset.close()
