import math
infile = open('/home/jason/Downloads/rosalind_ini2.txt')
result = 0
for line in infile:
	nums = line.split(' ')
	a = int(nums[0])
	b = int(nums[1])
	result = a*a + b*b
print result
