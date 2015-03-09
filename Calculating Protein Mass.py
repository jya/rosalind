conv = open('conv.txt', 'r')
infile = open('input.txt', 'r')
outfile = open('out.txt', 'w')
in_data = []
dic = {}
result = 0
for line in conv:
    raw = str(line)
    in_data += raw.split()
for x in range(0,len(in_data),2):
    dic[in_data[x]] = in_data[x+1]
string = str(infile.readline().strip())
for x in string:
    result += float(dic[x])
print result
