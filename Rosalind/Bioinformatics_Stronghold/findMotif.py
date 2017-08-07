#!/usr/local/bin/python
# coding: utf-8

"""
Input: txt file containing two DNA strings - the string s and its substring t.

Output: txt file containing all locations of t as a substring of s, using 1-based numbering.

Usage (via command line): python <filename.py> <input_file.txt>
"""

import sys

def findMotif(s, t):
	"""
	This finds all locations of the substring t in string s and 
	returns a list containing these locations.
	"""
	
	if len(t) > len(s):
		raise ValueError("Oops - the substring (t) should be shorter than the string (s)!")

	pattern_position = []
	for i in range(len(s)):
		if (s[i:i+len(t)]) == t:
			pattern_position.append(i+1)
	return pattern_position

dataset = open(sys.argv[1])
s, t = dataset.readline().strip(), dataset.readline().strip()

with open("result_" + sys.argv[1], "w") as f:
	print(findMotif(s, t), file = f)
	f.close()
dataset.close()
