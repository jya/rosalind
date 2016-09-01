def parsefile(f):
	line = f.readline().strip()
	id = ""
	seq = ""
	list = {}
	id = line[1:len(line)]
	line = f.readline().strip()
	while line:
		if line[0:1] == '>':
			list[id] = seq
			seq = ""
			id = line[1:len(line)]
		else:
			seq += line
		line = f.readline().strip()
	list[id] = seq
	return list

def parsesingle(string):
	seq = string[string.find('\n')+1:len(string)]
	return seq.replace('\n',"")

if __name__ == "__main__":
	convert(sys.argv[1])
