import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem



x, y = np.genfromtxt("../Daten/daten_hall_bconst_neg.txt", unpack = True)

plt.plot(x,y, 'r.', 
            label='scatter')

params, covariance_matrix = np.polyfit(x, y, deg=3, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

#plt.errorbar(x,y, yerr=ERROR aus fehlerfortpflanzung, fmt='o')

x = np.linspace(0, 5)
plt.plot(x, 
        params[0]*x**3 + params[1]*x**2 + params[2]*x + params[3],
        'b--',
        label='Hyster_a',
        linewidth=1.5)


#plt.show()
