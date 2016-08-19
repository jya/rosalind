import numpy, sys

inf = open('/home/jason/Downloads/rosalind_cons.txt')
tempstring = ""
dna_length = 1000
profile = numpy.zeros((4, dna_length))
line = inf.readline().strip()
prof_a = []
prof_c = []
prof_g = []
prof_t = []

def count_bases(string):
	for x in range(len(string)):
		if tempstring[x] == 'A':
			profile[0][x] += 1
		if tempstring[x] == 'C':
			profile[1][x] += 1
		if tempstring[x] == 'G':
			profile[2][x] += 1
		if tempstring[x] == 'T':
			profile[3][x] += 1

while line:
        if line[0:1] != '>':
		tempstring += line
        else:
                count_bases(tempstring)
		tempstring = ""
        line = inf.readline().strip()
count_bases(tempstring)
for x in range(len(tempstring)):
	prof_a.append(int(profile[:,x][0]))
	prof_c.append(int(profile[:,x][1]))
	prof_g.append(int(profile[:,x][2]))
	prof_t.append(int(profile[:,x][3]))
cons = ""
for pos in range(len(prof_a)):
	res = 'A'
	maxval = prof_a[pos]
	if prof_c[pos] > maxval:
		res = 'C'
		maxval = prof_c[pos]
	if prof_g[pos] > maxval:
		res = 'G'
		maxval = prof_g[pos]
	if prof_t[pos] > maxval:
		res = 'T'
		maxval = prof_t[pos]
	cons += res
print cons
print 'A:',
for x in prof_a:
	print x,
print
print 'C:',
for x in prof_c:
	print x,
print
print 'G:',
for x in prof_g:
	print x,
print
print 'T:',
for x in prof_t:
	print x,
print
