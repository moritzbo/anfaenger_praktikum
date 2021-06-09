import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

def gauss(x, sigma, alpha, beta):
    return beta/(np.sqrt(2 * np.pi *sigma**(2))) * np.exp(-(x-alpha)**2 / (2* sigma**2))


f, U= np.genfromtxt("../daten/kurve.txt", unpack=True)

U = U/10


x = np.linspace(13, 36, 2000)
plt.plot(f,
        U,
        "bx",
        label="Spannungsmesswerte",
        linewidth=1.5)
plt.axhline(y=1/2**(1/2), color='k', linestyle='--')

params, covariance_matrix = curve_fit(gauss, f, U,  p0=(1, 21.6, 1))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('σαβ', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

plt.plot(x, gauss(x, *params), "-")

plt.show()