import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

T1, p = np.genfromtxt("Daten/über.tx", unpack=True)

T1 = T1 + 273.15

p = p * 10**(2)

plt.errorbar(T1, p, xerr=1, yerr=0.2, fmt='bx', markersize=3.5, label='Messwerte mit Fehlerbalken')
plt.legend()
plt.xlabel(r'$T[\si{\kelvin}]$')
plt.ylabel(r'$p[\si{\kilo\pascal}]$')
plt.tight_layout()
plt.grid()

plt.savefig("build/plot3.pdf")