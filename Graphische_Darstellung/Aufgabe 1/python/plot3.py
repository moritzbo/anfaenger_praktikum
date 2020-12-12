import numpy as np
import matplotlib.pyplot as plt

x_wert, y_wert = np.genfromtxt("python/messungen3.txt", unpack=True)
x_wert = [1/60, 1/80, 1/100, 1/110, 1/120, 1/125]
y_wert = [1/285, 1/142, 1/117, 1/85, 1/86, 1/82]

plt.plot(x_wert, y_wert, 'k.', label="Messwerte")
plt.xlabel(r"$\symup{G}$")
plt.ylabel(r"$\symup{B}$")
plt.xlim(0, 0.02)
plt.ylim(0, 0.021)

params, covar_matrix = np.polyfit(x_wert, y_wert, deg= 1, cov=True)

errors = np.sqrt(np.diag(covar_matrix))
# B = aG + b
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')
x = np.linspace(0, 0.02)
plt.plot(x, 
        params[0]*x + params[1],
        'b--',
        label='Lineare Regression',
        linewidth=1.5)

plt.legend(loc="best")

plt.tight_layout()
plt.savefig('build/plot3.pdf')