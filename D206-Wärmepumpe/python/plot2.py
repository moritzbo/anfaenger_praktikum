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



t, T1, p1, T2, p2, N = np.genfromtxt("python/daten.dat", unpack=True)
t *= 60
T1 += 273.15
T2 += 273.15
p1 += 1
p2 += 1

p1 *= 10**5
p2 *= 10**5


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

Diff1_420 = 2*A1*420 + B1
Diff1_840 = 2*A1*840 + B1
Diff1_1260 = 2*A1*1260 + B1
Diff1_1680 = 2*A1*1680 + B1

Diff2_420 = 2*A2*420 + B2
Diff2_840 = 2*A2*840 + B2
Diff2_1260 = 2*A2*1260 + B2
Diff2_1680 = 2*A2*1680 + B2

print(Diff1_420)
print(Diff1_840)
print(Diff1_1260)
print(Diff1_1680)
print("Jetzt Diff2")
print(Diff2_420)
print(Diff2_840)
print(Diff2_1260)
print(Diff2_1680)

plt.savefig("build/plot2.pdf")

plt.clf()


params3, covariance_matrix3 = curve_fit(linreg, 1/T1, np.log(p1))
uncertainties3 = np.sqrt(np.diag(covariance_matrix3))

plt.plot(1/T1, np.log(p1), "kx", label="Messwerte")
plt.xlabel(r'1/$T_{1}$ [1/K]')
plt.ylabel(r'log($p_{1}$)')
plt.plot(1/T1, linreg(1/T1, *params3), 'b--', label='Lineare Regression')
plt.legend(loc="best")
plt.savefig("build/plot3.pdf")

aplot3 = ufloat(params3[0], uncertainties3[0])
bplot3 = ufloat(params3[1], uncertainties3[1])

M = 0.12091

L = aplot3/M
print(f'L: {L}')

print(f"A: {aplot3}")
print(f'B: {bplot3}')
