import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

light = const.physical_constants['speed of light in vacuum']
c = light[0]

Ug = [0.4000, 0.7644, 1.1699, 0.3466]
v = [c/(578e3), c/(546e3), c/(435e3), c/(408e3)]

plt.plot(v, 
        Ug,
        'bx',
        label='Spannungswerte',
        linewidth=0.5)
plt.plot(c/408e3, 
        0.3466,
        'rx',
        label='Ausreißer',
        linewidth=1)

Ugreal = [0.4000, 0.7644, 1.1699]
vreal = [c/578e3, c/546e3, c/435e3]

def sigmoid(x, a, b):
    return a*x+b


params, covariance_matrix = curve_fit(sigmoid, vreal, Ugreal)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:.7f} ± {uncertainty:.7f}')

x = np.linspace(0,800)
plt.plot(x, 
        (params[0]*x + params[1]),
        'k--',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)

plt.axhline(y=0, color='k', linestyle='--', linewidth=1, label="Nullgerade")

plt.ylabel(r'$U_g [\si{\volt}]$')
plt.xlabel(r'$\nu [\si{\tera\hertz}]$')
plt.grid()
plt.legend()
# plt.show()
plt.savefig("build/plot5.pdf")
