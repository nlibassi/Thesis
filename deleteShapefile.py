#example

import os, glob

location = '/home/nlibassi/Geodesy/Thesis/Project/Vector/ITRF96TM30'

for f in glob.glob(os.path.join(location, '20160929_RSTOrigToPt.*')):
    os.remove(f)

