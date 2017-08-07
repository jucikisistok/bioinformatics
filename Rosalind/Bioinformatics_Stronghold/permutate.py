#!/usr/bin/env python3

"""
Input: a positive integer n given via command line prompt

Output: a txt file containing the number of permutations of length n, followed by 
a list of all such permutations

Usage (via command line): python <filename.py>
"""

from itertools import permutations

def permutate(m):
	"""
	This returns the number of permutations of length n and all such permutations.
	"""

	possible_permutations = list(permutations(range(1, m + 1)))
	f.write("Number of possible permutations: %s\n" % str(len(possible_permutations)))

	for i in possible_permutations:
		perm = "".join(str(i)).replace(",", "")
		f.write("%s\n" % perm)

m = int(input("Choose an integer:"))
with open("result.txt", "w") as f:
	print(permutate(m), file = f)
	f.close()