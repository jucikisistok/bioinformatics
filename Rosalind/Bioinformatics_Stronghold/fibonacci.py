#!/usr/bin/env python3

"""
Input: positive integers corresponding to the number of months and 
the number of rabbit pairs (given via command line prompt)

Output: the total number of rabbit pairs that will be present after n months,
if we begin with 1 pair and in each generation, every pair of reproduction-age 
rabbits produces a litter of k rabbit pairs

Usage (via command line): python <filename.py>
"""

def fibonacci(n, k):
	"""
	This calculates the total number of rabbit pairs at the end of the
	nth month.
	"""

	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fibonacci(n-1, k) + k*(fibonacci(n-2, k))

n = int(input("Number of months: "))
k = int(input("Rabbit pairs produced by reproduction-age rabbits: "))

print("The total number of rabbit pairs after ", n, " months is", 
	fibonacci(n, k), "( number of pairs:", k, ").")
