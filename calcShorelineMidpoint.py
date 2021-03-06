"""
for use in qgis python console (add qgis modules to work as standalone)

input shapefile/layer contains x, y, z of runup and rundown

use one of the two for loops below: first one gets coordinates from field attributes, second gets coordinates from feature geometry
"""

layer = qgis.utils.iface.activeLayer()
#layer.startEditing()

#surLine field contains survey line for each shoreline measurment (3 points were measured, runup and rundown are being paired here for midpoint measurement)

for num in range(1, layer.featureCount()/2 + 1):
	snum = str(num)
	expr = QgsExpression( "\"surLine\"= " + snum ) 
	it = layer.getFeatures( QgsFeatureRequest( expr ) )
	ids = [i.id() for i in it]
	layer.setSelectedFeatures(ids)
	xlist = []
	ylist = []
	zlist = []
	for f in layer.selectedFeatures():
		xlist.append(f.attributes()[0]) #x (easting) is first field
		ylist.append(f.attributes()[1]) #y (northing) is second field
		zlist.append(f.attributes()[5]) #z ellipsoidal height
	print snum, sum(xlist)/2, sum(ylist)/2

#or write results directly to a file

#for num in range(1, 61) + range(62, 68): #used on March 25 data as missed one point on surLine 61 
for num in range(1, layer.featureCount()/2 + 1):
	snum = str(num)
	expr = QgsExpression( "\"surLine\"= " + snum ) 
	it = layer.getFeatures( QgsFeatureRequest( expr ) )
	ids = [i.id() for i in it]
	layer.setSelectedFeatures(ids)
	xlist = []
	ylist = []
	zlist = []
	for f in layer.selectedFeatures():
		geom = f.geometry()
		p = geom.asPoint()
		xlist.append(p[0]) #
		ylist.append(p[1]) #
		zlist.append(f.attributes()[3])
	print snum, sum(xlist)/2, sum(ylist)/2, sum(zlist)/2



