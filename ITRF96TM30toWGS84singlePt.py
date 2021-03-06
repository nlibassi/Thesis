from osgeo import ogr
from osgeo import osr

wkt4326 = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]'

wkt7539 = 'PROJCS["ITRF96 / TM30",GEOGCS["GCS_ITRF_1996",DATUM["D_ITRF_1996",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["degree",0.017453292519943295],AXIS["Longitude",EAST],AXIS["Latitude",NORTH]],PROJECTION["Transverse_Mercator"],PARAMETER["central_meridian",30.0],PARAMETER["latitude_of_origin",0.0],PARAMETER["scale_factor",1.0],PARAMETER["false_easting",500000.0],PARAMETER["false_northing",0.0],UNIT["m",1.0],AXIS["x",EAST],AXIS["y",NORTH]]'

srcProj = osr.SpatialReference()
srcProj.ImportFromWkt(wkt7539)

dstProj = osr.SpatialReference()
dstProj.ImportFromWkt(wkt4326)

transform = osr.CoordinateTransformation(srcProj, dstProj)

point = ogr.CreateGeometryFromWkt("POINT (417553.2 4568673.3)") #easting northing

point.Transform(transform)

print point.ExportToWkt()
