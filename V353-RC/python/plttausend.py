import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

f, U, a, b, phi = np.genfromtxt("../data/teilcd.dat", unpack=True)



print(phi)

def sigmoid(f, tau):
    return np.arctan(-f*tau)


params, covariance_matrix = curve_fit(sigmoid, f, phi)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('t', params, uncertainties): 
    print(f'{name} = {value:.4f} ± {uncertainty:.4f}')


x = np.linspace(10, 10000)

plt.plot(f, 
        phi, 
        'kx',
        label='messwerte',
        linewidth=1.5)

plt.plot(x, 
        sigmoid(x, params[0]), 
        'b--',
        label='Nichtlinearer Fit',
        linewidth=1.5)
plt.legend()        
plt.show()

t=params[0]
print(t)