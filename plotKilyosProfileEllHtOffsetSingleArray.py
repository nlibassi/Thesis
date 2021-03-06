from osgeo import ogr
import matplotlib.pyplot as plt
import numpy as np


source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/ProfilePoints/2001_2015_ProfilePtsEdited.shp')
layer = source.GetLayer()
layerDefn = layer.GetLayerDefn()

profNames = [u'pr0000106', u'pr4000106', u'pr3000106', u'pr7770106', u'pr7000106', u'pr2000106', u'pr6000106', u'pr1000106', u'pr5000106']

distArray = np.empty([0])
elevOrigArray = np.empty([0])
elevNewArray = np.empty([0])

hOffset = 0.891 #mean of ellipsoidal hts of shoreline pts in 2015 (m)

layer.SetAttributeFilter("Filename = 'pr4000106'")
for feature in layer: 
	distArray = np.append(distArray, feature.GetField('DistanceTo'))
	elevOrig = feature.GetField('Elevation_')
	elevNew = feature.GetField('Depth2015')
	elevOrigArray = np.append(elevOrigArray, elevOrig)

	if elevNew is not None:
		elevNewArray = np.append(elevNewArray, elevNew - hOffset) 
	else:
		elevNewArray = np.append(elevNewArray, None)

dx = distArray[:-1] - distArray[1:]
z = elevOrigArray - elevNewArray

print sum(abs(dx * z[:-1])) #modify z to get same dimensions

print len(dx)
print len(elevOrigArray)

plt.plot(distArray, elevOrigArray)
plt.plot(distArray, elevNewArray)
plt.xlabel('Distance from Benchmark (m)')
plt.ylabel('Depth (m)')
plt.legend(['June 2001', 'Dec 2015'], loc='upper right')
plt.show()
#plt.savefig('/home/nlibassi/Geodesy/Thesis/Project/ProfileData/Plots/TestProfileMethod1.png') 



