import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

theta, N = np.genfromtxt("../data/ComptonOhne.txt", unpack=True)

tau = 90 * 10**(-6)

Nerror = []
for x in N:
    Nerror.append((x)**(1/2))

Npoisson = unp.uarray(N, Nerror)

print(Npoisson)

Nkorr = []

for x in Npoisson:
    Nkorr.append(x/(1 - (tau * x)))


d = 201.4 *10**(-12)

#print(Nkorr)
np.savetxt(
    '../data/Nohnefehler.txt',
    np.column_stack([N, Nerror]),
    fmt=['%d', '%.4f'],       # first column integer, second 4 digits float
    delimiter='   ',
    header='N,Nerror',
)


np.savetxt(
    '../data/Nohnekorrigiert.txt',
    np.column_stack([unp.nominal_values(Nkorr), unp.std_devs(Nkorr)]),
    fmt=['%.6f', '%.6f'],       # first column integer, second 4 digits float
    delimiter='   ',
    header='N,Nerror',
)



wavelen = 2*d * np.sin(np.deg2rad(theta))


print(wavelen)
np.savetxt(
    '../data/wavelength.txt',
    np.column_stack([wavelen, wavelen]),       # first column integer, second 4 digits float
    delimiter='   ',
    header='N,Nerror',
)