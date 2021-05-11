import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp
import pandas as pd

n = np.genfromtxt('../data/statitsch.txt', delimiter="/t", encoding = "ISO-8859-1", unpack=True)


print(n)

# plt.plot(n, 
#         a,
#         'k.',
#         label='Messwerte Kuper T1',
#         linewidth=1.5)

