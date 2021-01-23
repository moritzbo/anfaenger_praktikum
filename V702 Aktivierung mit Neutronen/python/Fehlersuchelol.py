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

print(np.sum(N)/len(N)) #erst poisson dann mittel

B = ufloat(sum(x)/len(x), np.sqrt(sum(x)/len(x))) 

print(B) #erst mittel dann poisson #THIS IS THE WAY

#print(N[1]+N[2])
#print((np.sum(N)/len(N))) #mittel der poission sachen