import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const


B = ufloat(1.2301, 1*10**(-3))
e = const.physical_constants['elementary charge']
d = 105.2*(10**(-6))
rho = 8920
m_cuatom = 63.4 * 10**(-27)
n_st = rho/m_cuatom
j = 10**6

m_0 = 9.109 * 10**(-31)
R= ufloat(2.60, 0.13)
#zu ÄNDERNDE WERTE
b = ufloat(0.025, 0.001)
L = ufloat(0.04, 0.001)

Q = b*d




print(d)
print(e[0])

I, U = np.genfromtxt("../Daten/daten_hall_bconst_pos.txt", unpack=True)

U *= 10**(-3)

params, covar_matrix = np.polyfit(I, U, deg= 1, cov=True)

errors = np.sqrt(np.diag(covar_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.8f} ± {error:.8f}')

A = ufloat(params[0], errors[0])
print(f'A: {A}')

n = B/(A*e[0]*d)
print(f"n: {n}")

print(I)
print(U)

z = n/n_st


tau = (2*m_0*L)/((e[0])**2 *n *R * Q)
drift = - j/(n*e[0])

print(f'tau: {tau}')
print(f'z: {z}')
print(f'drift: {drift}')

