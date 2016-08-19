inf = open('/home/jason/Downloads/rosalind_subs.txt')
str1 = inf.readline().strip()
str2 = inf.readline().strip()
locations = []

for x in range(len(str1)-len(str2)):
	if str1[x:x+len(str2)] == str2:
		locations.append(x+1)

for x in locations:
	print str(x),
