import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

f, U, a, b = np.genfromtxt("data/teilcd.dat", unpack=True)

U_0 = 11

#f = f*2 *np.pi

A = U/U_0

print(A)

def sigmoid(f, a):
    return 1/((1+(f * a)**2)**(1/2))


params, covariance_matrix = curve_fit(sigmoid, f, A)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('a', params, uncertainties): 
    print(f'{name} = {value:.4f} ± {uncertainty:.4f}')


plt.plot(f, 
        A, 
        'kx',
        label='Messwerte',
        linewidth=1.5)
#plt.plot(f, 
#        sigmoid(f, params[0]), 
#        'kx',
#        label='Theoretischer Wert',
#        linewidth=1.5)
x = np.linspace(10, 10000)
plt.plot(x, 
        sigmoid(x, params[0]), 
        'b--',
        label='Nichtlinearer Fit',
        linewidth=1.5)
plt.grid()
plt.legend(loc="best")
#plt.tight_layout()
#plt.xscale("log")
plt.xlabel(r'$f[\si{\hertz}]$')
plt.ylabel(r'$A(f)$/$U_{0}$')
plt.savefig("build/plot4.pdf")
plt.clf()

plt.plot(f, 
        A, 
        'kx',
        label='Messwerte',
        linewidth=1.5)
plt.plot(x, 
        sigmoid(x, params[0]), 
        'b--',
        label='Nichtlinearer Fit',
        linewidth=1.5)
plt.grid()
plt.legend(loc="best")
#plt.tight_layout()
plt.xscale("log")
plt.xlabel(r'$f[\si{\hertz}]$')
plt.ylabel(r'$A(f)$/$U_{0}$')
plt.savefig("build/plot5.pdf")