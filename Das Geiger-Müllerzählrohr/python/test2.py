import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


U, N = np.genfromtxt("../Daten/Kennlinie.dat", unpack=True)

Nerr = np.sqrt(N)
print(Nerr)


#xlimit = np.array([310, 710])
#ylimit = np.array([185, 230])
#plt.errorbar(U, N, xerr=None, yerr=Nerr, fmt='kx', markersize=3.5, label='Messwerte mit Fehlerbalken')

#plt.xlabel(r'$U[\si{\volt}]$')
#plt.ylabel(r'$N[\text{Imp} / {60}\si{\second}]$')
#plt.grid()




#RECHNUNG

Ulin = []
Nlin = []
Nlinerr = []


for j in range(27):
    Ulin.append(U[j+5])  
    Nlin.append(N[j+5]) 
    Nlinerr.append(Nerr[j+5])

print(Ulin)
print(Nlin)

Nerrarray = unp.uarray(Nlin, Nlinerr)


params, covariance_matrix = np.polyfit(Ulin, Nlin, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

pande0 = ufloat(params[0], errors[0])
pande1 = ufloat(params[1], errors[1])


for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

#x_plot = np.linspace(370, 630)

#plt.plot(
#    x_plot,
#    params[0] * x_plot + params[1], "b--",
#    label='Lineare Ausgleichsgerade',
#    linewidth=1.5,
#)

#plt.legend(loc='upper left')
#plt.tight_layout()
#plt.savefig("build/plot1.pdf")


def percentfunction(k, j):
    return (100/2.6) * (pande0 * k + pande1 - pande0 * j -  pande1)/(pande0* k + pande1)

print(f'{percentfunction(630, 370):.6f}')

print(f"{Nerrarray[0]:.6f}")
print(f"{Nerrarray[26]:.6f}")