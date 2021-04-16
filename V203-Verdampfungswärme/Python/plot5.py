import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

R = const.physical_constants["molar gas constant"][0]

a = ufloat(-4710.774, 43.656)

L = -R * a  



T1, p = np.genfromtxt("Daten/über.tx", unpack=True)


T1 = (T1 + 273.15)

print(f"{L:.3f}")

p = p * 10**(5)

params, covar_matrix = np.polyfit(T1, p, deg= 3, cov=True)

errors = np.sqrt(np.diag(covar_matrix))
# B = aG + b
for name, value, error in zip('abcd', params, errors):
    print(f'{name} = {value:.6f} ± {error:.6f}')
x = np.linspace(390, 480)
plt.plot(x, 
        params[0]*(x**3) + params[1]*(x**2) + params[2]*x + params[3],
        'k--',
        label='Polynom dritter Ordnung',
        linewidth=1.5)
plt.grid()
plt.xlabel(r'$T[\si{\kelvin}]$')
plt.ylabel(r'$\text{ln}(p)$')

plt.errorbar(T1, p, xerr=1, yerr=0.2, fmt='bx', markersize=3.5, label='Messwerte mit Fehlerbalken')
plt.legend()
plt.savefig("build/plot5.pdf")



a = params[0]
b = params[1]
c = params[2]
d = params[3]

T = T1

z = 0.9


def f1(T):
    return (3*a*(T**3) +2*b*(T**2) + c*T)/(a*(T**3) +b*(T**2) + c*T + d) * ( (R*T)/(2)  + np.sqrt(((R*T)/(2))**2 - z*(a*(T**3) +b*(T)**2 + c*T + d)))


#Lp = (3*a*(T**3) +2*b*(T)**2 + c*T)/(a*(T**3) +b*(T)**2 + c*T + d) * ( (R*T)/(2)  + np.sqrt(((R*T)/(2))**2 - a*(a*(T**3) +b*(T)**2 + c*T + d)))
def f2(T):
    return (3*a*(T**3) +2*b*(T**2) + c*T)/(a*(T**3) +b*(T**2) + c*T + d) * ( (R*T)/(2)  - np.sqrt(((R*T)/(2))**2 - z*(a*(T**3) +b*(T)**2 + c*T + d)))

plt.clf()

x1 = np.linspace(390, 480)

plt.plot(x1, 
        f1(x1),
        'k--',
        linewidth=1.5)
plt.grid()
plt.xlabel(r'$T[\si{\kelvin}]$')
plt.ylabel(r'$L[\si{\joule\per\mol}]$')

plt.savefig("build/plot6.pdf")
plt.clf()
plt.plot(x1, 
        f2(x1),
        'k--',
        linewidth=1.5)
plt.grid()
plt.xlabel(r'$T[\si{\kelvin}]$')
plt.ylabel(r'$L[\si{\joule\per\mol}]$')

plt.savefig("build/plot7.pdf")


#Lm = () * ()