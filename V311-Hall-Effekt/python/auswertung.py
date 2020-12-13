import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const


B = ufloat(1230.1, 1)
e = const.physical_constants['elementary charge']
d = 105.2*(10**(-6))
print(d)
print(e[0])

I, U = np.genfromtxt("../Daten/daten_hall_bconst_pos.txt", unpack=True)

U *= 10**(-3)

params, covar_matrix = np.polyfit(I, U, deg= 1, cov=True)

errors = np.sqrt(np.diag(covar_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.8f} ± {error:.8f}')

A = ufloat(params[0], errors[0])

n = B/(A*e[0]*d)
print(f"n: {n}")

print(I)
print(U)