import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

print(const.physical_constants["elementary charge"])

e = const.physical_constants["elementary charge"][0]

N1 = 96041 / 120
N12 = 158479 / 120
N2 = 76518 / 120

N1err = np.sqrt(N1)
N2err = np.sqrt(N2)
N12err = np.sqrt(N12)

N1u = ufloat(N1, N1err)
N2u = ufloat(N2, N2err)
N12u = ufloat(N12, N12err)

def totzeit (k, l, m):
    return (k + l - m)/(2*k*l)

print("Totzeit")
h = totzeit(N1u, N2u, N12u)
print(f"Totzeit ist {totzeit(N1u, N2u, N12u):.6f}")




U, N = np.genfromtxt("../Daten/Kennlinie.dat", unpack=True)

U2, I, Ierr = np.genfromtxt("../Daten/Zaehlrohrstrom.dat", unpack=True)

e = 

I = I * 10**(-6)
print(I)

Ierr = Ierr * 10**(-6)

Iges = []

NNeu = []


for u in range(7):
    Iges.append(ufloat(I[u], Ierr[u]))

def Z(x, y):
    return x/(e*y)


Nerr = np.sqrt(N)
#print(Nerr)


#xlimit = np.array([310, 710])
#ylimit = np.array([185, 230])
#plt.errorbar(U, N, xerr=None, yerr=Nerr, fmt='kx', markersize=3.5, label='Messwerte mit Fehlerbalken')

#plt.xlabel(r'$U[\si{\volt}]$')
#plt.ylabel(r'$N[\text{Imp} / {60}\si{\second}]$')
#plt.grid()
#plt.legend(loc='upper left')
#plt.tight_layout()
#plt.savefig("build/plot1.pdf")


#RECHNUNG

Ulin = []
Nlin = []
Nlinerr = []


for j in range(27):
    Ulin.append(U[j+5])  
    Nlin.append(N[j+5]) 
    Nlinerr.append(Nerr[j+5])

print(Ulin)
print(Nlin)

Nerrarray = unp.uarray(Nlin, Nlinerr)


params, covariance_matrix = np.polyfit(Ulin, Nlin, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

print(N[5])
print(N[31])


N = N/60


N_5array = ufloat(N[5], np.sqrt(N[5]))
N_31array = ufloat(N[31], np.sqrt(N[31]))

def percentfunction (b, c):
    return 100 * ((b - c)/ b)



def newfunc (h,p):
    return (100/2.6)  * ((h - p)/ h)

value = percentfunction(N_31array, N_5array)

def blabla(var):
    return var/260

print(f"{newfunc(N_31array, N_5array):.6f}")
print(f"{blabla(value):.6f}")


Imean = np.sum(Iges)/8

print(Imean)

print(Iges)