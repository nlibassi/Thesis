from osgeo import ogr
import matplotlib.pyplot as plt

source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/ProfilePoints/2001_2015_ProfilePtsEdited.shp')
layer = source.GetLayer()

profNames = ['pr0000106', 'pr4000106', 'pr3000106', 'pr7770106', 'pr7000106', 'pr2000106', 'pr6000106', 'pr1000106', 'pr5000106']

#hOffset = 0.891 #mean of ellipsoidal hts of shoreline pts in 2015 (m)

for pname in profNames:
	distList = []
	elevOrigList = []
	elevNewList = []
	diff11mList = []
	layer.SetAttributeFilter("Filename = " + "'" + pname + "'")
	for feature in layer:
		elevOrig = feature.GetField('Elevation_')
		elevNew = feature.GetField('Depth2015')
		if elevOrig <= -11:
			diff11mList.append(elevOrig-elevNew)
	deepOffset = abs(sum(diff11mList)/len(diff11mList)) #abs
	print('Profile ' + pname[2:5] + ': Mean of differences between depths beyond 11m is %.3f' % deepOffset)

	layer.ResetReading()

	for feature in layer: 
		distList.append(feature.GetField('DistanceTo'))
		elevOrig = feature.GetField('Elevation_')
		elevNew = feature.GetField('Depth2015')
		elevOrigList.append(elevOrig)
		if feature.GetField('Depth2015') is not None:
			elevNewList.append(elevNew - deepOffset)
		else:
			elevNewList.append(None)

	plt.figure()
	plt.plot(distList, elevOrigList)
	plt.plot(distList, elevNewList)
	plt.suptitle('Profile ' + pname[2:5], fontsize=14)
	plt.xlabel('Distance from Benchmark (m)')
	plt.ylabel('Depth (m)')
	plt.legend(['June 2001', 'Dec 2015'], loc='upper right')
	#plt.show()
	plt.savefig('/home/nlibassi/Geodesy/Thesis/Project/ProfileData/Plots/Prof' + pname[2:5] + '_2001_2015_DeepOffset.png') 




