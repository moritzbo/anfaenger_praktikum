import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

# phi, U = np.genfromtxt("data/phaseOHNEE.dat", unpack=True)

phiM, UM = np.genfromtxt("../data/phaseMIT.dat", unpack=True)

# plt.plot(phi,
#         U,
#         "b-",
#         label="Messwerte OHNE",
#         linewidth=1.5)
print(phiM)
print(UM)
plt.plot(phiM,
        UM,
        "kx",
        label="Messwerte MIT",
        linewidth=1.5)


def sigmoid(phi, a, b, c, d):
   return a*np.cos((np.deg2rad(phi)*b+c))+d
 
 
params, covariance_matrix = curve_fit(sigmoid, phiM, UM, p0=(150, 1, -50, 0))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abcd', params, uncertainties): 
    print(f'{name} = {value:.4f} ± {uncertainty:.4f}')

# ABSTELLPLATZ:             np.deg2rad               

x = np.linspace(0,350)
plt.plot(x, 
        (params[0]*np.cos((np.deg2rad(x)*params[1]+params[2])) + params[3]),
        'b-',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)

 
plt.legend()
plt.show()