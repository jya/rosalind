inf = open('/home/jason/Downloads/rosalind_gc.txt')
line = inf.readline().strip()
longest_id = None
gc = 0.0
tempstring = "A"
id = ""

def calc_gc(seq):
	count = float(0)
	seqlen = float(len(seq))
	for x in seq:
		if x == 'G' or x == 'C':
			count += 1
	return count/len(seq)*100

while line:
	print tempstring
	if line[0:1] == '>':
		print calc_gc(tempstring)
		if calc_gc(tempstring) > gc:
			longest_id = id
			gc = calc_gc(tempstring)
		id = line[1:len(line)]
		print '\n' + id
		tempstring = ""
	else:
		tempstring += line
	line = inf.readline().strip()
if calc_gc(tempstring) > gc:
	longest_id = id
	gc = calc_gc(tempstring)

print longest_id
print gc
