import numpy as np
import scipy as sp
import matplotlib
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from scipy import integrate
import math

l = 633*10**(-9)*10**3 #mm
L = 1140 #mm

x2, I2 = np.genfromtxt("../Mr. Data/doppel2.dat", unpack=True)


def g(x2, b, x0, s):
    return 4*(l/(np.pi*b*np.sin((x2-x0)/L)))**2*(np.sin((np.pi*b*np.sin((x2-x0)/L))/l))**2*(np.cos((np.pi*s*np.sin((x2-x0)/L))/l))**2
params2, covariance_matrix2 = curve_fit(g, x2, I2, p0=(0.15, 25.01, 0.15))
errors2 = np.sqrt(np.diag(covariance_matrix2))

x_plot2 = np.linspace(0,50, 10000)

plt.plot(x_plot2,g(x_plot2, *params2),'red',label='Fitfunktion')

print('b=', ufloat(params2[0],errors2[0]))
print('x0 =', ufloat(params2[1],errors2[1]))
print('s =', ufloat(params2[2],errors2[2]))

plt.plot(x2, I2, 'kx', label='Messwerte')

plt.show()