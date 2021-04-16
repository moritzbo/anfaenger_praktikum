import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

T1, Tunnnnnnnötig, p = np.genfromtxt("Daten/ndd.txt", unpack=True)

T1 = T1 + 273.15

p = p * 10**(-1)

plt.errorbar(T1, p, xerr=1, yerr=1, fmt='bx', markersize=3.5, label='Messwerte mit Fehlerbalken')
plt.legend()
plt.xlabel(r'$T[\si{\kelvin}]$')
plt.ylabel(r'$p[\si{\kilo\pascal}]$')
plt.tight_layout()
plt.grid()

plt.savefig("build/plot1.pdf")