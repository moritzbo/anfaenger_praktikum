import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


tvangem = ufloat(3.64, 0.16) *60
tvanlit = ufloat(3.743, 0.005) *60

abwtvan = 100 - 100* (tvangem/tvanlit)


rh1gem = ufloat(39.27, 1.38) 
rh1lit = ufloat(42.3, 0.4)

abwrh1 = 100 - 100* (rh1gem/rh1lit)

print(f"{abwtvan:.2f}")


print(tvangem)
print(tvanlit)

print(f"{abwrh1:.2f}")

rh2gem = ufloat(3.60, 0.70) *60
rh2lit = ufloat(4.34, 0.03) *60

abwrh2 = 100 - 100* (rh2gem/rh2lit)

print(f"{abwrh2:.2f}")