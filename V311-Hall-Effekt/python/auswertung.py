import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const


B = ufloat(1.2301, 1*10**(-3))
e = const.physical_constants['elementary charge']
h = const.physical_constants['Planck constant']

d = 105.2*(10**(-6))
rho = 8920
m_cuatom = 63.4 * 10**(-27)
n_st = rho/m_cuatom
j = 10**6
T = 293.15
k = const.physical_constants['Boltzmann constant']


m_0 = 9.109 * 10**(-31)
R= ufloat(2.60, 0.13)
#zu ÄNDERNDE WERTE
b = ufloat(0.025, 0.005)
L = ufloat(0.04, 0.005)

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
mu = (-e[0]*tau)/(2*m_0)
fermi = (h[0]**2)/(2*m_0) * (((3*n)/(8*np.pi))**2)**(1/3)
totgeschw1 = ((2*fermi)/m_0)**(1/2) 
totgeschw2 = ((3*k[0]*T)/(m_0))**(1/2)

diskr = totgeschw2/totgeschw1

lambda1 = tau * totgeschw1
lambda2 = tau * totgeschw2 

print(f'tau: {tau}')
print(f'z: {z}')
print(f'drift: {drift}')
print(f'mu: {mu}')
print(f'fermienergie: {fermi}')
print(f'totgeschw1: {totgeschw1}')
print(f'totgeschw2: {totgeschw2}')
print(f'diskr: {diskr}')
print(f'lambda1: {lambda1}')
print(f'lambda2: {lambda2}')