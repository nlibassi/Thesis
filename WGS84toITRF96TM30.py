'''does not copy attributes, to be added if everything else works'''


import os, os.path, shutil
from osgeo import ogr
from osgeo import osr
from osgeo import gdal


def from4326to7539(inpath, outpath):
	wkt4326 = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]'

	wkt7539 = 'PROJCS["ITRF96 / TM30",GEOGCS["GCS_ITRF_1996",DATUM["D_ITRF_1996",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["degree",0.017453292519943295],AXIS["Longitude",EAST],AXIS["Latitude",NORTH]],PROJECTION["Transverse_Mercator"],PARAMETER["central_meridian",30.0],PARAMETER["latitude_of_origin",0.0],PARAMETER["scale_factor",1.0],PARAMETER["false_easting",500000.0],PARAMETER["false_northing",0.0],UNIT["m",1.0],AXIS["x",EAST],AXIS["y",NORTH]]'

	srcProj = osr.SpatialReference()
	srcProj.ImportFromWkt(wkt4326)

	dstProj = osr.SpatialReference()
	dstProj.ImportFromWkt(wkt7539)

	transform = osr.CoordinateTransformation(srcProj, dstProj)

	#Open the source shapefile

	srcFile = ogr.Open(inpath)
	srcLayer = srcFile.GetLayer(0)

	#Create the dest shapefile and give it the new projection

	dstLoc = outpath.split('.shp')[0]
	dstShp = outpath.rsplit('/')[-1]

	if os.path.exists(dstLoc):
		shutil.rmtree(dstLoc)
	os.mkdir(dstLoc)

	driver = ogr.GetDriverByName("ESRI Shapefile")
	dstPath = os.path.join(dstLoc, dstShp)
	dstFile = driver.CreateDataSource(dstPath)
	dstLayer = dstFile.CreateLayer("layer", dstProj)

	#Reproject each feature

	for i in range(srcLayer.GetFeatureCount()):
		feature = srcLayer.GetFeature(i)
		geometry = feature.GetGeometryRef()
		newGeometry = geometry.Clone()
		newGeometry.Transform(transform)	
		feature = ogr.Feature(dstLayer.GetLayerDefn())
		feature.SetGeometry(newGeometry)
		dstLayer.CreateFeature(feature)
		feature.Destroy()

	srcFile.Destroy()
	dstFile.Destroy()


bathyCorrectedWgs = '/home/nlibassi/Geodesy/Thesis/Project/Vector/WGS84/20160929_BathymetryCorrected.shp'

bathyCorrectedItrf = '/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/20160929_BathymetryCorrected.shp'

from4326to7539(bathyCorrectedWgs, bathyCorrectedItrf)

