infile = open('/home/jason/Downloads/rosalind_ini3.txt')
lines = []
for line in infile:
	lines.append(line)
text = lines[0]
nums = lines[1].split()
print nums
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
d = int(nums[3])
print text[a:b+1] + ' ' + text[c:d+1]
