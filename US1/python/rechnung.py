import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp


LochO, tO, U_eO, U_rO, sO  = np.genfromtxt("data/oben.dat", unpack=True)
LochU, tU, U_eU, U_rU, sU  = np.genfromtxt("data/unten.dat", unpack=True)

#plt.plot(tO, sO, "kx", label="Messdaten", linewidth=1.5)
#plt.plot(tU, sU, "bx", label="Messdaten", linewidth=1.5)

x = np.linspace(0, 50)

tgesamt = tO
sgesamt = sO

for i in range(len(LochU)):
    tgesamt = np.append(tgesamt, tU[i])

for j in range(len(LochU)):
    sgesamt = np.append(sgesamt, sU[j])

print(tgesamt)
print(sgesamt)
plt.plot(tgesamt, 2*sgesamt, "kx", label="Messdaten", linewidth=1.5)

params, covariance_matrix = np.polyfit(tgesamt, 2*sgesamt, deg=1, cov=True)

uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:.6} ± {uncertainty:.6}')

plt.plot(x, params[0]*x + params[1], "b-",label="Lineare Regression", linewidth= 1.5)

plt.xlabel(r"$\increment t$ [$\si{\micro\second}$]")
plt.ylabel(r"$2 \cdot s$ [$\si{\milli\meter}$]")
plt.legend()
plt.grid()


plt.savefig("build/plot1.pdf")


c = ufloat(2814.79, 54.41)

tO = tO * 10**(-3)
tU = tU * 10**(-3)

s_ermitteltO = (c * tO)/2

s_ermitteltO1 = unp.nominal_values(s_ermitteltO)
s_ermitteltO2 = unp.std_devs(s_ermitteltO)

s_ermitteltU = (c * tU)/2

print(s_ermitteltO1)
print(s_ermitteltO2)

s_ermitteltU1 = unp.nominal_values(s_ermitteltU)
s_ermitteltU2 = unp.std_devs(s_ermitteltU)


print(s_ermitteltU1)
print(s_ermitteltU2)

 
sobenprozent = 100 * (np.absolute(sO - s_ermitteltO ))/(sO)
suntenprozent = 100 * (np.absolute(sU - s_ermitteltU ))/(sU)

print(sobenprozent)

print(suntenprozent)


g, t2, t2err  = np.genfromtxt("data/yo.dat", unpack=True)
t2 = t2 * 10**(-6)
t2err = t2err * 10**(-6)

t2arr = unp.uarray(t2, t2err)

cl = 2500
cgk = 1410

s1 = (t2arr[0]* cgk)/2

s2 = ((t2arr[1]-t2arr[0]) * cgk )/(2)

s3 = ((t2arr[2]-t2arr[1]) * cl )/(2)

s4 = ((t2arr[3]-t2arr[2]) * cgk )/(2)

s1 = s1 * 10**(3)
s2 = s2 * 10**(3)
s3 = s3 * 10**(3)
s4 = s4 * 10**(3)

print(f"Sonde-Iris: {s1}")
print(f"Iris-Linse: {s2}")
print(f"Linse-Linse: {s3}")
print(f"Linse-Retina: {s4}")


prozc = 100 * (np.absolute(c - 2730))/(2730)

print(f"{prozc:.2f}")


