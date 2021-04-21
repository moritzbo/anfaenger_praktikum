import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

U, t = np.genfromtxt("data/ab.dat", unpack=True)
ulog = np.log(U)


Uneu = ulog[:-1]
tneu = t[:-1]
tneu = tneu * (10)**(-4)

plt.plot(tneu, 
        Uneu, 
        'bx',
        label='Messwerte',
        linewidth=1.5)
print(U)
print(Uneu)
params, covar_matrix = np.polyfit(tneu, Uneu, deg= 1, cov=True)

errors = np.sqrt(np.diag(covar_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')
x = np.linspace(0, 0.043)
plt.plot(x, 
        params[0]*x + params[1],
        'k--',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)

plt.grid()
plt.legend()
plt.xlabel(r'$t[\si{\second}]$')
plt.ylabel(r'$\text{ln}(U_c)$')


yo = ufloat(params[0], errors[0])

tau = - 1/(yo)
print(tau)

plt.savefig("build/plot1.pdf")
