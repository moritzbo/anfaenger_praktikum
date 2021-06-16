import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

I, U = np.genfromtxt("data/gelb.dat", unpack=True)

plt.plot(U, 
        I,
        'bx',
        label='Messwerte',
        linewidth=0.5)
plt.grid()
plt.legend()
plt.ylabel(r'$I [\si{\nano\ampere}]$')
plt.xlabel(r'$U[\si{\volt}]$')
plt.savefig("build/plot6.pdf")
plt.clf()

lolI   = []
lolU   = []
for i in range(21):
#    print(I[i+18])
   lolI = np.append(lolI, I[i+36]) 
for i in range(21):
#    print(U[i+18])
   lolU = np.append(lolU, U[i+36]) 

plt.plot(lolU, 
        lolI,
        'bx',
        label='Messwerte',
        linewidth=0.5)

plt.grid()
plt.legend()
plt.ylabel(r'$I [\si{\nano\ampere}]$')
plt.xlabel(r'$U[\si{\volt}]$')

plt.savefig("build/plot7.pdf")