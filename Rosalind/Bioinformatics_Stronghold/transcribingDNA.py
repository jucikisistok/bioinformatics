"""
Input: txt file containing a DNA string t corresponding to a coding strand

Output: txt file containing the transcribed RNA string u

Usage (via command line): python <filename.py> <input_dataset.txt>
"""

import sys

def transcribingDNA(t):
	"""
	This creates the transcribed RNA string u formed by replacing
	all occurrences of T in t with U in u
	"""

	u = t.replace("T", "U")
	return u

dataset = open(sys.argv[1], "r")
t = dataset.read()
with open("result_"+sys.argv[1], "w") as f:
	print(transcribingDNA(t), file = f)
	f.close()
dataset.close()