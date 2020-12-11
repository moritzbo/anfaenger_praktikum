import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import importlib

exec(open('python/u_hall_bconst+.py').read())
exec(open('python/u_hall_bconst-.py').read())




plt.savefig("build/u_hall.pdf") 

#ohne fehler bis jetzt