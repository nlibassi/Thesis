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


parser = argparse.ArgumentParser(description='renames shapefile')
parser.add_argument('-p', '--PATH', help='absolute path to shapefile')
parser.add_argument('-o', '--OLDNAME', help='previous file basename (no extension)')
parser.add_argument('-n', '--NEWNAME', help='new file basename (no extension)')
args = parser.parse_args()
#realpath = os.path.realpath(args.SHAPEFILENAME)
#print args.P
print getattr(args, 'PATH'), getattr(args, 'OLDNAME'), getattr(args, 'NEWNAME')
#renameShapefile("'" + args['PATH'] + "'", "'" + args['OLDNAME'] + "'", "'" + args['NEWNAME'] + "'")
renameShapefile(getattr(args, 'PATH'), getattr(args, 'OLDNAME'), getattr(args, 'NEWNAME'))


