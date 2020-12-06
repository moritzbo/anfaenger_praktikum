import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

t, T1, p1, T2, p2, N = np.genfromtxt("python/daten.dat", unpack=True)
t *= 60
T1 += 273.15
T2 += 273.15

plt.plot(t, T1, "bx", markersize=3.7, label=r'Temperatur $T_{1}$')
plt.plot(t, T2, "kx", markersize=3.7, label=r'Temperatur $T_{2}$')
plt.xlabel("$t$ [s]")
plt.ylabel("$T$ [K]")
plt.xticks(np.arange(0, 2110, step=200))
plt.legend(loc="best")
plt.xlim(left=0)
plt.xlim(right=2150)
plt.tight_layout()

plt.savefig("build/plot1.pdf")