import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

# phi, U = np.genfromtxt("data/phaseOHNEE.dat", unpack=True)

phiM, UM = np.genfromtxt("data/phaseMIT.dat", unpack=True)

# plt.plot(phi,
#         U,
#         "b-",
#         label="Messwerte OHNE",
#         linewidth=1.5)
 
plt.plot(phiM,
        UM,
        "kx",
        label="Messwerte MIT",
        linewidth=1.5)


def sigmoid(phi, a, b, c, d):
   return a*np.cos((phi*b+c))+d
 
 
params, covariance_matrix = curve_fit(sigmoid, phiM, UM)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abcd', params, uncertainties): 
    print(f'{name} = {value:.4f} ± {uncertainty:.4f}')

# ABSTELLPLATZ:             np.deg2rad         , p0=(0, 1, -50, 0)      

x = np.linspace(0,350)
plt.plot(x, 
        (0.065*params[0]*np.cos((np.deg2rad(x)*0.9*params[1]+params[2]+0.5)) + params[3]),
        'b-',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)

 
plt.legend()
plt.savefig("build/plot2.pdf")