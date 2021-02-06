

import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp









tw = ufloat(218.66, 11.04)

print(f"{2*tw:.3f}")