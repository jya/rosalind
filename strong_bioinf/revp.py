from parse import *

def reversecomp(seq):
	comp = ""
	for x in seq:
        	if x == 'A':
                	comp += 'T'
        	if x == 'T':
                	comp += 'A'
        	if x == 'G':
                	comp += 'C'
        	if x == 'C':
                	comp += 'G'
	comp = comp[::-1]
	return comp

inf = open('/home/jason/Downloads/rosalind_revp.txt')
seqs = parsefile(inf)
seq = seqs.values()[0]
pals = []
for x in range(0,len(seq),1):
	for i in range(2,7,1):
		if seq[x:x+i] == reversecomp(seq[x+i:x+2*i]):
			print seq[x:x+i]
			print reversecomp(seq[x+i:x+2*i])
			print (x+1,2*i)
			pals.append((x+1,2*i))
for x in pals:
	print str(x[0]) + ' ' + str(x[1])
