import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

x2, I2 = np.genfromtxt("Mr. Data/doppel2.dat", unpack=True)

I = I2/2380
lam = 633 * 10**(-9)
L=1.27
x = x2*10**(-3)
phi=(x-24.41*10**(-3))/L

def sigmoid(phi, s, b, A):
    return A*np.cos((np.pi*s*np.sin(phi))/(lam))**2 * ((lam)/(np.pi*b*np.sin(phi)))**2 * np.sin((np.pi*b*np.sin(phi)/(lam)))**2

params, covariance_matrix = curve_fit(sigmoid, phi, I, p0=[0.0005, 0.5e-7, 10])

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('sbA', params, uncertainties): 
    print(f'{name} = {value:.7f} ± {uncertainty:.7f}')

p = np.linspace(-0.020,0.02,100000)
plt.plot(p,
        sigmoid(p, *params),
        "k-",
        label="Ausgleichsfunktion Doppelspalt",
        linewidth=1.5)

plt.plot(phi,
        I,
        "kx",
        label="Messwerte Doppelspalt",
        linewidth=1.5)


x2, I2 = np.genfromtxt("Mr. Data/einfach2.dat", unpack=True)

I=I2/340
x=x2*10**(-3)
L=1.27
phi=(x-25.03*10**(-3))/L
lam = 633 * 10**(-9)






def sigmoid(phi, A, b):
    return A**2 * b**2 * (lam/(np.pi*b*np.sin(phi)))**2 * np.sin((np.pi*b*np.sin(phi))/(lam))**2


params, covariance_matrix = curve_fit(sigmoid, phi, I, p0=[1000, 1e-3])

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('Ab', params, uncertainties): 
    print(f'{name} = {value:.7f} ± {uncertainty:.7f}')

xachsep = np.linspace(-0.020,0.02,10000)
plt.plot(xachsep,
        sigmoid(xachsep, params[0], params[1]),
        "b-",
        label="Ausgleichsfunktion Einfachspalt",
        linewidth=1.5)

# xachsen = np.linspace(,-0.0001)
# plt.plot(xachsen,
#         sigmoid(xachsen, params[0], params[1]),
#         "k--",
#         linewidth=1.5)

plt.plot(phi,
        I,
        "bx",
        label="Messwerte Einfachspalt",
        linewidth=1)


plt.grid()
plt.xlabel(r'$\phi$[$\si{\radian}$]')
plt.legend(loc="upper right", prop={'size': 6})


plt.savefig("build/plot3.pdf")
