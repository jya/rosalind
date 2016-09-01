from parse import *

inf = open('/home/jason/Downloads/rosalind_orf.txt')
map = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
    "TAT":"Y", "TAC":"Y", "TAA":"STOP", "TAG":"STOP",
    "TGT":"C", "TGC":"C", "TGA":"STOP", "TGG":"W",
    "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
seqs = parsefile(inf)
seq = seqs.values()[0]
results = []
for x in range(len(seq)):
	if x+3 < len(seq):
		if seq[x:x+3] == 'ATG':
			tempstring = 'M'
			for x in range(x+3,len(seq)-3,3):
				if seq[x:x+3] != 'TAA' and seq[x:x+3] != 'TAG' and seq[x:x+3] != 'TGA':
					tempstring += map[seq[x:x+3]]
				else:
					if tempstring not in results:
						results.append(tempstring)
					break
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
seq = comp[::-1]
for x in range(len(seq)):
        if x+3 < len(seq):
                if seq[x:x+3] == 'ATG':
                        tempstring = 'M'
                        for x in range(x+3,len(seq)-3,3):
                                if seq[x:x+3] != 'TAA' and seq[x:x+3] != 'TAG' and seq[x:x+3] != 'TGA':
                                        tempstring += map[seq[x:x+3]]
                                else:
					if tempstring not in results:
	                                       results.append(tempstring)
                                        break
for x in results:
	print x
