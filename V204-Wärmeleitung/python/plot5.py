import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


n, a, b, c, d, e, f, g, h = np.genfromtxt("data/dynamisch2.txt", unpack =True)


plt.plot(n/2, a, 'b-', label="T1 Messing", markersize=1)
plt.plot(n/2, b, 'k-', label="T2 Messing", markersize=1)

plt.grid()
plt.legend()

plt.ylabel(r"$T[\si{\degreeCelsius}]$")
plt.xlabel(r"$t[\si{\second}]")

plt.savefig("build/plot4.pdf")