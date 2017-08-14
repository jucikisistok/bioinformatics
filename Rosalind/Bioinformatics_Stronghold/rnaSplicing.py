"""
Input: txt or FASTA file containing a DNA string s and a collection of
substrings of s acting as introns, given in FASTA format

Output: txt or FASTA file containing the protein resulting from
transcribing and translating the exons of s

Usage (via command line): python <filename.py> <input_file.txt or input_file.FASTA>
"""

import sys
from Bio import SeqIO

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

def rnaSplicing(s):
	"""
	This cuts out the introns from the DNA string s.
	"""
	dna = s[0]
	introns = s[1:]
	for i in introns:
		if i in dna:
			dna = dna.replace(i, "")

	"""
	This creates the pre-mRNA by replacing thymine with uracyl.
	"""
	dna = dna.replace("T", "U")
	
	"""
	This translates the exons to protein.
	"""
	codons = [dna[i:i+3] for i in range(len(dna))]
	
	protein = []
	for nucl in range(0, len(codons), 3):
		if len(codons[nucl])%3 == 0:
			protein.append(codonDict[codons[nucl]])
	return "".join(protein)


dataset = SeqIO.parse(open(sys.argv[1]), 'fasta')
s = []
for fasta in dataset:
	s.append(str(fasta.seq))

with open("result_" + sys.argv[1], "w") as f:
	print(rnaSplicing(s), file = f)
	f.close()
dataset.close()
