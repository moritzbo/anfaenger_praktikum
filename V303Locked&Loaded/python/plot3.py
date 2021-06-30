import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

d, U = np.genfromtxt("data/licht.dat", unpack=True)
d=d*10**(-3) 
plt.plot(d,
        U,
        "kx",
        label="Messwerte",
        linewidth=1.5)


def sigmoid(d, a, b):
   return a* 1/(d**2) + b 
 
 
params, covariance_matrix = curve_fit(sigmoid, d, U, p0=(1, 1))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:.4f} ± {uncertainty:.4f}')

x = np.linspace(0.05,0.52)
plt.plot(x, 
        params[0]*1/(x)+params[1],
        'b-',
        label='Ausgleichsfunktion',
        linewidth=1.5)

plt.ylabel(r'$U [\si{\volt}]$')
plt.xlabel(r'$d [\si{\meter}]$')

plt.legend()       
# plt.show() 
plt.savefig("build/plot3.pdf")