import processing


layer = iface.legendInterface().layers()[0]  #if only one layer or find better way to do this
features = processing.features(layer)

#OR

count = 0
depths = []
for feature in layer.getFeatures():  #getFeatures() returns an interator of the layer's features
	depths.append([count, feature.attributes()[-2]])
	count +=1
	

#To get field by name rather than index:

idx = layer.fieldNameIndex('name')

for feature in layer.getFeatures():
	depths.append(feature.attributes()[idx])







#add field to shp with ogr: (can be done while shp is open in qgis)

from osgeo import ogr
source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/20160929_BathymetryCorrected/20160929_BathymetryCorrected_attr.shp', update=True)
layerO = source.GetLayer()
layerDefn = layerO.GetLayerDefn() 

fieldNames = [layerDefn.GetFieldDefn(i).GetName() for i in range(layerDefn.GetFieldCount())]

#check for existence of current field with name of new field
print len(fieldNames), 'MW5Depth' in fieldNames
5 False

newField = ogr.FieldDefn('MW5Depth', ogr.OFTReal)

layerO.CreateField(newField)

#not sure if both of these are necessary but may be necessary before writing data to new field
source.Destroy()
source = None 

#ogr field types
"""
FIELD_TYPES = [
    'int',          # OFTInteger, Simple 32bit integer
    None,           # OFTIntegerList, List of 32bit integers
    'float',       # OFTReal, Double Precision floating point
    None,           # OFTRealList, List of doubles
    'str',          # OFTString, String of ASCII chars
    None,           # OFTStringList, Array of strings
    None,           # OFTWideString, deprecated
    None,           # OFTWideStringList, deprecated
    None,           # OFTBinary, Raw Binary data
    None,           # OFTDate, Date
    None,           # OFTTime, Time
    None,           # OFTDateTime, Date and Time
    ]
"""



#print values from a field:

for feature in layerO:
    print feature.GetField("Depth") #where Depth is example field name

#add field with shapely or others?



#No need for get field index in future, just use field names from LayerDefn

from osgeo import ogr
source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/20160929_BathymetryCorrected/20160929_BathymetryCorrected_attr2.shp', update=True)
layer = source.GetLayer()
layerDefn = layer.GetLayerDefn()
fieldNames = [layerDefn.GetFieldDefn(i).GetName() for i in range(layerDefn.GetFieldCount())]
type(layerDefn)
<class 'osgeo.ogr.FeatureDefn'>
fieldNames
['latitude', 'longitude', 'elevation', 'name', 'TestFld']
feature = layer.GetFeature(0)
feature.GetFieldIndex('TestFld')
#output: 4

for feature in layer:
    feature.SetField(4, 'test')

source.Destroy()
source = None

#getting dictionary in the following format with pyqgis: {rowNum: depth}

layer = iface.legendInterface().layers()[0]
depths = {}
for feature in layer.getFeatures():
	depths.append(feature.attributes()[1]:feature.attributes()[-1])
	
#how to write to a field?

#have not yet been able to write to a field in ogr using SetField() method
