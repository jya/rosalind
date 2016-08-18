inf = open('/home/jason/Downloads/rosalind_revc.txt')
text = inf.readline()
rev = ""
for x in range(len(text)-1, -1, -1):
	rev += text[x]
rev = rev.replace('\n', "")
revc = ""
dic = {'A':'T','T':'A','C':'G','G':'C'}
for x in range(len(rev)):
	revc += dic[rev[x]]
print revc
