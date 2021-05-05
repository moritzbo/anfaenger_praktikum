import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

x1, I1 = np.genfromtxt("../Mr. Data/doppel.dat", unpack=True)
#x1, I1 verworfen weil trash
x2, I2 = np.genfromtxt("../Mr. Data/doppel2.dat", unpack=True)

Ineu = I2*10**(-9)
x2 = x2*10**(-3)
L  = 1.27
lam  = lam = 633 * 10**(-9)
phi  = (x2-(24.44*10**(-3)))/L

def sigmoid(phi, s, b):
    return 4*((np.cos(np.pi*s*np.sin(phi)/lam)**2*((lam)/(np.pi*b*np.sin(phi)))**2*(np.sin(np.pi*b*np.sin(phi)/(lam))))**2)

params, covariance_matrix = curve_fit(sigmoid, phi, Ineu, p0=[0.5,0.00008])

uncertainties = np.sqrt(np.diag(covariance_matrix))
#b=0.5e-3
for name, value, uncertainty in zip('sb', params, uncertainties): 
    print(f'{name} = {value:.7f} ± {uncertainty:.7f}')

xachsep = np.linspace(-1.92402643e-02,2.01216031e-02)
plt.plot(xachsep,
        sigmoid(xachsep, params[0], params[1]),
        "k-",
        label="Ausgleichsfunktion",
        linewidth=1.5)
# plt.plot(
#         phi,
#         Ineu,
#         "bx",
#         linewidth=1.5
#                         )

plt.show()