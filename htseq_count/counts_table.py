#!/usr/bin/env python

import sys 
import os
import argparse
import numpy as np
import pandas as pd
from collections import defaultdict
from itertools import chain

'''
Takes the htseq counts file from each of the sample counts and writes it out to one table 
Adds the gene name as well from the gff 
'''

#concatenating the kraken reports from multiple file using a dictionary
def consolidate(dir, gff, type, out):
	filelist=input_dir(dir)
	h=defaultdict(list)
	g=gffparser(gff, type)
	for file in filelist:
		openfi=open(file, 'r')
		for line in openfi:
			tmp=line.strip('\n')
			fields=tmp.split('\t')
			h[fields[0]].append(fields[1])

	f=defaultdict(list)
	for k,v in chain(g.items(), h.items()):
		#print (f[k], v)
		f[k].append(v)

	print ("Writing output to a file")
	with open (out, 'w') as fout:
		fout.write('gene-id\tgene-name\t%s\n' %filelist)
		for key,value in f.items():
			#print (key, value)
			fout.write('%s\t%s\n' %(key, value))

#writing the gene name along with the gene id to the dictionary keys
def gffparser(gff, type):
	#opening the gff file 
	gff_fi=open(gff,'r')
	g=defaultdict(list)
	for line in gff_fi:
		field=line.split('\t')
		if (len(field)>2) and (field[2]==type):
			split_fields=field[8].split(';')
			id=split_fields[0].strip("ID=")
			name=split_fields[1].strip("Name=")
			#print (id, name)
			g[id].append(name)
	return(g)

#function that open the directory and confirms there are files, and checks to see that the files are summary files 
def input_dir(dir):
	files=os.listdir(dir)
	assert (len(files)!=0), "The directory is empty"
	path=[]
	for f in files:
		fipath=os.path.join(dir,f)
		path.append(fipath)
		report=open(fipath, 'r')
	#print (path)
	return (path)

if __name__=='__main__' :
	parser=argparse.ArgumentParser(description="Take multiple output files and consolidate to one file")
	parser.add_argument ('-d', dest='directory', help='Enter a directory with htseq count files')
	parser.add_argument ('-g', dest='gff', help='Enter the refernece gff file')
	parser.add_argument ('-t', dest='type', help= 'Enter the type of feature to get the inforamtion from, for example: gene, cds')
	parser.add_argument ('-o', dest='output', help='Enter the output file name')
	results=parser.parse_args()
	consolidate(results.directory, results.gff, results.type, results.output)

