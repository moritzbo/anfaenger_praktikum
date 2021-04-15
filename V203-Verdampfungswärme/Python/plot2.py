import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

T1, Tunnnnnnnötig, p = np.genfromtxt("Daten/ndd.txt", unpack=True)

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
x = np.linspace(0.0027, 0.0034)
plt.plot(x, 
        params[0]*x + params[1],
        'k--',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)
plt.grid()
plt.xlabel(r'$1/T[1/\si{\kelvin}]$')
plt.ylabel(r'$\text{ln}(p)$')
plt.legend()
plt.savefig("build/plot2.pdf")
