import sys, re
import urllib2
from parse import *

url = 'http://www.uniprot.org/uniprot/'
url += sys.argv[1] + '.fasta'
response = urllib2.urlopen(url)
fasta = response.read()
seq = parsesingle(fasta)

locs = []
prot = seq
motif = re.compile('N(?!P)[A-Z][ST](?!P)[A-Z]')
for x in range(len(prot)):
	if x+3 < len(prot):
		temp = prot[x:x+4]
		if motif.match(temp):
			locs.append(x+1)
for x in locs:
	print x,
