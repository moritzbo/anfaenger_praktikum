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



a5, a6, t3 = np.genfromtxt("../data/rechnen3.txt", unpack =True)


meana5 = np.mean(a5)

meana6 = np.mean(a6)

meant3 = np.mean(t3)


mean5err = sem(a5)
mean6err = sem(a6)
meant3err = sem(t3)


t3ufloat = ufloat(meant3, meant3err)
a5ufloat = ufloat(meana5, mean5err)
a6ufloat = ufloat(meana6, mean6err)
print("||||||||")
print("||||||||")
print(meana5)
print(meana6)
print(meant3)
print("||||||||")
print(mean5err)
print(mean6err)
print(meant3err)

kappaalu = dichtealu * calu * (x)**2 /(2*t3ufloat * unp.log((a6ufloat)/(a5ufloat)))


print(f"{kappaalu:.6f}")


test3 = unp.log((a6ufloat)/(a5ufloat))

print(test3)







messingkappalit = 113
alukappalit = 220
edelkappalit = 21







##########################################################


print(kappamessing)
print(kappaalu)
print(kappaedel)

messingprozent = 100 * (kappamessing - messingkappalit)/messingkappalit
aluprozent = 100 * (kappaalu - alukappalit)/alukappalit
edelprozent = 100 * (edelkappalit - kappaedel)/edelkappalit


print("TRENNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")

print(F"{messingprozent:.3f}")
print(F"{aluprozent:.3f}")
print(f"{edelprozent:.3f}")





#############################################################


Tneu = 200
omega = 2* np.pi /Tneu

wavelmessing = (kappamessing /(2*dichtemessing*omega * cmessing))**(1/2)

waveledel = (kappaedel /(2*dichteedel *omega * cedel))**(1/2)

wavelalu= (kappaalu /(2*dichtealu*omega * calu))**(1/2)

print("TRENNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
print(wavelmessing)
print(waveledel)
print(wavelalu)