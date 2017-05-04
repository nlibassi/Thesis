import glob, os, sys, argparse

def renameShapefile(path, oldName, newName): 

	"""changes name of shapefile or similar multi-file object

		absolute path

		old and new names given without extensions
	"""

	for fname in glob.glob(path + '//' + oldName + '.*'):
		ext = fname.rsplit('.')[-1]
		os.rename(fname, path + '//' + newName + '.' + ext)

def main():
	parser = argparse.ArgumentParser(description='renames shapefile')
	parser.add_argument('-p', '--PATH', help='absolute path to shapefile')
	parser.add_argument('-o', '--OLDNAME', help='previous file basename (no extension)')
	parser.add_argument('-n', '--NEWNAME', help='new file basename (no extension)')
	args = vars(parser.parse_args())
	print args['PATH']
	#renameShapefile("'" + args['PATH'] + "'", "'" + args['OLDNAME'] + "'", "'" + args['NEWNAME'] + "'")
	renameShapefile(args['PATH'], args['OLDNAME'], args['NEWNAME'])
"""
	renameShapefile("'" + sys.argv[1] + "'", "'" + sys.argv[2] + "'", "'" + sys.argv[3] + "'")

	print sys.argv[1], sys.argv[2], sys.argv[3]
"""

if __name__ == '__main__':
	main()
