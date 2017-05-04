fileList = ['/home/nlibassi/Geodesy/Thesis/Project/20170325/20170325am/CTD/CTD_2017032501.csv', '/home/nlibassi/Geodesy/Thesis/Project/20170325/20170325am/CTD/CTD_2017032502.csv', '/home/nlibassi/Geodesy/Thesis/Project/20170325/20170325am/CTD/CTD_2017032503.csv']

def calcMeanSoundVel(inFile):
	with open(inFile, 'r') as f:
		f.next()
		conductivityVals = []
		depthVals = []
		tempVals = []
		salinityVals = []
		soundVelVals = []
		lineList = []
		for line in f:
			lineVals = line.split(',')
			if float(lineVals[3]) >= 7 and float(lineVals[3]) <= 8:
				conductivityVals.append(float(lineVals[2]))
				depthVals.append(float(lineVals[3]))
				tempVals.append(float(lineVals[4]))
				salinityVals.append(float(lineVals[6]))
				soundVelVals.append(float(lineVals[7]))

	print('File {}'.format(inFile.rsplit('/')[-1]))
	print('Mean conductivity is {} mS/cm'.format(sum(conductivityVals)/len(conductivityVals)))
	print('Mean depth is {} m'.format(sum(depthVals)/len(depthVals)))
	print('Mean temperature is {} C'.format(sum(tempVals)/len(tempVals)))
	print('Mean salinity is {} g/kg'.format(sum(salinityVals)/len(salinityVals)))
	print('Mean sound velocity is {} m/s'.format(sum(soundVelVals)/len(soundVelVals)))
	print('Max depth is {} m'.format(max(depthVals)))
	print('Min depth is {} m\n'.format(min(depthVals)))

	return sum(soundVelVals)/len(soundVelVals)

meanSoundVelVals = []
for f in fileList:
	meanSoundVelVals.append(calcMeanSoundVel(f))

print('Mean of sound velocity means: {} m/s'.format(sum(meanSoundVelVals)/len(meanSoundVelVals)))


