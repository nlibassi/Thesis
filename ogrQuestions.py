

'''
#trying to get whole feature to avoid above repetition - fix later
layer.SetAttributeFilter("Filename = 'pr0000106'")
for i in range(0, layer.GetFeatureCount()):
	feature = layer.GetFeature(i) #printing this prints object name
	print feature.attributes() #not working (not in docs)
	break

for feature in layer.getFeatures(): #also not working with SWIG objects, works in QGIS on QGIS VectorLayer
	print feature.attributes()
	break
'''


from osgeo import ogr

source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/ProfilePoints/2001_2015_ProfilePts.shp', update=True)
layer = source.GetLayer()

for feature in layer:
	print feature.GetField('Elevation_')
	break
'''
for feature in layer.getFeatures(): #works in QGIS but not outside (objects are a bit different) but not sure of the exact problem yet
	print feature
	break
'''



#################


for feature in layer: 
	distList.append(feature.GetField('DistanceTo'))
	elevOrig = feature.GetField('Elevation_')
	elevNew = feature.GetField('Depth2015')
	elevOrigList.append(elevOrig)
	if elevOrig <= -11:
		feature.SetField('Diff11m15', elevOrig-elevNew) #finished without error but SetField ignored, nothing written

