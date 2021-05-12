import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


a1, a2, t = np.genfromtxt("../data/rechnen.txt", unpack =True)



meana1 = np.mean(a1)

meana2 = np.mean(a2)

meant = np.mean(t)


mean1err = sem(a1)
mean2err = sem(a2)
meanterr = sem(t)

#mean2err
#
#meanterr

tufloat = ufloat(meant, meanterr)
a1ufloat = ufloat(meana1, mean1err)
a2ufloat = ufloat(meana2, mean2err)


print(meana1)
print(meana2)
print(meant)
print("||||||||")
print(mean1err)
print(mean2err)
print(meanterr)

dichtemessing = 8520
dichtealu = 2800
dichteedel =8000

cmessing = 385
calu = 830
cedel = 400

x = 0.03

kappamessing = dichtemessing * cmessing* (x)**2 /(2*tufloat * unp.log((a2ufloat)/(a1ufloat)))


test = unp.log((a2ufloat)/(a1ufloat))

print(test)
print(f"{kappamessing:4f}")


