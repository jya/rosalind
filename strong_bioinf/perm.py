import itertools

inf = open('/home/jason/Downloads/rosalind_perm.txt')
num = int(inf.readline().strip())
list = []
for i in range(1, num+1):
	list.append(i)
perms = itertools.permutations(list)
count = 0
for x in perms:
	count += 1
	for y in x:
		print y,
	print
print count
