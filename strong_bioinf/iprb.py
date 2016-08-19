inf = open('/home/jason/Downloads/rosalind_iprb.txt')
counts = inf.readline().strip().split(" ")
k = float(counts[0])
m = float(counts[1])
n = float(counts[2])
total = k + m + n
p1 = k/total
p2 = (m/total)*(k/(total-1))+0.75*(m/total)*((m-1)/(total-1))+0.5*(m/total)*(n/(total-1))
p3 = (n/total)*(k/(total-1))+0.5*(n/total)*(m/(total-1))
print p1, p2, p3
res = p1+p2+p3
print res
