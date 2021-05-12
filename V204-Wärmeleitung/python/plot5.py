import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


n, a, b, c, d, e, f, g, h = np.genfromtxt("../data/dynamisch2.txt", unpack =True)


plt.plot(n/5, (g-h), 'b-', label="T7 - T8", markersize=1)
plt.plot(n/5, (b-a), 'k-', label="T2 - T1", markersize=1)

plt.show()