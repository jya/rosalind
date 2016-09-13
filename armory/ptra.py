from Bio.Seq import translate
inf = open('/home/jason/Downloads/rosalind_ptra.txt')
seq = inf.readline().strip()
prot = inf.readline().strip()
x = 1
while x < 26:
	if x == 7:
		x += 2
		continue
	if x == 17:
		x += 4
		continue
	if translate(seq, table=x, stop_symbol='') == prot:
		print x
	x += 1

