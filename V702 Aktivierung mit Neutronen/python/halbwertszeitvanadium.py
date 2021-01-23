import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

t, N = np.genfromtxt("daten/Vanadium.txt", unpack=True)

Nerr = N**(1/2)


Nzsm = unp.uarray(N, Nerr)

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

Nneu = Nzsm - nmean

print(Nneu)

Nneuecht = unp.nominal_values(Nneu)
Nneufehler = unp.std_devs(Nneu)

print(Nneuecht)
print(Nneufehler)

logvalues = unp.log(Nneu)
print(logvalues)
logfehler = unp.std_devs(logvalues)
logecht = unp.nominal_values(logvalues)


plt.errorbar(t, logecht, xerr=None, yerr=logfehler, fmt='kx', markersize=3.5, label='Zählraten Vanadium')
plt.xlabel(r'$t[\si{\second}]$')
plt.ylabel(r'log($N[\text{Imp} / {30}\si{\second}]$)')
plt.grid()



params, covariance_matrix = np.polyfit(t, logecht, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

#pande0 = ufloat(params[0], errors[0])
#pande1 = ufloat(params[1], errors[1])


for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.5f} ± {error:.5f}')

x_plot = np.linspace(0, 1330)

plt.plot(
    x_plot,
    params[0] * x_plot + params[1], "b--",
    label='Lineare Ausgleichsgerade',
    linewidth=1.5)
plt.ylim((0,5.5))
plt.legend(loc="best")
plt.savefig("build/plot1.pdf")
plt.clf()



plt.errorbar(t, Nneuecht, xerr=None, yerr=Nneufehler, fmt='kx', markersize=3.5, label='Zählraten Vanadium')
plt.yscale("log")

plt.xlabel(r'$t[\si{\second}]$')
plt.ylabel(r'$N[\text{Imp} / {30}\si{\second}]$')
plt.grid()


logvalues2 = np.log(Nneuecht)
print(Nneuecht)

params, covariance_matrix = np.polyfit(t, logvalues2, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

#pande0 = ufloat(params[0], errors[0])
#pande1 = ufloat(params[1], errors[1])


for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.5f} ± {error:.5f}')

x_plot = np.linspace(1, 1330)

plt.plot(
    x_plot,
   np.exp(params[0] * x_plot + params[1]), "b--",
    label='Lineare Ausgleichsgerade',
    linewidth=1.5)
plt.yscale("log")
plt.legend(loc="best")
plt.savefig("build/plot2.pdf")



