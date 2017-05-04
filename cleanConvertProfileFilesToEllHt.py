infile = '/home/nlibassi/Geodesy/Thesis/Project/ProfileData/pr0000106.txt' 
outfile = '/home/nlibassi/Geodesy/Thesis/Project/ProfileData/pr0000106_ellHt.csv' 
with open(infile, 'r') as f, open(outfile, 'a') as out:
	for line in f:
		nline = line.split()
		if nline:
			out.write(nline[0].strip() + ', ')
			h = float(nline[1].strip()) + 36.6975
			out.write(str(h) + '\n')

	
