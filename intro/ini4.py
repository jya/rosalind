infile = open('/home/jason/Downloads/rosalind_ini4.txt')
for line in infile:
	temp = line.split(' ')
	a = int(temp[0])
	b = int(temp[1])
result = 0
for x in range(a,b+1):
	if(x%2 == 1):
		result += x
print result
