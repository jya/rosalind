inf = open('/home/jason/Downloads/rosalind_hamm.txt')
str1 = inf.readline().strip()
str2 = inf.readline().strip()

count = 0
for x in range(len(str1)):
	if str1[x] != str2[x]:
		count += 1

print count
