import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

A, B = np.genfromtxt("../data/A4grün.dat", unpack=True)

a = A    #ist alpha_1
b = B   #ist alhpa_2
c =  const.physical_constants["speed of light in vacuum"]
n = ufloat(1.45108,0.01991)

aERR = np.array([])
bERR = np.array([])
for i in range(len(a)):
    aERR = np.append(aERR,ufloat(a[i],0.5))
for i in range(len(b)):
    bERR = np.append(bERR,ufloat(b[i],0.5))


beta = unp.arcsin(unp.sin(aERR)/n)
betaRAWERR = unp.std_devs(beta)
betaRAW = unp.nominal_values(beta)
beta2 = np.deg2rad(60) - beta
delta = (aERR+bERR)-(beta + beta2)
deltamean = np.mean(delta)

print(beta)
print(betaRAW)
print(betaRAWERR)