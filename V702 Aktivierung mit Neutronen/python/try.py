import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

t, N = np.genfromtxt("../daten/Rhodium.dat", unpack=True)

Nerr = N**(1/2)


Nzsm = unp.uarray(N, Nerr)

x = [129, 143, 144, 136, 139, 126, 158]

xin15 = [129/20, 143/20, 144/20, 136/20, 139/20, 126/20, 158/20]

xerr = [129**(1/2), 143**(1/2), 144**(1/2), 136**(1/2), 139**(1/2), 126**(1/2), 158**(1/2)]

xerrin15 = [(129/20**(1/2)), (143/20)**(1/2), (144/20)**(1/2), (136/20)**(1/2), (139/20)**(1/2), (126/20)**(1/2), (158/20)**(1/2)]


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
#
lmean = np.mean(l)
mmean = np.mean(m)
#lmeanerror = sem(l)
#
#lges = ufloat(lmean, lmeanerror)
#print(f'{lges:.4f}')
print(f"{lmean:.3f}")

zwischen = lmean/20
print(zwischen)
print(f"{mmean:.3f}")
#print(f"{nmean:.3f}")

Nneu = Nzsm - mmean
#Mneu = Nzsm - mmean

print(Nneu)

Nneuecht = unp.nominal_values(Nneu)
Nneufehler = unp.std_devs(Nneu)

print(Nneuecht)
print(Nneufehler)

logvalues = unp.log(Nneu)
print(logvalues)
logfehler = unp.std_devs(logvalues)
logecht = unp.nominal_values(logvalues)


plt.errorbar(t, logecht, xerr=None, yerr=logfehler, fmt='kx', markersize=3.5, label='Zählraten Rhodium')
#plt.xlabel(r'$t[\si{\second}]$')
#plt.ylabel(r'log($N[\text{Imp} / {30}\si{\second}]$)')
plt.grid()

tstar =[]
logechtstar = []

for o in range(23):
    tstar.append(t[o+21])
print(tstar)


for h in range(23):
    logechtstar.append(logecht[h+21])
print(logechtstar)


params, covariance_matrix = np.polyfit(tstar, logechtstar, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

#pande0 = ufloat(params[0], errors[0])
#pande1 = ufloat(params[1], errors[1])


for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.5f} ± {error:.5f}')

x_plot = np.linspace(330, 660)

#plt.plot(
#    x_plot,
#    params[0] * x_plot + params[1], "b--",
#    label='Lineare Ausgleichsgerade für den langen Zerfall',
#    linewidth=1.5)
#plt.legend(loc="best")
##plt.errorbar(t, Nneuecht, xerr=None, yerr=Nneufehler, fmt='kx', markersize=3.5, label='Zählraten Rhodium')
###plt.yscale("log")
##
##plt.xlabel(r'$t[\si{\second}]$')
##plt.ylabel(r'$N[\text{Imp} / {15}\si{\second}]$')
#plt.tight_layout()
#



#logvalues2 = np.log(Nneuecht)
#print(Nneuecht)
#
#params, covariance_matrix = np.polyfit(t, logvalues2, deg=1, cov=True)
#
#errors = np.sqrt(np.diag(covariance_matrix))
#
##pande0 = ufloat(params[0], errors[0])
##pande1 = ufloat(params[1], errors[1])
#
#
#for name, value, error in zip('ab', params, errors):
#    print(f'{name} = {value:.5f} ± {error:.5f}')
#
#x_plot = np.linspace(1, 660)

#plt.plot(
#    x_plot,
#   np.exp(params[0] * x_plot + params[1]), "b--",
#    label='Lineare Ausgleichsgerade',
#    linewidth=1.5)
#plt.yscale("log")
#plt.legend(loc="best")
#plt.show()



lambda2 = ufloat(0.00321, 0.00062)

t2 = np.log(2)/ (lambda2*60) 

print(f"{t2:.3f}")


print(Nneu)


Nneu2 = []

for g in range(13):
    Nneu2.append(Nneu[g])

tneu = []

for j in range(13):
    tneu.append(t[j])

print(Nneu2)
print(tneu)

Nklein =[]

for z in range(13):
    Nklein.append(Nneu2[z] - np.exp(params[0] * tneu[z] + params[1])) 

print(Nklein)

#plt.plot(
#    x_plot,
#    params[0] * x_plot + params[1], "g--",
#    label='Lineare Ausgleichsgerade für den kurzen Zerfall',
#    linewidth=1.5)
#plt.legend(loc="best")
##plt.errorbar(t, Nneuecht, xerr=None, yerr=Nneufehler, fmt='kx', markersize=3.5, label='Zählraten Rhodium')
###plt.yscale("log")
##
##plt.xlabel(r'$t[\si{\second}]$')
##plt.ylabel(r'$N[\text{Imp} / {15}\si{\second}]$')
#plt.tight_layout()

log2 = unp.log(Nklein)
logecht2 = unp.nominal_values(log2)

print(log2)

params2, covariance_matrix2 = np.polyfit(tneu, logecht2, deg=1, cov=True)

errors2 = np.sqrt(np.diag(covariance_matrix))

#pande0 = ufloat(params[0], errors[0])
#pande1 = ufloat(params[1], errors[1])


for name2, value2, error2 in zip('ab', params2, errors2):
    print(f'{name2} = {value2:.5f} ± {error2:.5f}')


lambda3 = ufloat(0.01765, 0.00062)

t3 = np.log(2)/ (lambda3) 

print(f"{t3:.3f}")


