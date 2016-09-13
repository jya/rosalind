from Bio import Entrez
from Bio import SeqIO
inf = open('/home/jason/Downloads/rosalind_frmt.txt')
ids = inf.readline().strip().split()
Entrez.email = 'jya@stanford.edu'
handle = Entrez.efetch(db='nuccore', id=ids, rettype='fasta')
records = list(SeqIO.parse(handle, 'fasta'))
shortest_id = 0
shortest_len = 99999999999
for x in range(len(records)):
	if len(records[x].seq) < shortest_len:
		shortest_id = x
		shortest_len = len(records[x].seq)
print records[shortest_id].format('fasta')
