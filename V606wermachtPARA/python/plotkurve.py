import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

f, U= np.genfromtxt("daten/kurve.txt", unpack=True)


U = U/10

def gauss(x, sigma, alpha, beta):
    return beta/(np.sqrt(2 * np.pi *sigma**(2))) * np.exp(-(x-alpha)**2 / (2* sigma**2))

plt.plot(f,
        U,
        "bx",
        label="Spannungsmesswerte",
        linewidth=1.5)

plt.xlabel(r"$f$ / $\si{\kilo\hertz}$")
plt.ylabel(r"$U_{\text{A}}$ / $\si{\volt}$")

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("build/kurve1.pdf")

plt.clf()

x = np.linspace(13, 36, 2000)
plt.plot(f,
        U,
        "bx",
        label="Spannungsmesswerte",
        linewidth=1.5)
plt.axhline(y=1/2**(1/2), color='k', label=r"$U = (1$/$\sqrt{2}) U_{\text{A}}$", linestyle='--')

plt.xlabel(r"$f$ / $\si{\kilo\hertz}$")
plt.ylabel(r"$U_{\text{A}}$/$U_{\text{E}}$")

params, covariance_matrix = curve_fit(gauss, f, U,  p0=(1, 21.6, 1))

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('σαβ', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

plt.plot(x, gauss(x, *params), "-", label="Gaußfitfunktion" )


plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("build/kurve2.pdf")


############################################################################################
y = 1/2**(1/2)

idx = np.argwhere(np.diff(np.sign(gauss(x, *params) - y))).flatten()

print(x[idx])

arr1 = x[idx]

numinus = ufloat(arr1[0], 0.05)
nuplus = ufloat(arr1[1], 0.05)

nunull = 21.6

Q = nunull/(nuplus - numinus)

print(f"{Q:.4}")