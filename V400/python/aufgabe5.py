import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

d100 = (1/100)*10**(-3)
d300 =  (1/300)*10**(-3)
d600 =  (1/600)*10**(-3)

##### GRÜNES LAMBDA

k, phi = np.genfromtxt("../data/A5grün100.dat", unpack=True)
phiERR = np.array([])
for i in range(len(phi)):
    phiERR = np.append(phiERR,ufloat(np.deg2rad(phi[i]),0.00872665))
lambda100g = d100*unp.sin(phiERR/k)
print(f"lamda_grün/100 ={lambda100g}")

k, phi = np.genfromtxt("../data/A5grün300.dat", unpack=True)
phiERR = np.array([])
for i in range(len(phi)):
    phiERR = np.append(phiERR,ufloat(np.deg2rad(phi[i]),0.00872665))
lambda300g = d300*unp.sin(phiERR/k)
print(f"lamda_grün/300 ={lambda300g}")

k, phi = np.genfromtxt("../data/A5grün600.dat", unpack=True)
phiERR = np.array([])
for i in range(len(phi)):
    phiERR = np.append(phiERR,ufloat(np.deg2rad(phi[i]),0.00872665))
lambda600g = d600*unp.sin(phiERR/k)
print(f"lamda_grün/600 ={lambda600g}")

lamdaGrünGesamt = np.append(lambda100g, np.append(lambda300g, lambda600g))
lamdaGRÜNmean = np.mean(lamdaGrünGesamt)
print(f"lamdaGESAMTmeanGRÜN ={lamdaGRÜNmean}")

##### ROTES LAMBDA

k, phi = np.genfromtxt("../data/A5rot100.dat", unpack=True)
phiERR = np.array([])
for i in range(len(phi)):
    phiERR = np.append(phiERR,ufloat(np.deg2rad(phi[i]),0.00872665))
lambda100r = d100*unp.sin(phiERR/k)
print(f"lamda_rot/100 ={lambda100r}")

k, phi = np.genfromtxt("../data/A5rot300.dat", unpack=True)
phiERR = np.array([])
for i in range(len(phi)):
    phiERR = np.append(phiERR,ufloat(np.deg2rad(phi[i]),0.00872665))
lambda300r = d300*unp.sin(phiERR/k)
print(f"lamda_rot/300 ={lambda300r}")

k, phi = np.genfromtxt("../data/A5rot600.dat", unpack=True)
phiERR = np.array([])
for i in range(len(phi)):
    phiERR = np.append(phiERR,ufloat(np.deg2rad(phi[i]),0.00872665))
lambda600r = d600*unp.sin(phiERR/k)
print(f"lamda_rot/600 ={lambda600r}")

lamdarotGesamt = np.append(lambda100r, np.append(lambda300r, lambda600r))
lamdaROTmean = np.mean(lamdarotGesamt)
print(f"lamdaGESAMTmeanROT ={lamdaROTmean}")