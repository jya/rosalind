infile = open('input.txt', 'r')
outfile = open('out.txt', 'w')
strings = {}
key = ""
tempstring = ""
for line in infile:
    if line[0:1] == ">":
        strings[key] = tempstring
        tempstring = ""
        key = line[1:].strip()
    else:
        tempstring += line.strip()
strings[key] = tempstring
del strings[""]
for key in strings:
    gc = 0
    temp = strings[key]
    for x in range(0, len(temp)):
        if temp[x] == "G" or temp[x] == "C":
            gc += 1
    strings[key] = gc/float(len(temp))*100
resultstring = ""
gcvalue = 0
for key in strings:
    if strings[key] > gcvalue:
        resultstring = key
        gcvalue = strings[key]
outfile.write(resultstring + '\n')
outfile.write(str(gcvalue) + '\n')
outfile.close()
