from Bio import SeqIO
inf = open('/home/jason/Downloads/rosalind_phre.txt')
threshold = int(inf.readline().strip())
handle = SeqIO.parse('/home/jason/Downloads/rosalind_phre.txt', 'fastq')
count = 0
for x in handle:
	sum = 0.0
	for y in x.letter_annotations['phred_quality']:
		sum += y
	average = sum / len(x.letter_annotations['phred_quality'])
	if average < threshold:
		count += 1
print count
