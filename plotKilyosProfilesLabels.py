#from __future__ import division
from osgeo import ogr
from scipy import integrate
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe


source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/ProfilePoints/2001_2017_ProfilePtsWEllHts.shp')
layer = source.GetLayer()

outFile = '/home/nlibassi/Geodesy/Thesis/Project/ProfileData/ProfileScratch3.txt'


profNames = ['pr0000106', 'pr4000106', 'pr3000106', 'pr7700106', 'pr7000106', 'pr2000106', 'pr6000106', 'pr1000106', 'pr5000106']

Shoreline2001Dict = {'pr0000106': 36.6975, 'pr1000106': 36.5645
, 'pr2000106': 36.5675
, 'pr3000106': 37.1915
, 'pr4000106': 36.566
, 'pr5000106':36.615
,'pr6000106':36.6805
,'pr7000106':36.648
, 'pr7700106':37.0815

}

Shoreline2017Dict = {'pr0000106': 36.6265, 'pr1000106': 36.60175, 'pr2000106': 36.64775, 'pr3000106': 36.64175, 'pr4000106': 36.5825
, 'pr5000106':36.5795
,'pr6000106':36.6075
,'pr7000106':36.59
, 'pr7700106':36.5615
}


def sameSign(x, y):
	#tests whether or not given args have same sign
	return (x<0 and y<0) or (x>0 and y>0)

def calcArea(x1, x2, y1, y2, y3, y4):
	"""
	given 2 x-coordinates and 4 y-coordinates, 
	calculates the equation of two lines and returns 
	the difference of the two integrals.
	"""
	if x1-x2 != 0:
		m1 = (y1-y2)/(x1-x2)
		m2 = (y3-y4)/(x1-x2)
		b1 = y1-m1*x1
		b2 = y3-m2*x1
		f1 = lambda x: m1*x + b1
		f2 = lambda x: m2*x + b2
		i1 = integrate.quad(f1, x1, x2)[0] #returns integral as 1st item in tuple
		i2 = integrate.quad(f2, x1, x2)[0]
		return abs(i1-i2)
		#return i1-i2 

def lineIntersection(line1, line2): 
    """
	takes line1 and line2 as two lists of tuples or 
	two tuples of tuples (8 total values, x and y of 4 pts)
	returns coordinates of intersection of given lines
    """
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) 

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

matplotlib.rcParams['font.size'] = 10

for pname in profNames:
	distList = []
	elevOrigList = []
	elevNewList = []
	layer.SetAttributeFilter("Filename = " + "'" + pname + "'")

	for feature in layer: 
		distList.append(feature.GetField('DistanceTo'))
		elevOrig = feature.GetField('EllHt2001')
		elevNew = feature.GetField('EllHt2017')
		elevOrigList.append(elevOrig)
		elevNewList.append(elevNew)

	fig = plt.figure()
	ax = fig.add_subplot(111)
	plt.plot(distList, elevOrigList)
	plt.plot(distList, elevNewList)

	#plt.plot(33.07, 36.71, 'b+')
	#plt.plot(29.51, 36.67, 'g+')
	Shore2001 = Shoreline2001Dict[pname]
	Shore2017 = Shoreline2017Dict[pname]
	plt.axhline(y=Shore2001, color='b', linestyle='-')
	plt.axhline(y=Shore2017, color='g', linestyle='-')
	plt.text(-150, Shore2001 + 0.5, str(Shore2001), color='b', path_effects=[pe.withStroke(linewidth=3,
                                                                                  foreground="w")])
	plt.text(-150, Shore2017 - 0.5, str(Shore2017), color='g', path_effects=[pe.withStroke(linewidth=3,
                                                                                  foreground="w")])
	hZipped = zip(elevOrigList, elevNewList)
	deltaList = []

	delta = 0
	for h in hZipped:
		if None not in h:
			delta = h[1] - h[0]  #new elev value minus orig elev value
			deltaList.append(delta)
		else:
			deltaList.append(None)

	allZipped = zip(distList, elevOrigList, elevNewList, \
	deltaList)
	#print allZipped[:10]
	allZippedComp = zip(allZipped, allZipped[1:])
	#print allZippedComp[:10]
	area = 0
	areaList = []
	count = 0
	countList = []
	indexList = [3] #guessing that around the first three will have a None value, adjust later
	#subList = []
	#binFirstIndex = 0
	labelList = [] #to hold list of three-element lists: x, y, area value to be printed

	with open(outFile, 'a') as out:
		for a in allZippedComp:
			if None not in a[0] and None not in a[1] and sameSign(a[0][3], a[1][3]):
				localArea = calcArea(a[0][0], a[1][0], a[0][1], a[1][1], a[0][2], a[1][2])
				if localArea: #some localAreas are None?
					area += localArea
				#count += 1
			elif None not in a[0] and None not in a[1] and not sameSign(a[0][3], a[1][3]):
				indexList.append(allZippedComp.index(a) + 1)
				intersectPts = lineIntersection([(a[0][0], a[0][1]), (a[1][0], a[1][1])], \
								[(a[0][0], a[0][2]), (a[1][0], a[1][2])])

				areaLast = calcArea(a[0][0], intersectPts[0], a[0][1], intersectPts[1], a[0][2], intersectPts[1])
				area += areaLast

				if a[0][3] < 0:
					areaList.append(round(area, 3) * -1)
				else:
					areaList.append(round(area, 3))
				
				areaFirst = calcArea(intersectPts[0], a[1][0], intersectPts[1], a[1][1],  intersectPts[1], a[1][2])
				area = areaFirst

		indexListStg = zip(indexList, indexList[1:])

		for i in indexListStg:
			if distList[i[0]:i[1]]:
				xmin = min(distList[i[0]:i[1]])
				xmax = max(distList[i[0]:i[1]])
				ymin = min(elevOrigList[i[0]:i[1]]+elevNewList[i[0]:i[1]])
				ymax = max(elevOrigList[i[0]:i[1]]+elevNewList[i[0]:i[1]])
				labelx = (xmin + xmax)/2
				labely = (ymin + ymax)/2
				labelList.append([labelx, labely, areaList[indexListStg.index(i)]])
							
		print areaList
		print sum(areaList)
		print 'Length of area list: %d' % len(areaList)
		print 'Length of label list: %d' % len(labelList)
		print labelList		

	sumLabel = '$Net change: %.2f m^2$' % sum(areaList)
	plt.suptitle('Profile ' + pname[2:5], fontsize=14)
	plt.xlabel('Distance from Benchmark (m)')
	plt.ylabel('Ellipsoidal Height (m)')
	for s in labelList:
		if s[2] > 5 or s[2] < -5:  #abs(s[2]) > 1 removes too many labels ???
			plt.text(s[0], s[1], str(round(s[2], 2)))
	plt.text(0.2, 0.1, sumLabel, ha='center', va='center', transform=ax.transAxes, path_effects=[pe.withStroke(linewidth=3,
                                                                                  foreground="w")])
	#plt.text(0.1, 0.9,'matplotlib', ha='center', va='center')
	plt.legend(['June 2001', 'Mar 2017'], loc='upper right')
	#plt.show()
	plt.savefig('/home/nlibassi/Geodesy/Thesis/Project/ProfileData/Plots/Prof' + pname[2:5] + '_200106_201703_EllHt.png') 

'''
Sample a from allZippedComp:
((-43.705, 40.1947, 38.64408, -1.550619999999995), (-37.435, 39.3647, 38.61456, -0.7501400000000018))
'''

