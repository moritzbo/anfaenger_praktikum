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

plt.errorbar(x ,y ,xerr=0.001, yerr=0.0005, markersize=2, elinewidth=0.8, fmt='ro')

x = np.linspace(0, 5)
plt.plot(x, 
        params[0]*x**3 + params[1]*x**2 + params[2]*x + params[3],
        'b--',
        label='Hyster_a',
        linewidth=1.5)

x_coordinates = [0, 5]
y_coordinates = [0, 0]

#plt.plot(x_coordinates, y_coordinates, 'k-', linewidth=1)
#eventuell spiegelachse anzeigen

plt.xlabel(r"$\symup{I_b}$")
h = plt.ylabel(r"$\symup{U_h}$")
h.set_rotation(0)

#plt.show()
