import math

inf = open('/home/jason/Downloads/rosalind_lia.txt')
input = map(int,inf.readline().strip().split())
k = input[0]
n = input[1]
count = math.pow(2,k)
result = math.pow(0.75,count)
for i in range(1,n,1):
	print '!' + str(i)
	num = float(math.factorial(count))
	den = float(math.factorial(i)*math.factorial(count-i))
	coeff = num/den
	print num
	print den
	print coeff
	result += coeff*math.pow(0.25,i)*math.pow(0.75,count-i)
print 1-result
