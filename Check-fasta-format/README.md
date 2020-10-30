# Check-fasta-format
Checks an input fasta file to make sure its in the correct format, if not it reformats the file to the correct format

## Dependecies 
**Python 3** \
Python packages 
- biopython

## Usage 
` python Check_fasta_format.py --help` \
usage: Check_fasta_format.py [-h] [-c CONTIGS] [-o OUTPUT] 

optional arguments: \
  -h, --help  show this help message and exit \
  -c CONTIGS  Contigs fasta file \
  -o OUTPUT   Output text file 

## Example command 
`python Check_fasta_format.py -c input.fasta -o input-new.fasta` 
 
 Replace input.fasta with the a fasta file that needs to be reformatted.
