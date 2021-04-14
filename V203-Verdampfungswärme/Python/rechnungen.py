import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

R = const.physical_constants["molar gas constant"][0]

a = ufloat(-4710.774, 43.656)

L = -R * a  
print(f"{L:.3f}")