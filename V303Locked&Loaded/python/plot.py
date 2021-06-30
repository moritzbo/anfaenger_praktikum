import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

phi, U = np.genfromtxt("data/phaseOHNEE.dat", unpack=True)

# phiM, UM = np.genfromtxt("data/phaseMIT.dat", unpack=True)

plt.plot(phi,
        U,
        "kx",
        label="Messwerte OHNE",
        linewidth=1.5)

# plt.plot(phiM,
#         UM,
#         "k-",
#         label="Messwerte MIT",
#         linewidth=1.5)


def sigmoid(phi, a, b, c, d):
   return a*np.cos((np.deg2rad(phi)*b+c))+d
 
 
params, covariance_matrix = curve_fit(sigmoid, phi, U, p0=(94.67, 0.80, -16+3.1415, -4.3))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abcd', params, uncertainties): 
    print(f'{name} = {value:.4f} ± {uncertainty:.4f}')

# ABSTELLPLATZ:             np.deg2rad    , p0=(-94, 1, -50, 0) , p0=(150, 1, -50, 0)

x = np.linspace(0,350)
plt.plot(x, 
        (params[0]*np.cos((np.deg2rad(x)*params[1]+params[2])) + params[3]),
        'b-',
        label='Ausgleichsfunktion',
        linewidth=1.5)

plt.ylabel(r'$U [\si{\volt}]$')
plt.xlabel(r'$\phi [\si{\degree}]$')

plt.legend()
plt.savefig("build/plot1.pdf")

#leerzeile
