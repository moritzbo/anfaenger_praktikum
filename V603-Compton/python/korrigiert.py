import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

theta, N = np.genfromtxt("../data/ComptonAl.txt", unpack=True)

tau = 90 * 10**(-6)

Nerror = []
for x in N:
    Nerror.append(sqrt(x))

Npoisson = np.uarray(N, Nerror)

print(Npoisson)

Nkorr = []

for x in Npoisson:
    Nkorr.np.append(x/(1 - (tau*x)))


print(Nkorr)