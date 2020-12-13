import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem


B1 = ufloat(1244.7, 1)
B2 = ufloat(1230.1, 1)

B_mean = (B1 + B2)/2
print(B_mean)