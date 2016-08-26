inf = open('/home/jason/Downloads/rosalind_iev.txt')
genotypes = inf.readline().strip().split()
genotypes = map(float, genotypes)
probs = [1.0, 1.0, 1.0, .75, .5, 0.0]
ev = 0
for x in range(len(genotypes)):
	ev += 2*probs[x]*genotypes[x]
print ev
