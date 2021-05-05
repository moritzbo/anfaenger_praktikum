import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

x1, I1 = np.genfromtxt("../Mr. Data/doppel.dat", unpack=True)
x, I = np.genfromtxt("../Mr. Data/doppel2.dat", unpack=True)

print(x)
print(I)

zeta = 24.41e-3

L = 1.27
x = x*(10**(-3)) 

phi = (x - zeta)/L

I = I*(10**(-9))

l = 663e-9

print(I)

plt.plot(phi, I , "kx", label="Messwerte")




def sigmoid(phi, b, s, A):
    return A* ((np.cos(np.pi*s*np.sin(phi)/l))**2*(l/(np.pi*b*np.sin(phi)))**2*(np.sin(np.pi*b*np.sin(phi)/l))**2)

params, covariance_matrix = curve_fit(sigmoid, phi, I, p0=(0.00000005, 0.000005, 6000))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('bsA', params, uncertainties): 
    print(f'{name} = {value:.6f} ± {uncertainty:.6f}')

x_plot = np.linspace(-0.020, 0.020)

plt.plot(x_plot, sigmoid(x_plot, *params), "-", label='Sigmoid Fit')
plt.show()

#p0=(0.0005, 0.005, 60000)