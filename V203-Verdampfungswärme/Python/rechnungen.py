import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

R = const.physical_constants["molar gas constant"][0]

a = ufloat(-4710.774, 43.656)

L = -R * a  



T1, p = np.genfromtxt("../Daten/über.tx", unpack=True)




print(f"{L:.3f}")

params, covar_matrix = np.polyfit(T1, p, deg= 3, cov=True)

errors = np.sqrt(np.diag(covar_matrix))
# B = aG + b
for name, value, error in zip('abcd', params, errors):
    print(f'{name} = {value:.6f} ± {error:.6f}')



