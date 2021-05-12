import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


n, a, b, c, d, e, f, g, h = np.genfromtxt("data/dynamisch2.txt", unpack =True)


plt.plot(n/2, g, 'b-', label="T7 Edelstahl", markersize=1)
plt.plot(n/2, h, 'k-', label="T8 Edelstahl", markersize=1)

plt.grid()
plt.legend()

plt.ylabel(r"$T[\si{\degreeCelsius}]$")
plt.xlabel(r"$t[\si{\second}]")

plt.savefig("build/plot5.pdf")