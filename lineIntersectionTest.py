import matplotlib.pyplot as plt

def line_intersection(line1, line2): #line1 and line2 contain endpoints of lines, two lists of tuples or two tuples of tuples
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

A = (-18.735, 38.0833)
B = (-7.155, 37.94831)
C = (-18.735, 38.3047)
D = (-7.155, 37.8447)

print line_intersection((A, B), (C, D))

plt.figure()

plt.plot([A[0], B[0]], [A[1], B[1]]) 
plt.plot([C[0], D[0]], [C[1], D[1]])

plt.text(A[0], A[1], 'A')
plt.text(B[0], B[1], 'B')
plt.text(C[0], C[1], 'C')
plt.text(D[0], D[1], 'D')

#plt.plot(B)
#plt.plot(C)
#plt.plot(D)
plt.show()



