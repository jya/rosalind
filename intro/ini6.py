infile = open('/home/jason/Downloads/rosalind_ini6.txt')
res = open('/home/jason/Downloads/result.txt', 'w')
temp = infile.readline().strip()
words = temp.split(' ')
results = {}
for word in words:
	if word in results:
		results[word] += 1
	else:
		results[word] = 1
for key in results:
	res.write(key + ' ' + str(results[key]) + '\n')
