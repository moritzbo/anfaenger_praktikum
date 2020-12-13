import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem



x, y = np.genfromtxt("Daten/daten_hall_bconst_neg.txt", unpack = True)

#plt.plot(x,y, 'r.', 
#            label='scatter')

params, covariance_matrix = np.polyfit(x, y, deg=3, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

plt.errorbar(x ,y ,xerr=0.001, yerr=0.0005, markersize=2, elinewidth=0.8, fmt='ro',
        label='Fehler -')

x = np.linspace(0, 5)
plt.plot(x, 
        params[0]*x**3 + params[1]*x**2 + params[2]*x + params[3],
        'c--',
        label='Hallspannung negative Polung',
        linewidth=1.5)

x_coordinates = [0, 5]
y_coordinates = [0, 0]


for name, value, error in zip('abcde', params, errors):
    print(f'{name} = {value:.6f} ± {error:.4f}')

#plt.plot(x_coordinates, y_coordinates, 'k-', linewidth=1)
#eventuell spiegelachse anzeigen

plt.xlabel(r"$\symup{I_q}$")
h = plt.ylabel(r"$\symup{U_h}$")
h.set_rotation(0)

plt.legend(fontsize=7, loc=3)

#plt.show()
