#!/usr/bin/env python3

import os 
import sys
import argparse
from Bio import SeqIO
from collections import defaultdict
from operator import add
import csv 

def mag_counts(mags_directory, raw_coverage, contig_lengths, read_length, output):

	#starting with the mags directory, saving the mag name as key and the corresponding contigs as values
	filelist=input_dir(mags_directory)
	mags_dict=defaultdict(list)
	for file in filelist:
		openfi=open(file, 'r')
		for record in SeqIO.parse(openfi, "fasta"):
			mags_dict[file].append(record.id)

	#saving the contig converage table to a dictionary
	contig_cov_dict=defaultdict(list)
	contig_coverage_table=open(raw_coverage)
	count=0
	sample_names=[]
	for f in contig_coverage_table:
		f=f.replace('\n', '')
		lines=f.split('\t')
		samples=len(lines)
		if (count==0):
			samples_names=lines
			count=count+1
		else:
			contig_cov_dict[lines[0]].append(lines[1])
			for i in range(2, samples):
				 contig_cov_dict[lines[0]].append(lines[i])

	#saving the contig lengths to the above dictionary 
	contig_len=open(contig_lengths)
	for f in contig_len:
		f=f.replace('\n', '')
		lines=f.split('\t')
		contig_cov_dict[lines[0]].append(lines[1])

	#sum of all contig counts that belong to each bin, per sample
	new_counts_dict=defaultdict(list)
	raw_counts=[]
	for k,v in mags_dict.items():
		sum_counts=[]
		for val in v:
			raw_counts=contig_cov_dict[val]
			if (len(sum_counts)==0):
				sum_counts=raw_counts
			else:
				sum_counts=[int(sum_counts[x])+ int(raw_counts[x]) for x in range(len(raw_counts))]
		new_counts_dict[k]=sum_counts
		
	#calculating the proprtion of reads
	rl=int(read_length)
	prop_counts_dict=defaultdict(list)
	for k,v in new_counts_dict.items():
		prop_counts=[]
		values=v
		for val in range(samples-1):
			prop=(int(val)*rl)/int(values[-1])
			prop_counts.append(prop)
		prop_counts_dict[k]=prop_counts

	#writing out the proportional counts to a dictionary
	writer=csv.writer(open(output, 'w'))
	writer.writerow(samples_names)
	for key,value in prop_counts_dict.items():
		writer.writerow([key, value])
		print(len(value))

def input_dir(dir):
	files=os.listdir(dir)
	path=[]
	for f in files:
		fipath=os.path.join(dir,f)
		path.append(fipath)
		report=open(fipath, 'r')
	return (path)

if __name__=='__main__' :
	parser=argparse.ArgumentParser(description="Getting the average coverage of each MAG assembled per sample from an already constructed contig coverage table")
	parser.add_argument('-d', dest='directory', help='Enter the directory with all the assembled MAGs')
	parser.add_argument('-c', dest='contig_coverage', help='Enter the file with the number of reads aligned against each contig per sample, in tsv format')
	parser.add_argument('-cl', dest='contig_length', help='Enter the tsv file with each contig name and its length')
	parser.add_argument('-rl', dest='read_length', help='Enter the average read length')
	parser.add_argument('-o', dest='output', help='Enter the output name')
	results=parser.parse_args()
	mag_counts(results.directory, results.contig_coverage, results.contig_length, results.read_length, results.output)
