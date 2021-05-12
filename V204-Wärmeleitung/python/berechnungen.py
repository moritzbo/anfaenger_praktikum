import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


n, a, b, c, d, e, f, g, h = np.genfromtxt("../data/statisch.dat", unpack =True)

ntry = n[700]

x = g[3500] - h[3500] 


Kappalit_messing = 113

Kappalit_alu = 220

Kappalit_edel = 21

Aschmal = 28e-6
Abreit = 48e-6

delta_x = 0.03

print(f"{x:2f}")


def func(x):
   return - Kappalit_edel * Abreit * x/delta_x

print(f"{func(x):.2f}")