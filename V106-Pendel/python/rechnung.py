import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

t1l, t2l , t1k, t2k = np.genfromtxt("../data/gleich.txt", unpack=True)

t1lmean = np.mean(t1l)
t1lerr = sem(t1l)
print("Mittelwert t1 71 cm:")
print(t1lmean)
print("fehler auf Mittelwert t1 71 cm:")
print(t1lerr)

t1lufloat = ufloat(t1lmean, t1lerr)
print("FINAL t1 71 cm:")
print(f"{t1lufloat:.3f}")

#########################################
print("####################")
#########################################

t2lmean = np.mean(t2l)
t2lerr = sem(t2l)
print("Mittelwert t2 71 cm:")
print(t2lmean)
print("fehler auf Mittelwert t2 71 cm:")
print(t2lerr)

t2lufloat = ufloat(t2lmean, t2lerr)
print("FINAL t2 71 cm:")
print(t2lufloat)

#########################################
print("####################")
#########################################

tL = np.concatenate((t1l, t2l))
meantL = np.mean(tL)
meantLerr = sem(tL)
meanTLufloat =ufloat(meantL,meantLerr) 
print("T lang gesamt ( 71 cm)")
print(meanTLufloat)

#########################################
print("####################")
#########################################

t1kmean = np.mean(t1k)
t1kerr = sem(t1k)
print("Mittelwert t1 32 cm:")
print(t1kmean)
print("fehler auf Mittelwert t1 32 cm:")
print(t1kerr)

t1kufloat = ufloat(t1kmean, t1kerr)
print("FINAL t1 32 cm:")
print(t1kufloat)

#########################################
print("####################")
#########################################

t2kmean = np.mean(t2k)
t2kerr = sem(t2k)
print("Mittelwert t2 32 cm:")
print(t2kmean)
print("fehler auf Mittelwert t2 32 cm:")
print(t2kerr)

#########################################
print("####################")
#########################################

tK = np.concatenate((t1k, t2k))
meantK = np.mean(tK)
meantKerr = sem(tK)
meanTKufloat =ufloat(meantK,meantKerr) 
print("T kurz gesamt ( 32 cm)")
print(meanTKufloat)

#########################################
print("####################")
#########################################

t2kufloat = ufloat(t2kmean, t2kerr)
print("FINAL t2 32 cm:")
print(t2kufloat)

#########################################
print("####################")
#########################################

T_L, T_K = np.genfromtxt("../data/gegen.txt", unpack=True)

test1 = (2* np.pi )/meanTLufloat
test2 = (2* np.pi )/meanTKufloat

print(test1)
print(test2)

#########################################
print("####################")
#########################################

T_Lmean = np.mean(T_L)
T_Lerr = sem(T_L)
T_Lgesamt = ufloat(T_Lmean,T_Lerr)
print("T mittelwert für 71 cm:")
print(T_Lgesamt)

#########################################
print("####################")
#########################################

T_Kmean = np.mean(T_K)
T_Kerr = sem(T_K)
T_Kgesamt = ufloat(T_Kmean,T_Kerr)
print("T mittelwert für 32 cm:")
print(T_Kgesamt)

#########################################
print("####################")
#########################################

Tschwebl, Tschwinl, Tschwebk, Tschwink = np.genfromtxt("../data/koppel.txt", unpack=True)

Tschweblmean = np.mean(Tschwebl)
Tschweblerr = sem(Tschwebl)
Tschweblges = ufloat(Tschweblmean, Tschweblerr)
print("T Mittelwert für Schwebung (71 cm):")
print(Tschweblges)

#########################################
print("####################")
#########################################

Tschwinlmean = np.mean(Tschwinl)
Tschwinlerr = sem(Tschwinl)
Tschwinlges  = ufloat(Tschwinlmean, Tschwinlerr)
print("T Mittelwert für (koppel)Sschwingung (71 cm):")
print(Tschwinlges)

#########################################
print("####################")
#########################################

Tschwebkmean = np.mean(Tschwebk)
Tschwebkerr = sem(Tschwebk)
Tschwebkges = ufloat(Tschwebkmean, Tschwebkerr)
print("T Mittelwert für Schwebung (32 cm):")
print(Tschwebkges)

#########################################
print("####################")
#########################################

Tschwinkmean = np.mean(Tschwink)
Tschwinkerr = sem(Tschwink)
Tschwinkges  = ufloat(Tschwinkmean, Tschwinkerr)
print("T Mittelwert für (koppel)Sschwingung (32 cm):")
print(Tschwinkges)
