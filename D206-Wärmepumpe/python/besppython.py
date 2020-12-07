import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem


def T(x, A, B, C):
    return A* x**2 + B* x + C

x_plot = np.linspace(0, 2100)



t, T1, p1, T2, p2, N = np.genfromtxt("daten.dat", unpack=True)
t *= 60
T1 += 273.15
T2 += 273.15
N_mean = ufloat(np.mean(N), sem(N))
params1, covariance_matrix1 = curve_fit(T, t, T1)
params2, covariance_matrix2 = curve_fit(T, t, T2)
uncertainties1 = np.sqrt(np.diag(covariance_matrix1))
uncertainties2 = np.sqrt(np.diag(covariance_matrix2))

plt.plot(t, T1, "bx", markersize=3.7, label=r'Temperatur $T_{1}$')
plt.plot(t, T2, "kx", markersize=3.7, label=r'Temperatur $T_{2}$')
plt.plot(x_plot, T(x_plot, *params1), "-", label=r"Fit zu $T_{1}$")
plt.plot(x_plot, T(x_plot, *params2), "k-", label=r"Fit zu $T_{2}$")
plt.xlim(left=0)
plt.xlim(right=2150)
plt.xlabel("$t$ [s]")
plt.ylabel("$T$ [K]")
plt.xticks(np.arange(0, 2110, step=200))
plt.legend(loc="best")
plt.tight_layout()

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

Diff1_400 = 2*A1*400 + B1
Diff1_800 = 2*A1*800 + B1
Diff1_1200 = 2*A1*1200 + B1
Diff1_1600 = 2*A1*1600 + B1

Diff2_400 = 2*A2*400 + B2
Diff2_800 = 2*A2*800 + B2
Diff2_1200 = 2*A2*1200 + B2
Diff2_1600 = 2*A2*1600 + B2

print(f"Wert A1: {A1}")
print(f"Wert B1: {B1}")

print(Diff1_400)
print(Diff1_800)
print(Diff1_1200)
print(Diff1_1600)
print("Jetzt Diff2")
print(Diff2_400)
print(Diff2_800)
print(Diff2_1200)
print(Diff2_1600)
print(np.mean(N))
print(sem(N))


nu_real_400 = (2*A1*400 + B1)*(4*4185.1 + 750)*(1/N_mean)
nu_real_800 = Diff1_800*(4*4185.1 + 750)*(1/N_mean)
nu_real_1200 = Diff1_1200*(4*4185.1 + 750)*(1/N_mean)
nu_real_1600 = Diff1_1600*(4*4185.1 + 750)*(1/N_mean)
print(nu_real_400)
print(nu_real_800)
print(nu_real_1200)
print(nu_real_1600)


nu_ideal_400 = T(400, params1[0], params1[1], params1[2])/(T(400, params1[0], params1[1], params1[2])-T(400, params2[0], params2[1], params2[2]))
print(nu_ideal_400)
nu_ideal_800 = T(800, params1[0], params1[1], params1[2])/(T(800, params1[0], params1[1], params1[2])-T(800, params2[0], params2[1], params2[2]))
print(nu_ideal_800)
nu_ideal_1200 = T(1200, params1[0], params1[1], params1[2])/(T(1200, params1[0], params1[1], params1[2])-T(1200, params2[0], params2[1], params2[2]))
print(nu_ideal_1200)
nu_ideal_1600 = T(1600, params1[0], params1[1], params1[2])/(T(1600, params1[0], params1[1], params1[2])-T(1600, params2[0], params2[1], params2[2]))
print(nu_ideal_1600)

plt.show()