import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

#x_messung, y_messung = np.genfromtxt("python/messungen.txt", unpack=True)
#plt.plot(x_messung, y_messung, 'k.', label="Messwerte")
#plt.xlim(0, 7)
#plt.ylim(0, 5)
#plt.xlabel(r'$m \ [\si{\gram}]$')
#plt.ylabel(r'$x \ [\si{\centi\meter}]$')
#plt.tight_layout()
#
#params, covar_matrix = np.polyfit(x_messung, y_messung, deg= 1, cov=True)
#
#errors = np.sqrt(np.diag(covar_matrix))
#
#x = np.linspace(0, 7)
#plt.plot(x, 
#        params[0]*x + params[1],
#        'b--',
#        label='Lineare Regression',
#        linewidth=1.5)
#
#plt.legend(loc="best")
#
#plt.savefig('build/plot2.pdf')






t,n = np.loadtxt('daten/Vanadium.txt', skiprows=1, unpack=True)

Nerr = []

for x in n:
    Nerr.append(np.sqrt(x))

N = unp.uarray(n,Nerr)

plt.plot(t, n, 'k.',label="Vandium Messdaten")

plt.xlabel("t")
plt.ylabel("N")
plt.tight_layout()

plt.legend(loc="best")

plt.savefig('build/plot1.pdf')
#plt.show()