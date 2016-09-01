inf = open('/home/jason/Downloads/rosalind_mrna.txt')
prot = inf.readline().strip()
possible = {'F':2, 'L':6, 'S':6, 'Y':2, 'C':2, 'W':1, 'P':4, 'H':2, 'Q':2, 'R':6, 'I':3,
	    'M':1, 'T':4, 'N':2, 'K':2, 'V':4, 'A':4, 'D':2, 'E':2, 'G':4}
result = 3
for x in prot:
	result %= 1000000
	result *= possible[x]
print result%1000000
