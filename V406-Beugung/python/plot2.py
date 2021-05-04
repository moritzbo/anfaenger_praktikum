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

Idunkel = 0.7
I2ohneD = I2-Idunkel
Iges = I2ohneD/(1950-Idunkel)
lam = 633 * 10**(-9)
xecht=x2*10**(-3)
L=1.27
phi=(xecht-24.41*10**(-3))/L
print(phi)
def sigmoid(phi, s, b):
    return 4*np.cos((np.pi*s*np.sin(phi))/(lam))**2 * ((lam)/(np.pi*b*np.sin(phi)))**2 * np.sin((np.pi*b*np.sin(phi)/(lam)))**2


params, covariance_matrix = curve_fit(sigmoid, phi, Iges)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('sb', params, uncertainties): 
    print(f'{name} = {value:.7f} ± {uncertainty:.7f}')

xachsep = np.linspace(0.0001,0.02)
plt.plot(xachsep,
        sigmoid(xachsep, params[0], params[1]),
        "k--",
        label="Ausgleichsfunktion",
        linewidth=1.5)

xachsen = np.linspace(-0.020,-0.0001)
plt.plot(xachsen,
        sigmoid(xachsen, params[0], params[1]),
        "k--",
        linewidth=1.5)

# plt.plot(phi,
#         Iges,
#         "bx",
#         label="Messwerte",
#         linewidth=1)

plt.show()