from collections import Counter
import sys

def countNucleotides(s):
	"""
	This counts the number of times that the nucleotides occur in the DNA string.

	Input: txt file containing a DNA string

	Output: txt file containing a list of the nucleotide counts in the A, C, G, T order

	Usage: python <filename.py> <input_dataset.txt>
	"""
	
	c = Counter(s)

	return [c["A"], c["C"], c["G"], c["T"]]

dataset = open(sys.argv[1], "r")
s = dataset.read()
with open("result_"+sys.argv[1], "w") as f:
	print(countNucleotides(s), file = f)
	f.close()
dataset.close()