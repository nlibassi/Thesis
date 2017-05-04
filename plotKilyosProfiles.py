#from __future__ import division
from osgeo import ogr
from scipy import integrate
import matplotlib.pyplot as plt


source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/ProfilePoints/2001_2017_ProfilePtsWEllHts.shp')
layer = source.GetLayer()

outFile = '/home/nlibassi/Geodesy/Thesis/Project/ProfileData/ProfileScratch3.txt'

profNames = ['pr0000106', 'pr4000106', 'pr3000106', 'pr7700106', 'pr7000106', 'pr2000106', 'pr6000106', 'pr1000106', 'pr5000106']

def sameSign(x, y):
	return (x<0 and y<0) or (x>0 and y>0)

def calcArea(x1, x2, y1, y2, y3, y4):
	"""
	given 2 x-coordinates and 4 y-coordinates, 
	calculates the equation of two lines and returns 
	the difference of the two integrals.
	"""
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

def lineIntersection(line1, line2): #takes line1 and line2 as two lists of tuples or two tuples of tuples (8 total values, x and y of 4 pts)
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
		subList = []
		labelList = [] #will hold list of three-element lists: x, y, value to be printed

		with open(outFile, 'a') as out:
			for a in allZippedComp:
				if None not in a[0] and None not in a[1] and sameSign(a[0][3], a[1][3]):
					localArea = calcArea(a[0][0], a[1][0], a[0][1], a[1][1], a[0][2], a[1][2])
					area += localArea
					subList.append(a[0])
					#print subList; break
				elif None not in a[0] and None not in a[1] and not sameSign(a[0][3], a[1][3]):
					#subList.append(a[0])
					intersectPts = lineIntersection([(a[0][0], a[0][1]), (a[1][0], a[1][1])], \
									[(a[0][0], a[0][2]), (a[1][0], a[1][2])])

					areaLast = calcArea(a[0][0], intersectPts[0], a[0][1], intersectPts[1], a[0][2], intersectPts[1])
					area += areaLast

					if a[0][3] < 0:
						areaList.append(round(area, 3) * -1)
					else:
						areaList.append(round(area, 3))
					
					#print len(subList); print subList; break
					xList = [s[0] for s in subList]
					yList = [s[1] - s[2] for s in subList]
					#print xList, subList; break
					labelx = sum(xList)/len(subList)
					labely = sum(yList)/len(subList)
					#print labelx, labely
					#break
					labelList.append([labelx, labely, area])
					#subList = []

					areaFirst = calcArea(intersectPts[0], a[1][0], intersectPts[1], a[1][1],  intersectPts[1], a[1][2])
					area = areaFirst
					#area = 0
						

					
			print areaList
			print sum(areaList) 	
			print labelList	
				
	plt.suptitle('Profile ' + pname[2:5], fontsize=14)
	plt.xlabel('Distance from Benchmark (m)')
	plt.ylabel('Ellipsoidal Height (m)')
	for s in labelList:
		plt.text(s[0], s[1], str(round(s[2], 2)))
	plt.legend(['June 2001', 'Mar 2017'], loc='upper right')
	#plt.show()
	plt.savefig('/home/nlibassi/Geodesy/Thesis/Project/ProfileData/Plots/Prof' + pname[2:5] + '_200106_201703_EllHtTest2.png') 

'''
Sample a from allZippedComp:
((-43.705, 40.1947, 38.64408, -1.550619999999995), (-37.435, 39.3647, 38.61456, -0.7501400000000018))
'''
