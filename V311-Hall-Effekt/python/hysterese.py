import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import importlib

exec(open('hysterese_a_poly.py').read())
exec(open('hysterese_z_poly.py').read())


#plt.show()
plt.safefig("../build/hystere.pdf")
#ohne fehler bis jetzt