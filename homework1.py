import numpy as np
from scipy.integrate import quad
from matplotlib import pyplot as plt

def integrand(z):
    return 1/(1+z) / (0.26*(1+z)**3 + 0.74)**0.5

zp = np.linspace(0,20) #discrete redshift points to calculate
tp = [] # empty list to save results
# This method (using 'in') is more pythonic.
for z in zp:
    ans,err = quad(integrand, 0, z)
    tp.append(ans * 13.88)
tp = np.asarray(tp) #convert the mutable list to a static array when finished.
# This conversion isn't necessary so long as both zp and tp have same number of points.

plt.plot(zp,tp)
plt.xlabel('Redshift')
plt.ylabel('Lookback Time in Gyr')
plt.title('AST376 Plot')

# They're gonna have to save it for submission
plt.savefig('hw1.png', bbox_inches='tight') #bbox_inches option just tightens up the produced figure
