import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

rpm7, l7, s7, m7 = np.genfromtxt("Data/7aufgabe1.dat", unpack=True)
l10, s10, m10 = np.genfromtxt("Data/10aufgabe1.dat", unpack=True)
l16, s16, m16 = np.genfromtxt("Data/16aufgabe1.dat", unpack=True)

fnull = 2e6

alphaS = np.deg2rad(80.06)
alphaM = np.deg2rad(70.53)
alphaL = np.deg2rad(54.74)

c = 1800

geschs7 = s7*c/(fnull*2*alphaS)
geschm7 = m7*c/(fnull*2*alphaM)
geschl7 = l7*c/(fnull*2*alphaL)

geschs10 = s10*c/(fnull*2*alphaS)
geschm10 = m10*c/(fnull*2*alphaM)
geschl10 = l10*c/(fnull*2*alphaL)

geschs16 = s16*c/(fnull*2*alphaS)
geschm16 = m16*c/(fnull*2*alphaM)
geschl16 = l16*c/(fnull*2*alphaL)

print(geschs7)
print(geschm7)
print(geschl7)

######
print("######")

print(geschs10)
print(geschm10)
print(geschl10)

######
print("######")

print(geschs16)
print(geschm16)
print(geschl16)


plt.plot(geschs7,
        s7/(np.cos(alphaS)),
        "kx",
        label="Rohrdurchmesser 7 mm",
        linewidth=1.5)


plt.plot(geschs10,
        s10/(np.cos(alphaS)),
        "bx",
        label="Rohrdurchmesser 10 mm",
        linewidth=1.5)


plt.plot(geschs16,
        s16/(np.cos(alphaS)),
        "gx",
        label="Rohrdurchmesser 16 mm",
        linewidth=1.5)

plt.ylabel(r'$\frac{\Delta f}{\alpha_{15}}$[$\si{\hertz\per\radian}$]')
plt.xlabel(r'$v $[$\si{\meter\per\second}$]')

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("build/plot1.pdf")
plt.show()

plt.clf()

plt.plot(geschm7,
        m7/(np.cos(alphaM)),
        "kx",
        label="Rohrdurchmesser 7 mm",
        linewidth=1.5)


plt.plot(geschm10,
        m10/(np.cos(alphaM)),
        "bx",
        label="Rohrdurchmesser 10 mm",
        linewidth=1.5)


plt.plot(geschm16,
        m16/(np.cos(alphaM)),
        "gx",
        label="Rohrdurchmesser 16 mm",
        linewidth=1.5)

plt.ylabel(r'$\frac{\Delta f}{\alpha_{15}}$[$\si{\hertz\per\radian}$]')
plt.xlabel(r'$v $[$\si{\meter\per\second}$]')

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("build/plot2.pdf")
plt.show()

plt.clf()

plt.plot(geschl7,
        l7/(np.cos(alphaL)),
        "kx",
        label="Rohrdurchmesser 7 mm",
        linewidth=1.5)


plt.plot(geschl10,
        l10/(np.cos(alphaL)),
        "bx",
        label="Rohrdurchmesser 10 mm",
        linewidth=1.5)


plt.plot(geschl16,
        l16/(np.cos(alphaL)),
        "gx",
        label="Rohrdurchmesser 16 mm",
        linewidth=1.5)
        
plt.ylabel(r'$\frac{\Delta f}{\alpha_{15}}$[$\si{\hertz\per\radian}$]')
plt.xlabel(r'$v $[$\si{\meter\per\second}$]')

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("build/plot3.pdf")
plt.show()
