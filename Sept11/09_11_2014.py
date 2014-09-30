# coding: utf-8

import numpy as np
from matplotlib import pyplot as plt
plt.ion()

data = np.loadtxt('n6388.txt')
ra = data[:,1]
dec = data[:,2]
ra -= 264.07265
dec += 44.735611
ra *= np.cos(44.735611/57)

plt.clf()
plt.plot(ra,dec, 'bo')
radius = np.sqrt(ra**2 + dec**2)
plt.clf()
plt.scatter(radius, ra)
plt.clf()
radsorted = radius.copy()
radsorted.sort()
radsorted[:50]
center = np.where(radius < 0.001)
radius[center]
center
plt.plot(ra,dec, 'bo')
plt.plot(ra[center],dec[center], 'ro')
plt.axhline(0)
plt.axvline(0)


vel = data[:,4]
vel.std()
vel[center].std()
bc = np.where((radius < 0.001) & (data[:,3] < 17))
bc
vel[bc].std()
vel[center].std()
#get_ipython().magic(u"save 'out' 0-92")
