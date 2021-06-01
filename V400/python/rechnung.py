import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

A, B = np.genfromtxt("../data/A2.dat", unpack=True)

a =np.deg2rad(A)
b = np.deg2rad(B)
c =  const.physical_constants["speed of light in vacuum"]

aERR = np.array([])
bERR = np.array([])
for i in range(len(a)):
    aERR = np.append(aERR,ufloat(a[i],0.5))
for i in range(len(b)):
    bERR = np.append(bERR,ufloat(b[i],0.5))
n = unp.sin(a)/unp.sin(b)   
nerr = unp.sin(aERR)/unp.sin(bERR)
print(f"Brechungsindex:{n}")

nmean = np.mean(nerr)
print(f"{nmean:.6}")
nsem = sem(n)
print(f"{nsem:.6}")

aufgabeeins = 299792458.0/nmean
print(f"{aufgabeeins:.2f}")

d = 0.0585
beta = unp.arcsin(unp.sin(aERR)/nmean)
betamean = np.mean(beta)
strahl = d * unp.sin(aERR-bERR)/unp.cos(bERR)
strahlmean =  np.mean(strahl)
print(f"{strahlmean:.4f}")
print(np.mean(bERR))
print(f"betamean =  {betamean:.4f}")
strahlneu = d * unp.sin(aERR-beta)/unp.cos(beta)
strahlneumean = np.mean(strahlneu)
print(f"{strahlneumean:.4f}")

beta2mean = np.deg2rad(60) - betamean
print(beta2mean)