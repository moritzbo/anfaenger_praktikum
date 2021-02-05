import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


N0, N0fehler = np.genfromtxt("data/Nohnekorrigiert.txt", unpack="True")

I0 = unp.uarray(N0, N0fehler)


NAl, NAlfehler = np.genfromtxt("data/Nalukorrigiert.txt", unpack="True")

IAl = unp.uarray(NAl, NAlfehler)

print(IAl)


wavelen, wavelen2 = np.genfromtxt("data/wavelength.txt", unpack="True")

wavelen = wavelen * 10**(11)


T = IAl/I0


np.savetxt(
    'data/transmission.txt',
    np.column_stack([unp.nominal_values(T), unp.std_devs(T)]),
    fmt=['%.4f', '%.4f'],       # first column integer, second 4 digits float
    delimiter='   ',
    header='T,Terror',
)

plt.errorbar(wavelen, unp.nominal_values(T), xerr=None, yerr=unp.std_devs(T), fmt="kx",label="Transmission")
plt.xlabel(r'$\lambda \cdot$\SI{e-11}{[\meter]}$')
plt.ylabel(r'$T$')

plt.grid()
plt.tight_layout()


params, covariance_matrix = np.polyfit(wavelen, unp.nominal_values(T), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

#pande0 = ufloat(params[0], errors[0])
#pande1 = ufloat(params[1], errors[1])


for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

x = np.linspace(4.9, 7)

plt.plot(x, params[0]*x + params[1], "b--", label="Lineare Ausgleichsgerade")
plt.legend()
plt.savefig("build/plot2.pdf")