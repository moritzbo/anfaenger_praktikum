import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

x1, I1 = np.genfromtxt("Mr. Data/einfach.dat", unpack=True)
x2, I2 = np.genfromtxt("Mr. Data/einfach2.dat", unpack=True)

xecht=x2*10**(-3)
L=1.27
phi=(xecht-25.03*10**(-3))/L
print(phi)
lambdu = 633 * 10**(-9)
Idunkel = 0.7
IohneD = I2-Idunkel
Iges = IohneD/(340-Idunkel)



def sigmoid(phi, A, b):
    return A**2 * b**2 * (lambdu/(np.pi*b*np.sin(phi)))**2 * np.sin((np.pi*b*np.sin(phi))/(lambdu))**2


params, covariance_matrix = curve_fit(sigmoid, phi, Iges, p0=[1000, 1e-3])

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('Ab', params, uncertainties): 
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

plt.plot(phi,
        Iges,
        "bx",
        label="Messwerte",
        linewidth=1)

# plt.plot(x2,
#         I2,
#         "bx",
#         label="Messwerte",
#         linewidth=1.5)
plt.grid()
plt.legend()
plt.xlabel(r'$\varphi [\si{\radian}]$')
plt.ylabel(r'$\propto Intensität$')

plt.savefig("build/plot1.pdf")
# plt.show()
