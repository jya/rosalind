infile = open('/home/jason/Downloads/rosalind_dna.txt')
input = infile.readline()
a=c=g=t=0
for x in range(len(input)):
	if input[x] == 'A': a += 1
	if input[x] == 'C': c += 1
	if input[x] == 'G': g += 1
	if input[x] == 'T': t += 1
print str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t)
