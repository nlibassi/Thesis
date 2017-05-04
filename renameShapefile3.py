#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob, os, sys, argparse

def renameShapefile(path, oldName, newName): 

	"""changes name of shapefile or similar multi-file object

		absolute path

		old and new names given without extensions
	"""

	for fname in glob.glob(path + '//' + oldName + '.*'):
		ext = fname.rsplit('.')[-1]
		os.rename(fname, path + '//' + newName + '.' + ext)

renameShapefile('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/', ' Benchmarks2001_02_ITRF96TM30_corrected1', '2001_2002_Benchmarks_ITRF96TM30')




#for use from command line but easier to change function call above
"""
parser = argparse.ArgumentParser(description='renames shapefile')
parser.add_argument('PATH')
parser.add_argument('OLDNAME')
parser.add_argument('NEWNAME')
args = parser.parse_args()
print type(args)
print getattr(args, 'PATH'), getattr(args, 'OLDNAME'), getattr(args, 'NEWNAME')
#renameShapefile("'" + args['PATH'] + "'", "'" + args['OLDNAME'] + "'", "'" + args['NEWNAME'] + "'")
renameShapefile(getattr(args, 'PATH'), getattr(args, 'OLDNAME'), getattr(args, 'NEWNAME'))
"""

