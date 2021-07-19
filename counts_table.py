#!/usr/bin/env python

import sys 
import os
import argparse
import numpy as np
import pandas as pd
from collections import defaultdict
from itertools import chain

#joining files based on common column
def consolidate(dir, match_col, out):
	filelist=input_dir(dir)
	h=defaultdict(list)
	col=int(match_col)
	for file in filelist:
		openfi=open(file, 'r')
		for line in openfi:
			tmp=line.strip('\n')
			fields=tmp.split('\t')
			h[fields[0]].append(fields[col])

	print ("Writing output to a file")
	with open (out, 'w') as fout:
		fout.write('contigs\t %s\n' %filelist)
		for key,value in h.items():
			fout.write('%s\t%s\n' %(key, value))

#function that open the directory and confirms there are files,
def input_dir(dir):
	files=os.listdir(dir)
	assert (len(files)!=0), "The directory is empty"
	path=[]
	for f in files:
		fipath=os.path.join(dir,f)
		path.append(fipath)
		report=open(fipath, 'r')
	return (path)

if __name__=='__main__' :
	parser=argparse.ArgumentParser(description="Take multiple output files and consolidate to one file")
	parser.add_argument ('-d', dest='directory', help='Enter a directory with files to consolidatex')
	parser.add_argument ('-c', dest='column', help= 'Enter the column number')
	parser.add_argument ('-o', dest='output', help='Enter the output file name')
	results=parser.parse_args()
	consolidate(results.directory, results.column, results.output)

