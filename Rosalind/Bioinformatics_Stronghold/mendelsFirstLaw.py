#!/usr/bin/env python3

"""
Input: three positive integers k, m and n, representing a population 
containing k+m+n organisms: k individuals are homozygous dominant 
for a factor, m are heterozygous, and n are homozygous recessive

Output: the probability that two randomly selected mating organisms will 
produce an individual possessing a dominant allele (and thus displaying 
the dominant phenotype)

Usage (via command line): python <filename.py>
"""

def mendelsFirstLaw(k, m, n):
	"""
	This returns the probability that given all the possible matings, the
	offspring will have at least one dominant allele.
	"""

	total = k + m + n

	"""
	Probability that the heterozygote-heterozygote, recessive-recessive
	and heterozygote-recessive matings will yield an individual homozygous
	recessive for the factor
	"""
	het_het = 1/4 * (m/total * (m-1)/(total-1))
	rec_rec = n/total * (n-1)/(total-1)
	het_rec = 1/2 * (m/total * n/(total-1) + n/total * m/(total-1))

	return 1 - (het_het + rec_rec + het_rec)


k = int(input("Number of homozygous dominant individuals: "))
m = int(input("Number of heterozygous individuals: "))
n = int(input("Number of homozygous recessive individuals: "))

print(mendelsFirstLaw(k, m, n))