import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const


U, N = np.genfromtxt("Daten/Kennlinie.dat", unpack=True)

Nerr = np.sqrt(N)
print(Nerr)


#xlimit = np.array([310, 710])
#ylimit = np.array([185, 230])
plt.errorbar(U, N, xerr=None, yerr=Nerr, fmt='kx', markersize=3.5, label='Messwerte mit Fehlerbalken')

plt.xlabel(r'$U\;/\;\si{\volt}$')
plt.ylabel(r'$N\;/\;\sfrac{1}{\,\SI{60}{\second}}$')
plt.grid()
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("build/plot1.pdf")

