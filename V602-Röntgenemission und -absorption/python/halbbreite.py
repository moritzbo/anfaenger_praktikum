import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

theta, N = np.genfromtxt("../data/Emissionsspektrum.txt", unpack=True)


halbintalpha = 5050/2

halbintbeta = 1599/2

print(halbintalpha)
print(halbintbeta)

planck = const.physical_constants["Planck constant"][0]
print(planck)

light = const.physical_constants["speed of light in vacuum"][0]
print(light)

d = 201.4 * 10**(-12)

elem = const.physical_constants["elementary charge"][0]
print(elem)

alphadegmain = np.deg2rad(22.5)

betadegmain = np.deg2rad(20.2)

Ealpha = planck * light / (2*d * np.sin(alphadegmain)) / elem
Ebeta = planck * light / (2*d * np.sin(betadegmain)) / elem

print(Ealpha)
print(Ebeta)

alphadeglinks = np.deg2rad(20.06)
betadeglinks = np.deg2rad(22.35)
alphadegrechts = np.deg2rad(20.55)
betadegrechts = np.deg2rad(22.85)


Ealphalinks = planck * light / (2*d * np.sin(alphadeglinks)) / elem
Ealpharechts = planck * light / (2*d * np.sin(alphadegrechts)) / elem

Ebetalinks = planck * light / (2*d * np.sin(betadeglinks)) / elem
Ebetarechts = planck * light / (2*d * np.sin(betadegrechts)) / elem


print(f"alpha links {Ealphalinks}")
print(f"alpha rechts {Ealpharechts}")
print(f"beta links {Ebetalinks}")
print(f"beta rechts {Ebetarechts}")

deltaalpha = Ealphalinks - Ealpharechts
deltabeta = Ebetalinks - Ebetarechts

print(f"delta alpha {deltaalpha}")
print(f"delta beta {deltabeta}")

Aalpha = Ealpha / deltaalpha
Abeta = Ebeta / deltabeta

print(F"Auflöse alpha {Aalpha}")
print(F"Auflöse beta {Abeta}")

ryddi = const.physical_constants["Rydberg constant times hc in eV"][0]

#sigma1 = 29 - ((8987.96)/(13.6057))**(1/2)




ZKupfer = 29

Ekabs = ufloat(8987.96, 0.15)

sigma1 = ZKupfer - unp.sqrt( Ekabs/ryddi)
sigma2 = ZKupfer - 2* unp.sqrt((ryddi* (ZKupfer-sigma1)**2 - Ealpha)/(ryddi))
sigma3 = ZKupfer - 2* unp.sqrt((ryddi* (ZKupfer-sigma1)**2 - Ebeta)/(ryddi))


print(F"SIGMA1 ist: {sigma1:.4f}")
print(F"SIGMA2 ist: {sigma2:.4f}")
print(F"SIGMA3 ist: {sigma3:.4f}")
print(ryddi)

