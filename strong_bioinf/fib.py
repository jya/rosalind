infile = open('/home/jason/Downloads/rosalind_fib.txt')
line = infile.readline().strip().split(" ")
n = int(line[0])
k = int(line[1])
result = 1
numrep = 0
prevres = 1
def rabbits(n, k, r):
	if n == 1:
		print result
		return
	else:
		global result
		prevres = result
		result = result + r*k
		print result
		rabbits(n-1,k,prevres)

def main():
	rabbits(n,k,numrep)

main()
