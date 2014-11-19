# 09_16_2014.py
# Script from Practical intro to research 09/16/14
# Jacob Hummel


import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt

#import matplotlib as mpl
#mpl.rc('figure', figsize=(16,12))

data = np.loadtxt('data/co2_monthly_data.txt')

time = data[:,2]
co2 = data[:,4]

plt.clf()
plt.plot(time, co2, label='Monthly Mean')
plt.xlabel('Time [yr]')
plt.ylabel('CO2 Mole Fraction [ppm]')


def fit(x, a, b, c):
    return a*x**2 + b*x + c

coeff, err = optimize.curve_fit(fit, time, co2)
a,b,c = coeff

time = np.linspace(1958, 2040)
plt.plot(time, fit(time, a,b,c), label='our fit')
plt.legend(loc=0)
