import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

theta, N = np.genfromtxt("data/Emissionsspektrum.txt", unpack=True)


n1 = [291.0,1127.0,1599.0,1533.0,1430.0,1267.0,425.0,241.0]
n1err = [291.0**(1/2),1127.0**(1/2),1599.0**(1/2),1533.0**(1/2),1430.0**(1/2),1267.0**(1/2),425.0**(1/2),241.0**(1/2)]
theta1 = [20.0,
20.1,
20.2,
20.3,
20.4,
20.5,	
20.6,	
20.7	]

n2 = [536.0,4128.0,	5050.0,	4750.0,	4571.0,	4097.0,	901.0,	244.0]
n2err = [536.0**(1/2),4128.0**(1/2),	5050.0**(1/2),	4750.0**(1/2),	4571.0**(1/2),	4097.0**(1/2),	901.0**(1/2),	244.0**(1/2)]
theta2 = [22.3,
22.4,
22.5,
22.6,
22.7,
22.8,
22.9,
23.0	]


Nfehler = np.sqrt(N)

plt.errorbar(theta, N, xerr=None, yerr=Nfehler, fmt="k.", markersize =1.2,label="Bremsstrahlung", elinewidth=0.6)
plt.annotate(r"$K_{\alpha}$",
             xy=(22.5, 5050.0),
             xytext=(20, -1), textcoords='offset points', fontsize=12,arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
plt.annotate(r"$K_{\beta}$",
             xy=(20.2, 1599.0),
             xytext=(20, -1), textcoords='offset points', fontsize=12,arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))


plt.errorbar(theta1, n1, xerr=None, yerr=n1err, fmt="gx",markersize=4, label=r"$K_{\beta}-\text{Linie}$", elinewidth=0.6)
plt.errorbar(theta2, n2, xerr=None, yerr=n2err, fmt="bx",markersize=4, label=r"$K_{\alpha}-\text{Linie}$", elinewidth=0.6)

plt.xlabel(r'$\theta[\textdegree]$')
plt.ylabel(r'$N[\si{{\text{Imp}}\per\second}]$')
plt.grid()
plt.legend(loc=2)
plt.savefig("build/plot2.pdf")