inf = open('/home/jason/Downloads/rosalind_fibd.txt')
input = inf.readline().strip().split()

def fib(n, m, ages):
	if n > 1:
		new_young = 0
		for y in range(1, m, 1):
			new_young += ages[y]
		for x in range(m, 0, -1):
			ages[x] = ages[x-1]
		ages[0] = new_young
		fib(n-1, m, ages)
	else:
		result = 0
		for x in range(0,m):
			result += ages[x]
		print result

def main():
	ages = [0] * (int(input[1])+1)
	ages[0] = 1
	fib(int(input[0]), int(input[1]), ages)

main()
