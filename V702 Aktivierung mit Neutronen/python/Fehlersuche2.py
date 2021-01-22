import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

t,n = np.loadtxt('../daten/Vanadium.txt', skiprows=1, unpack=True)

Nerr = []

for x in n:
    Nerr.append(np.sqrt(x))

N = unp.uarray(n,Nerr)


print(N)
