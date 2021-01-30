import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

theta, N = np.genfromtxt("data/Bragg.txt", unpack=True)

plt.plot(theta, N, "kx", label="Zählraten")
plt.grid()
plt.xlabel(r'$\theta[\textdegree]$')
plt.ylabel(r'$N[\si{{\text{Imp}}\per\second}]$')
plt.legend(loc="upper left")
plt.savefig("build/plot1.pdf")