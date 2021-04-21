import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

U, t = np.genfromtxt("../data/ab.dat", unpack=True)

plt.plot(U, 
        t,
        'bx',
        label='entladen',
        linewidth=1.5)

params, covar_matrix = np.polyfit(U, t, deg= 1, cov=True)

errors = np.sqrt(np.diag(covar_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')
x = np.linspace(0, 2)
plt.plot(x, 
        params[0]*x + params[1],
        'k--',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)
plt.show()