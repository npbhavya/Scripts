# Quast_output_manipulation
Take multiple quast reports and add them to one tsv table

## Pre-requisites 
Run QUAST command and generate a report \
`quast.py <contigs> -o <output folder>`

## Dependecies 
**Python 3** \
Python packages 
- numpy 
- scipy
- argparse
- pandas 
- collection 

## Usage 
`python quast_table.py --help`
usage: quast_table.py [-h] [-d DIRECTORY] [-o OUTPUT]

Take multiple quast output files and consolidate them to one output

optional arguments:
  -h, --help    show this help message and exit \
  -d DIRECTORY  Enter the quast output directories \
  -o OUTPUT     Enter the output file name \

## Example command 
`python quast_table.py -d quast_out -o quast_output.tsv`

## Input files
This code takes the quast output (report.tsv) from quast output directories. To setup the input files, 
1) Run QUAST first for all the assemblies, \
`quast.py sampplename_contigs -o samplename_quast_assembly`

2) write all the report.tsv files to the new directory, but make sure to rename the report.tsv to sample-name.tsv, here are the commands to do this, \
`mv samplename_quast_assembly/report.tsv sample_name_quast.tsv`

3) Confirm that the new directory quast-out has the right number of files and is named correctly before running the quast,py script

