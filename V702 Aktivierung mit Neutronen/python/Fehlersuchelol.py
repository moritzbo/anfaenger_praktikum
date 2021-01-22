import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

x = [129, 143, 144, 136, 139, 126, 158]
error = []

for n in x:
    error.append(np.sqrt(n))

N = unp.uarray(x,error)

#print(N) #poisson vertielter fehler 
#print(N[1]+N[2])
print((np.sum(N)/len(N))/20) #mittel der poission sachen