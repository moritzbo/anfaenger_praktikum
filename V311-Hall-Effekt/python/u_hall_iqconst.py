import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import importlib

exec(open('python/u_hall_iqconst_pos.py').read())
exec(open('python/u_hall_iqconst_neg.py').read())



plt.tight_layout()
plt.savefig("build/u_hall_i.pdf") 

#ohne fehler bis jetzt