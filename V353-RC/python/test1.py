import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

f, U, phi = np.genfromtxt("../data/art.dat", unpack=True)

phi_rad=np.deg2rad(phi)

U = - (np.sin(phi)/(f*np.pi*2*-0.0014))*3

plt.polar(phi_rad, 
        U, 
        'kx',
        label='messwerte',
        linewidth=1.5)
# plt.polar(phi, 
#         U, 
#         'bx',
#         label='messwerte',
#         linewidth=1.5)


plt.show()