from parse import *

inf = open('/home/jason/Downloads/rosalind_lcsm.txt')
seqs = parse(inf)
seqs = seqs.values()

def is_substr(find, data):
	if len(data) < 1 and len(find) < 1:
		return False
	for i in range(len(data)):
		if find not in data[i]:
			return False
	return True

def longest_substr(data):
	longest = ''
	if len(data) > 1 and len(data[0]) > 0:
		for i in range(len(data[0])):
			for j in range(len(data[0])-i+1):
				if j > len(longest) and is_substr(data[0][i:i+j], data):
					longest = data[0][i:i+j]
	return longest

print longest_substr(seqs)
