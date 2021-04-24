import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

f, U, a, b, phi = np.genfromtxt("data/teilcd.dat", unpack=True)


def sigmoid(f, p):
    return (np.sin(p)/(f*2*np.pi*0.0164))


params, covariance_matrix = curve_fit(sigmoid, f, U/11)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('p', params, uncertainties): 
    print(f'{name} = {value:.4f} ± {uncertainty:.4f}')



#params, covar_matrix = np.polyfit(phi, U/11, deg= 2, cov=True)
# 
#errors = np.sqrt(np.diag(covar_matrix))
#
#for name, value, error in zip('ab', params, errors):
#    print(f'{name} = {value:.3f} ± {error:.3f}')
#x=np.linspace(1.4,2)
#plt.polar(x, 
#        params[0]*x**2 +params[1]*x+params[2],
#        'k--',
#        label='Messwerte',
#        linewidth=1.5)

x = np.linspace(0.0,np.pi)
plt.polar(x, 
        (sigmoid(x,params[0])/11), 
        'k--',
        label='curvefit',
        linewidth=1.5)
plt.polar(phi, 
        U, 
        'bx',
        label='Messwerte',
        linewidth=1.5)
plt.plot()
# plt.polar(phi, 
#         A*11, 
#         'kx',
#         label='messwerte',
#         linewidth=1.5)

# plt.xlabel(r'$f[\si{\hertz}]$')
# plt.ylabel(r'$\phi(f)[\si{\radian}]$')
plt.savefig("build/plot10.pdf")

