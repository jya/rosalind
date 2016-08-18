inf = open('/home/jason/Downloads/rosalind_rna.txt')
dna = inf.readline()
rna = ""
for x in range(len(dna)):
	if dna[x] == 'T':
		rna += 'U'
	else: rna += dna[x]
print rna
