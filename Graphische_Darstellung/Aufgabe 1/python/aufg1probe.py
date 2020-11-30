import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

x_messung, y_messung = np.genfromtxt("messungen.txt", unpack=True)
#plt.plot(x_messung, y_messung, 'k.')
#plt.xlim(0, 7)
#plt.ylim(0, 5)
#plt.xlabel(r'$m \ [\si{\gram}]$')
#plt.ylabel(r'$x \ [\si{\centi\meter}]$')
#plt.tight_layout()

params, covar_matrix = np.polyfit(x_messung, y_messung, deg= 1, cov=True)

errors = np.sqrt(np.diag(covar_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.6f} ± {error:.10f}')

a = ufloat(params[0], errors[0])
x = 981 / params[0]
print(x) 
print(a)
def kfunc(a):
    return 981 / a

print(kfunc(a))