indexListStg = [(5, 6), (6, 9)]
# (12, 970), (970, 2183), (2183, 3914), (3914, 7048), (7048, 7050), (7050, 7051), (7051, 7053), (7053, 7984), (7984, 7985), (7985, 7989), (7989, 7990)]


allZippedTest = [(-55.095, 41.4747, None, None), (-52.245, 40.9847, None, None), (-48.065, 40.4447, None, None), (-43.705, 40.1947, 38.64408, -1.550619999999995), (-37.435, 39.3647, 38.61456, -0.7501400000000018), (-18.735, 38.3047, 38.08033, -0.2243700000000004), (-7.155, 37.8447, 37.94831, 0.1036099999999962), (-0.13, 37.6967, 37.86183, 0.16512999999999778), (7.77, 37.4947, 37.69497, 0.20026999999999617), (10.745, 37.4147, 37.65726, 0.24255999999999744)]



for i in indexListStg:
	xList = allZippedTest[i[0]:i[1]][0]
	print xList

'''
for i in indexListStg:
	#xList = [a[0] for a in allZippedTest[indexListStg[i][0]:indexListStg[i][1]]]
	xList = [a[0] for a in allZippedTest[i[0]:i[1]]]
	print xList

'''
