import itertools

inf = open('/home/jason/Downloads/rosalind_lexf.txt')
alphabet = inf.readline().strip().split()
alphabet = sorted(alphabet)
print alphabet
length = int(inf.readline())
tups = []
strings = []

a = alphabet
l = []
for x in range(0,length,1):
	l.append(a)

tups.append([x for x in itertools.product(*l)])
for x in tups[0]:
	tempstring = ""
	for y in range(len(x)):
		tempstring += x[y]
	strings.append(tempstring)
for x in strings:
	print x
