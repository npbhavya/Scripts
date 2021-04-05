import sys
import os
import argparse
from Bio import SeqIO
from collections import defaultdict
from collections import OrderedDict
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

'''
Get the reverse completement of the genome or multi fasta file
To run the script,
	python reverse_complement.py -f <fasta file> -o <output fasta file>
'''

def reverse_complement(fastain, fastaout):
	fout=open(fastaout, "w")
	with open(fastain) as handle:
		for record in SeqIO.parse(handle, "fasta"):
			ids=str(record.id)
			seq=record.seq
			new_seq=str(seq.reverse_complement())
			new_rec=SeqRecord(Seq(new_seq), id=ids)
			SeqIO.write(new_rec, fout, "fasta")
	fout.close()

if __name__=='__main__' :
	parser=argparse.ArgumentParser(description="reverse complement code")
	parser.add_argument ('-f', dest='fasta')
	parser.add_argument ('-o', dest='output')
	results=parser.parse_args()
	reverse_complement(results.fasta, results.output)
