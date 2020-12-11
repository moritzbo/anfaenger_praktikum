import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem


x, y = np.genfromtxt("Daten/daten_magnet_z.txt", unpack = True)

plt.plot(x,y, 'k.', 
            label='scatter')

params, covariance_matrix = np.polyfit(x, y, deg=3, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

x = np.linspace(0, 5)
plt.plot(x, 
        params[0]*x**3 + params[1]*x**2 + params[2]*x + params[3],
        'r--',
        label='Hyster_z',
        linewidth=1.5)

#plt.show()
