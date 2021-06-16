import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

I, U = np.genfromtxt("data/grün.dat", unpack=True)


lolI   = []
lolU   = []
for i in range(15):
   print(I[i+5])
   lolI = np.append(lolI, I[i+5]) 
for i in range(15):
   print(U[i+5])
   lolU = np.append(lolU, U[i+5]) 
sqrtI = np.sqrt(lolI)
# # print(I)
# # print(lolI)
# sqrtI = np.sqrt(lolI)
# # print(sqrtI)
# print(sqrtI.size)


plt.plot(lolU, 
        sqrtI,
        'bx',
        label='Messwerte',
        linewidth=1.5)

plt.ylabel("I ")
plt.xlabel("U [Volt]")


# plt.xlabel(r'$$')
# plt.ylabel(r'$$')

plt.xlim(-1.1,1)
plt.ylim(-0.1,2)

def sigmoid(x, a, b):
    return a*x+b


params, covariance_matrix = curve_fit(sigmoid, lolU, sqrtI)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:.4f} ± {uncertainty:.4f}')


x = np.linspace(-2,5)
plt.plot(x, 
        params[0]*x + params[1],
        'k--',
        label='Lineare Ausgleichsgerade',
        linewidth=1.5)

plt.axhline(y=0, color='g', linestyle='--', linewidth=1.5, label="Nullgerade")

plt.grid()
plt.legend()
# plt.show()

plt.savefig("build/plot2.pdf")