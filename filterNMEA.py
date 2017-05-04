infile = '/home/nlibassi/Geodesy/Thesis/Project/20160929/20160929_KBS_GNSS.log'
outfile = '/home/nlibassi/Geodesy/Thesis/Project/20160929/20160929_KBS_GNSS_GPGGA.txt'

with open(infile, 'r') as f, open(outfile, 'a') as out:
	for line in f:
		if 'GPGGA' in line:
			out.write(line)
