import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

tiefe45, delta45, I45 = np.genfromtxt("Data/45aufgabe2.dat", unpack=True)
tiefe70, delta70, I70 = np.genfromtxt("Data/70aufgabe2.dat", unpack=True)

alphaS = np.deg2rad(80.06)
fnull = 2e6
c = 1800

plt.plot(tiefe45,
        I45,
        "bx",
        label="Pumpleistung 45%",
        linewidth=1.5)

plt.plot(tiefe70,
        I70,
        "kx",
        label="Pumpleistung 70%",
        linewidth=1.5)
plt.ylabel(r'I[$\si{\volt\squared\per\second}$]')
plt.xlabel(r'Messtiefe [$\si{\micro\second}$]')

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("build/plot4.pdf")
plt.clf()

gesch45 = delta45*c/(fnull * 2 * np.cos(alphaS))
gesch70 = delta70*c/(fnull * 2 * np.cos(alphaS))

plt.plot(tiefe45,
        gesch45,
        "bx",
        label="Pumpleistung 45%",
        linewidth=1.5)

plt.plot(tiefe70,
        gesch70,
        "kx",
        label="Pumpleistung 70%",
        linewidth=1.5)

plt.ylabel(r'v[$\si{\meter\per\second}$]')
plt.xlabel(r'Messtiefe [$\si{\micro\second}$]')

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("build/plot5.pdf")