import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

T1, p = np.genfromtxt("Daten/über.tx", unpack=True)

T1 = (T1 + 273.15)

T1_neu = 1/T1
p_neu = np.log(p)


plt.plot(T1_neu, 
        p_neu,
        'bx',
        label='Messwerte',
        linewidth=1.5)

print(T1_neu)
print(p_neu)
params, covar_matrix = np.polyfit(T1_neu, p_neu, deg= 1, cov=True)

errors = np.sqrt(np.diag(covar_matrix))
# B = aG + b
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')
x = np.linspace(0.0021, 0.00255)
plt.plot(x, 
        params[0]*x + params[1],
        'k--',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)
plt.grid()
plt.xlabel(r'$1/T[1/\si{\kelvin}]$')
plt.ylabel(r'$\text{ln}(p)$')
plt.legend()

R = const.physical_constants["molar gas constant"][0]

a = ufloat(params[0], errors[0])

erg = - R * a
print(a)
print(f"{erg:.3f}")
plt.savefig("build/plot4.pdf")
