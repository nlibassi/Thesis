from osgeo import ogr
import matplotlib.pyplot as plt

source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/ProfilePoints/2001_2017_ProfilePtsWEllHts.shp')
layer = source.GetLayer()

profNames = ['pr0000106', 'pr4000106', 'pr3000106', 'pr7700106', 'pr7000106', 'pr2000106', 'pr6000106', 'pr1000106', 'pr5000106']

def sameSign(x, y):
	return (x<0 and y<0) or (x>0 and y>0)

#hOffset = 0.891 #mean of ellipsoidal hts of shoreline pts in 2015 (m)

for pname in profNames:
	distList = []
	elevOrigList = []
	elevNewList = []
	#diff11mList = []
	layer.SetAttributeFilter("Filename = " + "'" + pname + "'")

	for feature in layer: 
		distList.append(feature.GetField('DistanceTo'))
		elevOrig = feature.GetField('EllHt2001')
		elevNew = feature.GetField('EllHt2017')
		elevOrigList.append(elevOrig)
		elevNewList.append(elevNew)

	plt.figure()
	plt.plot(distList, elevOrigList)
	plt.plot(distList, elevNewList)
	if pname == 'pr0000106':

		plt.plot(33.07, 36.71, 'b+')
		plt.plot(29.51, 36.67, 'g+')
		plt.axhline(y=36.71, color='b', linestyle='-')
		plt.axhline(y=36.67, color='g', linestyle='-')
		#will do for each profile but single test here
		hZipped = zip(elevOrigList, elevNewList)
		deltaList = []
		totalList = []
		delta = 0
		total = 0
		for h in hZipped:
			if None not in h:
				delta = h[1] - h[0]
				deltaList.append(delta)
			else:
				deltaList.append(None)
		dZipped = zip(deltaList, deltaList[1:])
		
		for d in dZipped:
			if None not in d and sameSign(d[0], d[1]) \
			and not totalList:
				total = d[0]+d[1]
				totalList.append(total)
			elif None not in d and sameSign(d[0], d[1]) \
			and totalList:
				totalList[-1] += d[1]
			elif None not in d and not sameSign(d[0], d[1]):
				totalList.append(d[1])
		print totalList
		print sum(totalList)
		
		#allZippedLists should provide info for coordinates for labels
		#of total accretion or erosion areas (labels from totalList)
		allZipped = zip(distList, elevOrigList, elevNewList, \
		deltaList)
		allZippedComp = zip(allZipped, allZipped[1:])
		allZippedList = []
		allZippedLists = []
		for a in allZippedComp:
			if None not in a and sameSign(a[0][3], a[1][3])\ 				and not allZippedList:
				allZippedList.append(a)
			elif None not in a and sameSign(a[0][3], a[1][3]) \
			and allZippedList:	
				allZippedList.append(a[1])
			elif None not in a and not sameSign(a[0][3], a[1][3]):
				allZippedLists.append(allZippedList)
				allZippedList = [a[1]]
				
	plt.suptitle('Profile ' + pname[2:5], fontsize=14)
	plt.xlabel('Distance from Benchmark (m)')
	plt.ylabel('Ellipsoidal Height (m)')
	plt.legend(['June 2001', 'Mar 2017'], loc='upper right')
	#plt.show()
	plt.savefig('/home/nlibassi/Geodesy/Thesis/Project/ProfileData/Plots/Prof' + pname[2:5] + '_200106_201703_EllHtTest2.png') 



