import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem



x = np.linspace(0, 5)
plt.plot(x, 0.5*((-0.000006*x**3 + 0.000112*x**2 + 0.001876*x + 0.000727)+(-0.000047*x**3 + 0.000280*x**x - 0.002408*x + 0.000084)), "r--",
            label="Hallspannung")

#plt.xlabel(r"$\symup{I_b}$")
#h = plt.ylabel(r"$\symup{U_h}$")
#h.set_rotation(0)
# error kp why


plt.legend()
plt.savefig("build/plot1.pdf")
plt.show()