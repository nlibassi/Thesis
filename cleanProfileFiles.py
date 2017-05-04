
infile = '/home/nlibassi/Geodesy/Thesis/Project/ProfileData/pr0000106.txt' 
outfile = '/home/nlibassi/Geodesy/Thesis/Project/ProfileData/pr0000106_clean.txt' 
with open(infile, 'r') as f, open(outfile, 'a') as out:
	for line in f:
		nline = line.split()
		if nline:
			out.write(nline[0].strip() + ' ')
			out.write(nline[1].strip() + '\n')


