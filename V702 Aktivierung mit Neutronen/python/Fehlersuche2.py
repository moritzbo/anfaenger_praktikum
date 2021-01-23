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

NulleffektE = B
Nulleffekt = sum(NulleffektE)/len(NulleffektE)

print(Nulleffekt)

t,n = np.loadtxt('../daten/Vanadium.txt', skiprows=1, unpack=True)

Nerr = []

for x in n:
    Nerr.append(np.sqrt(x))




N = unp.uarray(n,Nerr) 
Nfinal = N - (Nulleffekt/10)

print(Nfinal)
for x in Nfinal:
    print(f"{x:.5f}") #Faktor 1/10 wegen intervall anpassung

Ntxt = np.transpose(np.array([t,Nfinal]))
np.savetxt("../daten/werte.txt", Ntxt , header="time N zählungen", fmt='%1.20s' )

print(Ntxt)


