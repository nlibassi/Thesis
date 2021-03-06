from scipy import integrate

def calcArea(x1, x2, y1, y2, y3, y4):
	"""
	given 2 x-coordinates and 4 y-coordinates, 
	calculates the equation of two lines and returns 
	the integral between the two.
	"""
	m1 = (y1-y2)/(x1-x2)
	m2 = (y3-y4)/(x1-x2)
	b1 = y1-m1*x1
	b2 = y3-m2*x1
	f1 = lambda x: m1*x + b1
	f2 = lambda x: m2*x + b2
	i1 = integrate.quad(f1, x1, x2)[0] #returns integral as 1st item in tuple
	i2 = integrate.quad(f2, x1, x2)[0]
	print 'm1 = ', m1
	print 'm2 = ', m2
	print 'b1 = ', b1
	print 'b2 = ', b2
	print 'final = ', abs(i1-i2)
	return abs(i1-i2)
'''
first = calcArea(-43.705, -37.435, 40.1947, 39.3647, 38.64408, 38.61456)
second = calcArea(-37.435, -18.735, 39.3647, 38.3047, 38.61456, 38.08033)
'''
first = calcArea(-18.735, -7.155, 38.3047, 37.8447, 38.08033, 37.94831)
print first
#print 'total = ', first + second

