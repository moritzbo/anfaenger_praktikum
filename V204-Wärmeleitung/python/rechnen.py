import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


a1, a2, t = np.genfromtxt("../data/rechnen.txt", unpack =True)

a1 = a1 

a2 = a2


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
print(f"{kappamessing:.6f}")




a7, a8, t2 = np.genfromtxt("../data/rechnen2.txt", unpack =True)


meana7 = np.mean(a7)

meana8 = np.mean(a8)

meant2 = np.mean(t2)


mean7err = sem(a7)
mean8err = sem(a8)
meant2err = sem(t2)


t2ufloat = ufloat(meant2, meant2err)
a7ufloat = ufloat(meana7, mean7err)
a8ufloat = ufloat(meana8, mean8err)
print("||||||||")
print("||||||||")
print(meana7)
print(meana8)
print(meant2)
print("||||||||")
print(mean7err)
print(mean8err)
print(meant2err)

kappaedel = dichteedel * cedel * (x)**2 /(2*t2ufloat * unp.log((a7ufloat)/(a8ufloat)))


print(f"{kappaedel:.6f}")


test2 = unp.log((a7ufloat)/(a8ufloat))

print(test2)