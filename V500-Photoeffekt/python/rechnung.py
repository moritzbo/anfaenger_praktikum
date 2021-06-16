import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

#gelb#gelb#gelb#gelb#gelb
a = ufloat(-0.6043, 0.0390)
b = ufloat(0.2417, 0.0231)
x = -b/a
print(f"Schnittpunkt gelb = {x:.4f}")

#grün#grün#grün#grün#grün
a = ufloat(-0.8503 , 0.0457)
b = ufloat(0.6500 , 0.0240)
x = -b/a
print(f"Schnittpunkt grün = {x:.4f}")

#violet1#violet1#violet1#violet1
a = ufloat(-0.6267 , 0.0178)
b = ufloat(0.7332 , 0.0096)
x = -b/a
print(f"Schnittpunkt grün = {x:.4f}")

#violet2#violet2#violet2#violet2
a = ufloat(-0.5892 , 0.0331)
b = ufloat(0.2042 , 0.0196)
x = -b/a
print(f"Schnittpunkt grün = {x:.4f}")



a = ufloat(4.0132,1.3517)
heprozent =  100*(44173801/10681177560000000000000 - a*10**(-15))/(44173801/10681177560000000000000)
print(f"{heprozent:.4f}")