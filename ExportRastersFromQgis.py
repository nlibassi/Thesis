'''to be used from qgis console'''

#refresh file browser if tifs not showing up at first

##################

out = '/home/nlibassi/Geodesy/Thesis/Project/Raster/ITRF96TM30/201703_RST_05m_v2' #no trailing slash for copy/paste

lyrsToExport = [l for l in iface.legendInterface().layers() if l.type() == 1] #gets all raster layers in legend (type 0 is vector)

for layer in lyrsToExport:
	fileName = out + '/' + out.split('/')[-1] + layer.name().replace(' ', '') + '.tif'
	fileWriter = QgsRasterFileWriter(fileName)
	pipe = QgsRasterPipe()
	provider = layer.dataProvider()
	if not pipe.set(provider.clone()):
		print 'cannot set pipe provider'
		continue
	fileWriter.writeRaster(pipe, provider.xSize(), provider.ySize(), provider.extent(), provider.crs())

############ OR

import os

out = '/home/nlibassi/Geodesy/Thesis/Project/Raster/ITRF96TM30/20160929_SeaPtsCorrected_RSTmw5_20170304' #no trailing slash

lyrsToExport = [l for l in iface.legendInterface().layers() if l.type() == 1] #gets all raster layers in legend (type 0 is vector)

for layer in lyrsToExport:
	fileName = os.path.join(out, out.split('/')[-1] + layer.name().replace(' ', '') + '.tif')
	fileWriter = QgsRasterFileWriter(fileName)
	pipe = QgsRasterPipe()
	provider = layer.dataProvider()
	if not pipe.set(provider.clone()):
		print 'cannot set pipe provider'
		continue
	fileWriter.writeRaster(pipe, provider.xSize(), provider.ySize(), provider.extent(), provider.crs())

####
#all layers in legend

out = '/home/nlibassi/Geodesy/Thesis/Project/Raster/ITRF96TM30/20160929_SeaPtsCorrected_RSTmw5_20170304/' #trailing slash or edit as above

for layer in iface.legendInterface().layers():
	fileName = out + layer.name().replace(' ', '') + '.tif'
	fileWriter = QgsRasterFileWriter(fileName)
	pipe = QgsRasterPipe()
	provider = layer.dataProvider()
	if not pipe.set(provider.clone()):
		print 'cannot set pipe provider'
		continue
	fileWriter.writeRaster(pipe, provider.xSize(), provider.ySize(), provider.extent(), provider.crs())
