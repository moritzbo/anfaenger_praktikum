import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

I, U = np.genfromtxt("data/violett.dat", unpack=True)


lolI   = []
lolU   = []
for i in range(9):
#    print(I[i+16])
   lolI = np.append(lolI, I[i+15]) 
for i in range(9):
#    print(U[i+16])
   lolU = np.append(lolU, U[i+15]) 
sqrtI = np.sqrt(lolI)
# # print(I)
# # print(lolI)
# sqrtI = np.sqrt(lolI)
# # print(sqrtI)
# print(sqrtI.size)


plt.plot(U, 
        np.sqrt(I),
        'bx',
        label='Messwerte',
        linewidth=0.5)

plt.ylabel(r'$\left( I [\si{\nano\ampere}] \right)^{1/2}$')
plt.xlabel(r'$U[\si{\volt}]$')

# plt.xlabel(r'$$')
# plt.ylabel(r'$$')

# plt.xlim(-1,1.25)


def sigmoid(x, a, b):
    return a*x+b


params, covariance_matrix = curve_fit(sigmoid, lolU, sqrtI)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:.4f} ± {uncertainty:.4f}')


x = np.linspace(0.0,1.0)
plt.plot(x, 
        params[0]*x + params[1],
        'k--',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)

plt.axhline(y=0, color='g', linestyle='--', linewidth=1.5, label="Nullgerade")

plt.grid()
plt.legend()
# plt.show()

plt.savefig("build/plot3.pdf")