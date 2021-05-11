import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


n, a, b, c, d, e, f, g, h = np.genfromtxt("../data/statisch.dat", unpack =True)

plt.plot(n/5, a, 'b.', markersize=1)

plt.show()