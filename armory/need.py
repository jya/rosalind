from Bio import Entrez
from Bio import SeqIO
inf = open('/home/jason/Downloads/rosalind_need.txt')
seqs = inf.readline().strip().split()
Entrez.email = 'jya@stanford.edu'
handle = Entrez.efetch(db='nuccore', id=seqs, rettype='fasta')
records = list(SeqIO.parse(handle, 'fasta'))
for x in range(len(records)):
	print records[x].format('fasta')
