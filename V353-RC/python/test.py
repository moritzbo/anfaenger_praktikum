import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

U, t, a, b = np.genfromtxt("../data/teilcd.dat", unpack=True)

phi =a*2* np.pi/b
phi360 =a*360/b
print(phi)
print(phi360)