from osgeo import ogr
import matplotlib.pyplot as plt

source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/2001_2002_ProfilePoints_ITRF.shp')
layer = source.GetLayer()

#outFile = '/home/nlibassi/Geodesy/Thesis/Project/ProfileData/ProfileScratch.txt'

profNames = ['pr000', 'pr400', 'pr300', 'pr770', 'pr700', 'pr200', 'pr600', 'pr100', 'pr500']
yearNames = ['0106', '0206']

def produceProfLists(x, z):
	distList = []
	elevList = []
	for feature in layer:
		distList.append(feature.GetField(x))
		elevList.append(feature.GetField(z))	
	return distList, elevList

for pname in profNames:
	layer.SetAttributeFilter("Filename = " + "'" + pname + '0106'+ "'")
	dist01List, elev01List = produceProfLists('DistanceTo', 'Elevation_')
	layer.SetAttributeFilter("Filename = " + "'" + pname + '0206'+ "'")
	dist02List, elev02List = produceProfLists('DistanceTo', 'Elevation_')
	#all01 = zip(dist01List, elev01List)
	#all02 = zip(dist02List, elev02List)
	#print dist01List

	plt.figure()
	plt.plot(dist01List, elev01List)
	plt.plot(dist02List, elev02List)
	plt.suptitle('Profile ' + pname[2:5], fontsize=14)
	plt.xlabel('Distance from Benchmark (m)')
	plt.ylabel('Ellipsoidal Height (m)')
	plt.legend(['June 2001', 'June 2002'], loc='upper right')
	#plt.show()
	plt.savefig('/home/nlibassi/Geodesy/Thesis/Project/ProfileData/Plots/Prof' + pname[2:] + '_200106_200206.png') 


