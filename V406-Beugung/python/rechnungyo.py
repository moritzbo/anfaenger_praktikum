import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp



b = ufloat(0.074e-3, 0.001e-3)

blit = 0.075e-3

bpro = 100* (blit - b)/blit

print(f"{bpro:.4f}")