import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

f, V, a, b= np.genfromtxt("../data/teilcd.dat", unpack=True)

flog = np.log(f)
plt.plot(f, 
        V, 
        'bx',
        label='Messwerte',
        linewidth=1.5)
#plt.xscale("log")
#plt.show()


params, covar_matrix = np.polyfit(f, V, deg= 1, cov=True)
 
errors = np.sqrt(np.diag(covar_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')
x = np.linspace(0, 10000)
plt.plot(x, 
         params[0]*x + params[1],
         'k--',
         label='Ausgleichsgerade',
         linewidth=1.5)
plt.show()