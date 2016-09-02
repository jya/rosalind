from parse import *
from prot import *

inf = open('/home/jason/Downloads/rosalind_splc.txt')
seqs = parsefile(inf)
longest = ""
longestseq = ""
for x in seqs.keys():
	if len(seqs[x]) > len(longestseq):
		longest = x
		longestseq = seqs[x]
for x in seqs.keys():
	if x != longest:
		substr = seqs[x]
		for i in range(len(longestseq)):
			if longestseq[i:i+len(substr)] == substr:
				longestseq = longestseq[0:i] + longestseq[i+len(substr):len(longestseq)]
print convertdna(longestseq)
