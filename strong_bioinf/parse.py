def parse(f):
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

if __name__ == "__main__":
	convert(sys.argv[1])
