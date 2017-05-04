#new field has already been created 
#why can't anything be written to new field?

from osgeo import ogr
source = ogr.Open('/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30/20160929_BathymetryCorrected/20160929_BathymetryCorrected_attr2.shp', update=True)
layer = source.GetLayer()
layerDefn = layer.GetLayerDefn()

"""
feature = layer.GetFeature(0) #lets get the first feature (FID=='0')
i = feature.GetFieldIndex("TestFld")
feature.SetField(i, 'Chicago')

print i #prints 4 as expected

"""
for feature in layer:
    feature.SetField(4, 'test') #field index is 4

source.Destroy()
source = None
