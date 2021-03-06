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
    aERR = np.append(aERR,ufloat(a[i],0.00872665))
for i in range(len(b)):
    bERR = np.append(bERR,ufloat(b[i],0.00872665))
n = unp.sin(a)/unp.sin(b)   
nerr = unp.sin(aERR)/unp.sin(bERR)
print(f"Brechungsindex array:{n}")

nmean = np.mean(nerr)
print(f"Brechungsindex mean:{nmean:.6}")
nsem = sem(n)
print(f"{nsem:.6}")

aufgabeeins = 299792458.0/nmean
print(f"{aufgabeeins:.2f}")

d = 0.0585
beta = unp.arcsin(unp.sin(aERR)/nmean)
betamean = np.mean(beta)
strahl = d * unp.sin(aERR-bERR)/unp.cos(bERR)
strahlmean =  np.mean(strahl)
print("#### STRAHL STANDART (gemessenes beta)####")
print(strahl)
print(f"{strahlmean:.4f}")
print(np.mean(bERR))
print(f"betamean =  {betamean:.4f}")
strahlneu = d * unp.sin(aERR-beta)/unp.cos(beta)
strahlneumean = np.mean(strahlneu)
# print(f"strahl für jden einzeln: {strahlneu:.4f}")
print("#### STRAHL alternativ)####")
print(strahlneu)
print(f"strahlneu = {strahlneumean:.4f}")

beta2mean = np.deg2rad(60) - betamean
print(f"{beta2mean:.4f}")
deltamean = (np.mean(aERR)+np.mean(bERR))-(betamean+ beta2mean)
delta = (aERR+bERR)-(betamean+ beta2mean)
print(delta)
print(f"deltaauslenkung = {deltamean:.4f}")

nLIT =  1.49
nprozent = 100*(nmean-nLIT)/nLIT
print(f"Abweichung brechungsindex in % = {nprozent:.4f}")


print("########## beta errechnet:")
print(beta*180/np.pi)