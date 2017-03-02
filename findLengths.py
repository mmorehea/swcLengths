import sys
import os
import code
import numpy as np
import math


swcInput = sys.argv[1]

dtype = [('id', int), ('type', int), ('x', float), ('y', float), ('z', float), ('r', float), ('parent', int)]
data = np.genfromtxt(swcInput)

parents = data[:,-1]

root = np.where(parents==-1)

length = 0.0
for ii in range(data.shape[0]):
    #print ii
    each = data[ii]
    parent = each[-1]
    if parent == -1:
        continue
    x = each[2]
    y = each[3]
    z = each[4]
    myParent = data[parent]
    pX = myParent[2]
    pY = myParent[3]
    pZ = myParent[4]
    newLength = math.sqrt(np.power((x-pX),2) + np.power((y-pY),2) + np.power((z-pZ),2))
    length += newLength
print length
