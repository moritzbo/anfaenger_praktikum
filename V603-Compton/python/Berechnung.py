import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

theta, N = np.genfromtxt("../data/EmissionCu.txt", unpack=True)


winkelalpha = 22.5

winkelbeta = 20.2


planck = const.physical_constants["Planck constant"][0]
print(planck)

light = const.physical_constants["speed of light in vacuum"][0]
print(light)

d = 201.4 * 10**(-12)

elem = const.physical_constants["elementary charge"][0]


Ealpha = (planck * light) / (2*d * elem * np.sin(np.deg2rad(winkelalpha)))
Ebeta = (planck * light) / (2*d * elem *np.sin(np.deg2rad(winkelbeta)))

print(f"Energie von ALPHA: {Ealpha}")
print(f"Energie von BETA: {Ebeta}")

Ealphalit = 8048
Ebetalit = 8907


Ealphaabw = 100 - 100*(Ealpha/Ealphalit)
Ebetaabw = 100 - 100*(Ebeta/Ebetalit)

print(f"Abweichung der Energie von ALPHA: {Ealphaabw}")
print(f"Abweichung derEnergie von BETA: {Ebetaabw}")

winkellitalpha = 22.49
winkellitbeta = 20.22

Ealphaabwwinkel = 100 - 100 * (winkelalpha/winkellitalpha)
Ebetaabwwinkel = 100 - 100 * (winkelbeta/winkellitbeta)


print(f"Abweichung der Winkel von ALPHA: {Ealphaabwwinkel}")
print(f"Abweichung der Winkel von BETA: {Ebetaabwwinkel}")
