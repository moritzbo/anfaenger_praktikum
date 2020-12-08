
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem

R = 8.314462618

def T(x, A, B, C):
    return A* x**2 + B* x + C

def linreg(x, a, b):
    return -(a/R)*x + b 


x_plot = np.linspace(0, 2100)



t, T1, p1, T2, p2, N = np.genfromtxt("daten.dat", unpack=True)
t *= 60
T1 += 273.15
T2 += 273.15
p1 += 1
p2 += 1
p1 *= 10**5
p2 *= 10**5

kappa = 1.14
T0 = 273.15
p0 = 10**5
rho0 = 5.51

print(p1)
print(p2)

N_mean = ufloat(np.mean(N), sem(N))

params1, covariance_matrix1 = curve_fit(T, t, T1)
params2, covariance_matrix2 = curve_fit(T, t, T2)
uncertainties1 = np.sqrt(np.diag(covariance_matrix1))
uncertainties2 = np.sqrt(np.diag(covariance_matrix2))

for name, value, uncertainty in zip('ABC', params1, uncertainties1): 
    print(f'{name} = {value} ± {uncertainty}')

for name2, value2, uncertainty2 in zip('ABC', params2, uncertainties2): 
    print(f'{name2} = {value2} ± {uncertainty2}')

A1 = ufloat(params1[0], uncertainties1[0])
B1 = ufloat(params1[1], uncertainties1[1])
C1 = ufloat(params1[2], uncertainties1[2])

A2 = ufloat(params2[0], uncertainties2[0])
B2 = ufloat(params2[1], uncertainties2[1])
C2 = ufloat(params2[2], uncertainties2[2])

Diff1_420 = 2*A1*420 + B1
Diff1_840 = 2*A1*840 + B1
Diff1_1260 = 2*A1*1260 + B1
Diff1_1680 = 2*A1*1680 + B1

Diff2_420 = 2*A2*420 + B2
Diff2_840 = 2*A2*840 + B2
Diff2_1260 = 2*A2*1260 + B2
Diff2_1680 = 2*A2*1680 + B2

print(f"p1[7]: {p1[7]}")
print(f"p1[14]: {p1[14]}")
print(f"p1[21]: {p1[21]}")
print(f"p1[28]: {p1[28]}")

print(f"p2[7]: {p2[7]}")
print(f"p2[14]: {p2[14]}")
print(f"p2[21]: {p2[21]}")
print(f"p2[28]: {p2[28]}")

print(f"T2[7]: {T2[7]}")
print(f"T2[14]: {T2[14]}")
print(f"T2[21]: {T2[21]}")
print(f"T2[28]: {T2[28]}")

