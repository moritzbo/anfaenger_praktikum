import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem



x, y = np.genfromtxt("Daten/daten_hall_Iqconst_neg.txt", unpack = True)

#plt.plot(x,y, 'r.', 
#            label='scatter')

params, covariance_matrix = np.polyfit(x, y, deg=3, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))



p = np.linspace(0, 5) #sonst x aber variablen konflikt
plt.plot(p, 
        params[0]*p**3 + params[1]*p**2 + params[2]*p + params[3],
        'c--',
        label='Hallspannung negative Polung',
        linewidth=1.5)

plt.errorbar(x ,y ,xerr=0.001, yerr=0.0005, markersize=2, elinewidth=0.8, fmt='ro',
                label='Fehler Hallspannung -')

#x_coordinates = [0, 5]
#y_coordinates = [0, 0]

#plt.plot(x_coordinates, y_coordinates, 'k-', linewidth=1)
#eventuell spiegelachse anzeigen

plt.xlabel(r"$\symup{I_b}$")
h = plt.ylabel(r"$\symup{U_h}$")
h.set_rotation(0)

plt.legend(fontsize=8, loc=3)


#plt.show()
