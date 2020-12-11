import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

A_messung, mT_messung = np.genfromtxt("Daten/daten_magnet_z.txt", unpack = True)
plt.plot(A_messung, mt_messung)
