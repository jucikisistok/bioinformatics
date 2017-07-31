"""
Input: txt file containing two DNA strings of equal length

Output: txt file containing the Hamming-distance between the two strings

Usage (via command line): python <filename.py> <input_data.txt>
"""

import sys

def hammingDistance(string1, string2):
	"""
	This computes the Hamming-distance between two strings of equal length.

	The Hamming-distance is the number of corresponding symbols that differ
	in string1 and string2.
	"""

	if len(string1) != len(string2):
		raise ValueError("Error! The two strings should be of equal length.")
	return sum([1 for i, j in zip(string1, string2) if i != j])

dataset = open(sys.argv[1])
string1, string2 = dataset.readline(), dataset.readline()
with open("result_" + sys.argv[1], "w") as f:
	print("The Hamming-distance is:", hammingDistance(string1, string2), file = f)
	f.close()
dataset.close()

