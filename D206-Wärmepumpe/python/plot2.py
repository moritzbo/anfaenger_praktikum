import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit



def T(x, A, B, C):
    return A* x**2 + B* x + C

x_plot = np.linspace(0, 2100)



t, T1, p1, T2, p2, N = np.genfromtxt("python/daten.dat", unpack=True)
t *= 60
T1 += 273.15
T2 += 273.15

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


plt.savefig("build/plot2.pdf")