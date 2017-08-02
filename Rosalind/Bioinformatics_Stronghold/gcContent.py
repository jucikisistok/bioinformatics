"""
Input: txt file containing DNA strings in FASTA format

Output: txt file containing the ID of the string having the highest GC-content, 
followed by the GC-content of that string

Usage (via command line): python <filename.py> <input_file.txt>
"""

import sys
from Bio import SeqIO

def gcContent(data):
	"""
	This calculates the GC-content of the strings and returns the one with 
	the highest GC-content.
	"""

	GC_cont = {}
	for fasta in data:
		GC = ((str(fasta.seq).count("C") + str(fasta.seq).count("G"))/len(fasta.seq))*100
		GC_cont.update({fasta.id : GC})
	return ([(key, value) for key,value in GC_cont.items() if value == max(GC_cont.values())])


data = SeqIO.parse(open(sys.argv[1]), "fasta")
with open("result_" + sys.argv[1], "w") as f:
	print("The string with the highest GC content is:", gcContent(data), file = f)
	f.close()
data.close()
