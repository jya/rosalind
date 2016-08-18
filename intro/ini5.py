infile = open('/home/jason/Downloads/rosalind_ini5.txt')
outfile = open('/home/jason/Downloads/result.txt', 'w')
lines = infile.readlines()
for x in range(len(lines)):
	if(x%2 == 1):
		outfile.write(lines[x])
