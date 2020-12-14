import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem



x = np.linspace(0, 5)
plt.plot(x, 0.5*((-0.000146 *x**3 + 0.001047 * x**2 - 0.000053 *x - 0.000740)-( -0.000044 *x**3+ 0.000415 *x**2 - 0.003241 * x + 0.000137)), "r--",
            label="Hallspannung")

plt.xlabel("$I_q[A]$")
h = plt.ylabel("$U_h[V]$ ")
h.set_rotation(0)

plt.tight_layout()
plt.legend()
plt.savefig("build/plot2.pdf")
plt.show()