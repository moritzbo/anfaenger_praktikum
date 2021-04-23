import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

f, U, a, b, phi = np.genfromtxt("../data/teilcd.dat", unpack=True)

A = - np.sin(phi)/(f*-0.037)*11

plt.polar(A, 
        phi, 
        'kx',
        label='messwerte',
        linewidth=1.5)

plt.show()