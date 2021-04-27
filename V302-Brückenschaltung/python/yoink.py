import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

f, U = np.genfromtxt("daten/hz.dat", unpack=True)


omega = 10**9 / (2 * np.pi * 294.75 * 1000)

x = np.linspace(0, 2.5 * 10**4, 1000)
w0 = np.ones(1000)
w0 *= omega
OMEGALULW = x / w0
sigmoid = (np.sqrt(1/9 * ((OMEGALULW**2 - 1)**2)/((1 - OMEGALULW**2)**2 + 9 * OMEGALULW**2)))*0.7
w0 = np.ones(len(f))
w0 *= omega
l = f / w0

plt.plot(l, U, 'bx', label='Messwerte')
plt.plot(OMEGALULW, sigmoid, 'k--', label='Theoriekurve')
plt.xscale("log")

plt.xlabel(r"$\Omega$")
plt.ylabel(r"$U_{B}$[$\si{\volt}$]")


plt.grid()
plt.legend(loc="best")

omeganull = 2 * np.pi *omega
print(omeganull)
print(omega)

plt.savefig("build/plot1.pdf")