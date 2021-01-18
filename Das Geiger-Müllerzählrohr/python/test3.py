import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


U, I, Ierr, N = np.genfromtxt("Daten/Zaehlrohrstrom.dat", unpack=True)

N = N/60

I = I * 10**(-6)
Ierr = Ierr * 10**(-6)

Nerr = np.sqrt(N)

print(Nerr)
print(N)
print(I)

e = const.physical_constants["elementary charge"][0]

print(e)

def Z(x, y):
    return x/(e * y)

Zwerte = Z(I, N) / (10**(10))

Zfehler = [0.21, 0.22, 0.27, 0.29, 0.34, 0.40, 0.40, 0.50]  
for i in range(8):
    nmitfehler = ufloat(N[i], Nerr[i])
    imitfehler = ufloat(I[i], Ierr[i])
    print(f'Das {i}te Z ist {Z(imitfehler, nmitfehler)}')
    

print(Zwerte)
print(Zfehler)


plt.errorbar(U, Zwerte, xerr=None, yerr=Zfehler, fmt='kx', markersize=4.5, label='Werte mit Fehlerbalken')
plt.xlabel(r'$U[\si{\volt}]$')
plt.ylabel(r'$Z \cdot {10}^{10}$')
plt.legend(loc="upper left")
plt.savefig("build/plot2.pdf")