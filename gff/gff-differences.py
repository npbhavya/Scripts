#!/usr/bin/env python

import sys
import pandas as pd
from collections import defaultdict
import csv

v1=open("LD-03.fasta_v1.11_output.gff", "rb")
v2=open("LD-03.fasta_v1.14_output.gff", "rb")

gff_v1=pd.read_csv(v1, sep="\t")
gff_list_v1=gff_v1.values.tolist()
gff_v2=pd.read_csv(v2, sep="\t")
gff_list_v2=gff_v2.values.tolist()

#generating a new key
key=[]
for x in gff_list_v1:
	key_x='%s:%s:%s' %(x[0],str(x[3]),str(x[4]))
	x.append(key_x)
	key.append(key_x)
#print (len(key))

for x in gff_list_v2:
	key_x='%s:%s:%s' %(x[0],str(x[3]),str(x[4]))
	x.append(key_x)
	key.append(key_x)
#print (len(key))


keys=set(key)
#print (len(keys))

#generating a dictionary
new_gff=defaultdict(list)

#adding all the uniue keys to the dictionary
for k in keys:
	new_gff[k]=[]

#print (len(new_gff))

#adding values to the keys
#count=0
for f in keys: 
	for x in gff_list_v1:
		if (f==x[9]):
			#print (f,x[9])
			new_gff[f].append(x[8])
			#count=count+1
#print (len(new_gff))
#print (count)

for key, value in new_gff.items():
	if (len(value)==0):
		new_gff[key].append("NA")
#print(new_gff)

for f in keys:
	for y in gff_list_v2:
		if (f==y[9]):
			new_gff[f].append(y[8])

for key, value in new_gff.items():
	if (len(value)==1):
		new_gff[key].append("NA")

for key, value in new_gff.items():
	if (len(value)==2):
		new_gff[key].append("NA")

tst=pd.DataFrame(list(new_gff.items()))
tst.fillna(0)

f=open("output-gff-new", 'w')
tst.to_csv(f, index=False, sep="\t", header=False)
