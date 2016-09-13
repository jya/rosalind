from Bio import ExPASy
from Bio import SwissProt
inf = open('/home/jason/Downloads/rosalind_dbpr.txt')
id = inf.readline().strip()
handle = ExPASy.get_sprot_raw(id)
record = SwissProt.read(handle)
crossref = record.cross_references
terms = []
for x in crossref:
	if x[0] == 'GO':
		if x[2][0:2] == 'P:':
			terms.append(x[2][2:])
for x in terms:
	print x
