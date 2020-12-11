import numpy as np
import matplotlib.pyplot as plt

x_messung, y_messung = np.genfromtxt("python/messungen.txt", unpack=True)
plt.plot(x_messung, y_messung, 'k.')
plt.xlim(0, 7)
plt.ylim(0, 5)
plt.xlabel(r'$m \ [\si{\gram}]$')
plt.ylabel(r'$x \ [\si{\centi\meter}]$')
plt.tight_layout()
plt.savefig('build/plot1.pdf')

 