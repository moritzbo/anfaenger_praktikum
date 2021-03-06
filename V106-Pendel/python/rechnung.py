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
print("T- mittelwert für 71 cm:")
print(T_Lgesamt)

#########################################
print("####################")
#########################################

T_Kmean = np.mean(T_K)
T_Kerr = sem(T_K)
T_Kgesamt = ufloat(T_Kmean,T_Kerr)
print("T- mittelwert für 32 cm:")
print(T_Kgesamt)

#########################################
print("####################")
#########################################

test3 = (2* np.pi )/T_Lgesamt
test4 = (2* np.pi )/T_Kgesamt
 
print(test3)
print(test4)

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


#########################################
print("####################")
#########################################

omegaS71 = (2* np.pi )/Tschweblges
omegaS32 = (2* np.pi )/Tschwebkges
omegaSchwin71 = (2* np.pi )/Tschwinlges
omegaSchwin32 = (2* np.pi )/Tschwinlges

print(omegaS71)
print(omegaS32)
print(omegaSchwin71)
print(omegaSchwin32)
#########################################
print("####################")
#########################################



Kl = (test3**2 - test1**2)/(test3**2 + test1**2)
Kk = (test4**2 - test2**2)/(test4**2 + test2**2)

print(Kl)
print(Kk)

x=const.physical_constants["standard acceleration of gravity"]

omegaminusL = unp.sqrt(x[0]/0.71+(2*Kl)/0.71)
omegaminusK = unp.sqrt(x[0]/0.32+(2*Kk)/0.32)

print(omegaminusL)
print(omegaminusK)







omegasL = test1 - test3
# omegasK = test2 - test4

print(omegasL)
# print(omegasK)

TschwebungRechnung71 =  (T_Lgesamt*meanTLufloat)/(T_Lgesamt-meanTLufloat)
print("Schwebung Ts für 71cm (errechnet)")
print(f"{TschwebungRechnung71:.5}")

print("#############")


omegasK = test2 - test4
print(omegasK)
print("Schwebung Ts für 32cm (errechnet)")
TschwebungRechnung32 = (T_Kgesamt*meanTKufloat)/(T_Kgesamt-meanTKufloat)
print(f"{TschwebungRechnung32:.5}")


wplus71 = test1
wplus32 = test2
wpluseigen71 = 3.716
wpluseigen32 = 5.536

wminus71 = test3
wminus32 = test4
wminuseigen71 = omegaminusL
wminuseigen32 = omegaminusK

wschwebung71 = np.abs(omegaS71)
wschwebung32 = np.abs(omegaS32)
wschwebungeigen71 = np.abs(omegasL)
wschwebungeigen32 = np.abs(omegasK)

prozentwplus71 = 100*(wpluseigen71-wplus71)/wpluseigen71
print("prozentwplus71:")
print(prozentwplus71)

prozentwplus32 = 100*(wpluseigen32-wplus32)/wpluseigen32
print("prozentwplus32:")
print(prozentwplus32)

prozentwminus71 = 100*(wminuseigen71-wminus71)/wminuseigen71
# print(wminuseigen71)
# print(wminus71)
print("prozentwminus71:")
print(prozentwminus71)

prozentwminus32 = 100*(wminuseigen32-wminus32)/wminuseigen32
# print(wminuseigen32)
# print(wminus32)
print("prozentwminus32:")
print(prozentwminus32)

prozentwschwebung71 = 100*(wschwebungeigen71-wschwebung71)/wschwebungeigen71
# print(wschwebungeigen71)
# print(wschwebung71)
print("prozentwschwebung71:")
print(f"{prozentwschwebung71:.6}")

prozentwschwebung32 = 100*(wschwebungeigen32-wschwebung32)/wschwebungeigen32
# print(wschwebungeigen32)
# print(wschwebung32)
print("prozentwschwebung32:")
print(f"{prozentwschwebung32:.6}")