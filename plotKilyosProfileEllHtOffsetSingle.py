from osgeo import ogr
import matplotlib.pyplot as plt
import numpy as np


source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/ProfilePoints/2001_2015_ProfilePtsEdited.shp')
layer = source.GetLayer()
layerDefn = layer.GetLayerDefn()

profNames = [u'pr0000106', u'pr4000106', u'pr3000106', u'pr7770106', u'pr7000106', u'pr2000106', u'pr6000106', u'pr1000106', u'pr5000106']

distList = []
elevOrigList = []
elevNewList = []

hOffset = 0.891 #mean of ellipsoidal hts of shoreline pts in 2015 (m)

diff11mList = []

layer.SetAttributeFilter("Filename = 'pr4000106'")
for feature in layer: 
	distList.append(feature.GetField('DistanceTo'))
	elevOrig = feature.GetField('Elevation_')
	elevNew = feature.GetField('Depth2015')
	elevOrigList.append(elevOrig)

	if elevNew is not None:
		elevNewList.append(elevNew - hOffset) 
	else:
		elevNewList.append(None)



#print dist[:50], elev01[:50], elev15[:50]

plt.plot(distList, elevOrigList)
plt.plot(distList, elevNewList)
plt.xlabel('Distance from Benchmark (m)')
plt.ylabel('Depth (m)')
plt.legend(['June 2001', 'Dec 2015'], loc='upper right')
plt.show()
#plt.savefig('/home/nlibassi/Geodesy/Thesis/Project/ProfileData/Plots/TestProfileMethod1.png') 



