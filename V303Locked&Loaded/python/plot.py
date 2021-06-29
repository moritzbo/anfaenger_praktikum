import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

phi, U = np.genfromtxt("data/phaseOHNEE.dat", unpack=True)

phiM, UM = np.genfromtxt("data/phaseMIT.dat", unpack=True)

plt.plot(phi,
        U,
        "b-",
        label="Messwerte OHNE",
        linewidth=1.5)

plt.plot(phiM,
        UM,
        "k-",
        label="Messwerte MIT",
        linewidth=1.5)


def sigmoid(phi, a, b, c):
   return a*np.cos(phi+b)+c


params, covariance_matrix = curve_fit(sigmoid, phi, U)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('abc', params, uncertainties): 
    print(f'{name} = {value:.4f} ± {uncertainty:.4f}')


x = np.linspace(-1,0.8)
plt.plot(x, 
        params[0]*x + params[1],
        'k--',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)

plt.legend()
plt.savefig("build/plot1.pdf")