import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

U, t = np.genfromtxt("../data/ab.dat", unpack=True)
ulog = np.log(U)
plt.plot(ulog, 
        t,
        'bx',
        label='entladen',
        linewidth=1.5)


Uneu = ulog[:-1]
tneu = t[:-1]
print(U)
print(Uneu)
params, covar_matrix = np.polyfit(Uneu, tneu, deg= 1, cov=True)

errors = np.sqrt(np.diag(covar_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')
x = np.linspace(-3, 2)
plt.plot(x, 
        params[0]*x + params[1],
        'k--',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)
#plt.yscale("log")
plt.show()