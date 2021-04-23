import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

U, t, a, b, x= np.genfromtxt("../data/teilcd.dat", unpack=True)

phi =a*2* np.pi/b
phi360 =a*360/b
print(phi)
print(phi360)


a1 = ufloat(12.4, 0,8)
a2 = ufloat(16.4 , 0.4)

b1 = ufloat(37.9, 0.7)

erg = 100* ((a2 - b1)/a2)

print(f'{erg:.4f}')