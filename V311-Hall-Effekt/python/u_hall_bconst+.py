import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem



x, y = np.genfromtxt("Daten/daten_hall_bconst_pos.txt", unpack = True)

#plt.plot(x,y, 'bo', markersize=0.05,
#            label='scatter')

params, covariance_matrix = np.polyfit(x, y, deg=3, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

plt.errorbar(x,y,xerr=0.001, yerr=0.0005,fmt="ko", markersize=2, elinewidth=0.8,
        label='Fehler+')

x = np.linspace(0, 5)
plt.plot(x, 
        params[0]*x**3 + params[1]*x**2 + params[2]*x + params[3],
        'b--',
        label='Hallspannung postive polung',
        linewidth=1.5)

for name, value, error in zip('abcde', params, errors):
    print(f'{name} = {value:.6f} ± {error:.4f}')



plt.plot(0.5, 0.001, "yo", markersize=5, Label='Ausreißer')

plt.xlabel(r"$\symup{I_q}$")
h = plt.ylabel(r"$\symup{U_h}$")
h.set_rotation(0)


#plt.show()
 