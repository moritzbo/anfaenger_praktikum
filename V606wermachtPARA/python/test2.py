import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

rhoNd = 7240

rhoDy = 7800

rhoGd = 7400

molNd = 336.48/1000

molDy = 373.00/1000

molGd = 362.50/1000

T = 293.15

mu0arr = const.physical_constants['vacuum mag. permeability']

mubarr = const.physical_constants['Bohr magneton']

karr = const.physical_constants['Boltzmann constant']

avogadroarr = const.physical_constants['Avogadro constant']


NA = avogadroarr[0]
mu0 = mu0arr[0]
mub = mubarr[0]
k = karr[0]

gnd = 0.727
gdy = 1.333
ggd = 2.000

ndj = 24.75
dyj = 63.75
gdj = 15.75


Nnd = 2 * NA * rhoNd/molNd
Ndy = 2 * NA * rhoDy/molDy
Ngd = 2 * NA * rhoGd/molGd

CHInd = (mu0 * mub**(2) * gnd**(2) * Nnd * ndj)/(3 * k * T )
CHIdy = (mu0 * mub**(2) * gdy**(2) * Ndy * dyj)/(3 * k * T )
CHIgd = (mu0 * mub**(2) * ggd**(2) * Ngd * gdj)/(3 * k * T )


print(f"𝜒Nd: {CHInd:.6f}")
print(f"𝜒Dy: {CHIdy:.6f}")
print(f"𝜒Gd: {CHIgd:.6f}")



LängeND = 0.177
LängeDY = 0.175
LängeGD = 0.177

MasseND = 0.01408
MasseDY = 0.01510
MasseGD = 0.00848

Qnd = MasseND / (LängeND * rhoNd)
Qdy = MasseDY / (LängeDY * rhoDy)
Qgd = MasseGD / (LängeGD * rhoGd)


print(f"QNd: {Qnd:.8f}")
print(f"QDy: {Qdy:.8f}")
print(f"QGd: {Qgd:.8f}")


F = 8.66*10**(-5)

Usp = 0.72

CHInd2 =[]
CHIdy2 =[]
CHIgd2 = []

deltaU_nd = np.array([0.60*10**(-3),
0.30*10**(-3),
0.39*10**(-3)
])
deltaU_dy = np.array([14.50*10**(-3),
13.55*10**(-3),
14.05*10**(-3)
])

deltaU_gd = np.array([6.85*10**(-3),
7.00*10**(-3),
6.71*10**(-3)
])
print(deltaU_nd)

CHInd2 = 4 * F* deltaU_nd / (Qnd * Usp)
CHIdy2 = 4 * F* deltaU_dy / (Qdy * Usp)
CHIgd2 = 4 * F* deltaU_gd / (Qgd * Usp)

#print(f"QNd: {CHInd2:.8}")
#print(f"QDy: {CHIdy2:.8}")
#print(f"QGd: {CHIgd2:.8}")

print(CHIdy2)
print(CHIgd2)


CHInd2mean = np.mean(CHInd2)
CHIdy2mean =np.mean(CHIdy2)
CHIgd2mean= np.mean(CHIgd2)

CHInd2sem = sem(CHInd2)
CHIdy2sem = sem(CHIdy2)
CHIgd2sem = sem(CHIgd2)

CHInd2full = ufloat(CHInd2mean, CHInd2sem)
CHIdy2full = ufloat(CHIdy2mean, CHIdy2sem)
CHIgd2full = ufloat(CHIgd2mean, CHIgd2sem)

print(f"𝜒Ndmean: {CHInd2full:.8}")
print(f"𝜒Dymean: {CHIdy2full:.8}")
print(f"𝜒Gdmean: {CHIgd2full:.8}")



R3 = 1000

deltaR_nd = np.array([0.09,
0.08,
0.08
])

deltaR_dy = np.array([1.52,
1.52,
1.51
])

deltaR_gd = np.array([0.76,
0.75,
0.73
])

CHInd3 = 2 * F* deltaR_nd / (Qnd * R3)
CHIdy3 = 2 * F* deltaR_dy / (Qdy * R3)
CHIgd3 = 2 * F* deltaR_gd / (Qgd * R3)

CHInd3mean = np.mean(CHInd3)
CHIdy3mean =np.mean(CHIdy3)
CHIgd3mean= np.mean(CHIgd3)

CHInd3sem = sem(CHInd3)
CHIdy3sem = sem(CHIdy3)
CHIgd3sem = sem(CHIgd3)

CHInd3full = ufloat(CHInd3mean, CHInd3sem)
CHIdy3full = ufloat(CHIdy3mean, CHIdy3sem)
CHIgd3full = ufloat(CHIgd3mean, CHIgd3sem)

print(f"𝜒Ndmean: {CHInd3full:.8}")
print(f"𝜒Dymean: {CHIdy3full:.8}")
print(f"𝜒Gdmean: {CHIgd3full:.8}")

CHIspannungABWEICHUNGnd = 100*(CHInd2full-CHInd)/CHInd
CHIspannungABWEICHUNGdy = 100*(CHIdy2full-CHIdy)/CHIdy
CHIspannungABWEICHUNGgd = 100*(CHIgd2full-CHIgd)/CHIgd

print(f"Abweichung % Spannungsmethode von Nd= {CHIspannungABWEICHUNGnd:.5f}")
print(f"Abweichung % Spannungsmethode von Dy= {CHIspannungABWEICHUNGdy:.5f}")
print(f"Abweichung % Spannungsmethode von Gd= {CHIspannungABWEICHUNGgd:.5f}")

CHIwiderstandABWEICHUNGnd = 100*(CHInd3full-CHInd)/CHInd
CHIwiderstandABWEICHUNGdy = 100*(CHIdy3full-CHIdy)/CHIdy
CHIwiderstandABWEICHUNGgd = 100*(CHIgd3full-CHIgd)/CHIgd

print(f"Abweichung % Widerstandsmethode von Nd= {CHIwiderstandABWEICHUNGnd:.5f}")
print(f"Abweichung % Widerstandsmethode von Dy= {CHIwiderstandABWEICHUNGdy:.5f}")
print(f"Abweichung % Widerstandsmethode von Gd= {CHIwiderstandABWEICHUNGgd:.5f}")