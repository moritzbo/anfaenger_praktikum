import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

f, U = np.genfromtxt("../daten/hz.dat", unpack=True)

f = f *2*np.pi

o1 = (f/(1/(294.75 * 10**(-9) * 1000)))


def sigmoid(o1):
    return np.sqrt(1/9 * ((o1**2 - 1)**2)/((1 - o1**2)**2 + 9 * o1**2))
a = (np.sqrt(1/9 * ((o1**2 - 1)**2)/((1 - o1**2)**2 + 9 * o1**2)))

# params, covariance_matrix = curve_fit(sigmoid, omega, U)

# uncertainties = np.sqrt(np.diag(covariance_matrix))

# for name, value, uncertainty in zip('w', params, uncertainties): 
#     print(f'{name} = {value:.4f} ± {uncertainty:.4f}')

x = np.linspace(0,15)
plt.plot(x,
        a,
        "r--",
        label="Theoretische Kurve",
        linewidth=1.5)

plt.plot(o1, 
        U,
        'kx',
        label='Messwerte',
        linewidth=1.5)
plt.xscale("log")


plt.show()