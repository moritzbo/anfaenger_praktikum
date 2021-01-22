import numpy as np
import matplotlib.pyplot as plt

x_messung, y_messung = np.genfromtxt("python/messungen.txt", unpack=True)
plt.plot(x_messung, y_messung, 'kx', label="Messwerte")
plt.xlim(0, 7)
plt.ylim(0, 5)
plt.xlabel(r'$m \ [\si{\gram}]$')
plt.ylabel(r'$x \ [\si{\centi\meter}]$')
plt.tight_layout()

params, covar_matrix = np.polyfit(x_messung, y_messung, deg= 1, cov=True)

errors = np.sqrt(np.diag(covar_matrix))

x = np.linspace(0, 7)
plt.plot(x, 
        params[0]*x + params[1],
        'b--',
        label='Lineare Regression',
        linewidth=1.5)
plt.grid()

plt.legend(loc="best")

plt.savefig('build/plot2.pdf')

