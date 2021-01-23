import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


x = [129, 143, 144, 136, 139, 126, 158]

xin15 = [129/20, 143/20, 144/20, 136/20, 139/20, 126/20, 158/20]


xerr = [129**(1/2), 143**(1/2), 144**(1/2), 136**(1/2), 139**(1/2), 126**(1/2), 158**(1/2)]

xerrin15 = [(129/20**(1/2)), (143/20)**(1/2), (144/20)**(1/2), (136/20)**(1/2), (139/20)**(1/2), (126/20)**(1/2), (158/20)**(1/2)]

xin30 = [129/10, 143/10, 144/10, 136/10, 139/10, 126/10, 158/10]

xerrin30 = [(129/10)**(1/2), (143/10)**(1/2), (144/10)**(1/2), (136/10)**(1/2), (139/10)**(1/2), (126/10)**(1/2), (158/10)**(1/2)]

print(f"{xerr}")

#mean = np.mean(x)
#print(mean)
#errmean = sem(x)
#print(errmean)
#mittel = ufloat(mean, errmean)
##print(mittel)
#kackwert = (mittel)**(1/2)
#print(kackwert)
#
#
#
l = unp.uarray(x, xerr)
m = unp.uarray(xin15, xerrin15)
n = unp.uarray(xin30, xerrin30)
print(l)
#
lmean = np.mean(l)
mmean = np.mean(m)
nmean = np.mean(n)
#lmeanerror = sem(l)
#
#lges = ufloat(lmean, lmeanerror)
#print(f'{lges:.4f}')
print(f"{lmean:.3f}")

zwischen = lmean/20
print(zwischen)
print(f"{mmean:.3f}")
print(f"{nmean:.3f}")


lambdawert = ufloat(0.00317, 0.00016)


twert = np.log(2)/lambdawert

twert60 = twert/60

print(f"{twert:.3f}")

print(f"{twert60:.3f}")
