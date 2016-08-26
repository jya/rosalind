from parse import *

inf = open('/home/jason/Downloads/rosalind_grph.txt')
seqs = parse(inf)

prefixes = {}
suffixes = {}
adj = {}
for x in seqs:
	prefixes[x] = seqs[x][0:3]
	suffixes[x] = seqs[x][len(seqs[x])-3:len(seqs[x])]
for x in suffixes:
	for y in prefixes:
		if x != y:
			if suffixes[x] == prefixes[y]:
				if x not in adj:
					adj[x] = [y]
				else:
					adj[x].append(y)
for x in adj:
	for y in adj[x]:
		print x + ' ' + y
