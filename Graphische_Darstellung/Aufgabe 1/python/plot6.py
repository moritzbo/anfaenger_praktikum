import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

d, N, F = np.genfromtxt("python/messungen4.txt", unpack=True)

def absorptionsgesetz(d, A, μ): 
    return A * np.exp(-μ*d)

params, covariance_matrix = curve_fit(absorptionsgesetz, d, N)
uncertainties = np.sqrt(np.diag(covariance_matrix))

x_plot = np.linspace(0, 5, 50)

plt.plot(d, N, '.', label="Messwerte")
plt.plot(x_plot, absorptionsgesetz(x_plot, *params), "-", label="Curvefit")
plt.yticks(np.arange(0,9100, step=1000))
plt.xlim(0, 5)
plt.xlabel(r"$d$[cm]")
plt.ylabel(r"$N$")
plt.title(r'Angepasstes Absorptionsgesetz durch einen Curvefit', fontsize = 11)
plt.legend(loc="best")

plt.tight_layout()
plt.savefig("build/plot6.pdf")