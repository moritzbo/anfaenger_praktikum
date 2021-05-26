import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

rpm7, l7, s7, m7 = np.genfromtxt("../Data/7aufgabe1.dat", unpack=True)
l10, s10, m10 = np.genfromtxt("../Data/10aufgabe1.dat", unpack=True)
l16, s16, m16 = np.genfromtxt("../Data/16aufgabe1.dat", unpack=True)

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
print("6000rpm      6500rpm     7000rpm     7500rpm      8000rpm")
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

######
print("######")
mean60007mm = np.mean((geschs7[0],geschm7[0],geschl7[0]))
mean60007mmerr = sem((geschs7[0],geschm7[0],geschl7[0]))
mean60007mmU = ufloat(mean60007mm,mean60007mmerr)
print(f"6000rpm 7mm:{mean60007mmU:.6} ")

mean65007mm = np.mean((geschs7[1],geschm7[1],geschl7[1]))
mean65007mmerr = sem((geschs7[1],geschm7[1],geschl7[1]))
mean65007mmU = ufloat(mean65007mm,mean65007mmerr)
print(f"6500rpm 7mm:{mean65007mmU:.6} ")

mean70007mm = np.mean((geschs7[2],geschm7[2],geschl7[2]))
mean70007mmerr = sem((geschs7[2],geschm7[2],geschl7[2]))
mean70007mmU = ufloat(mean70007mm,mean70007mmerr)
print(f"7000rpm 7mm:{mean70007mmU:.6} ")

mean75007mm = np.mean((geschs7[3],geschm7[3],geschl7[3]))
mean75007mmerr = sem((geschs7[3],geschm7[3],geschl7[3]))
mean75007mmU = ufloat(mean75007mm,mean75007mmerr)
print(f"7500rpm 7mm:{mean75007mmU:.6} ")

mean80007mm = np.mean((geschs7[4],geschm7[4],geschl7[4]))
mean80007mmerr = sem((geschs7[4],geschm7[4],geschl7[4]))
mean80007mmU = ufloat(mean80007mm,mean80007mmerr)
print(f"8000rpm 7mm:{mean80007mmU:.6} ")


######
print("######")
mean600010mm = np.mean((geschs10[0],geschm10[0],geschl10[0]))
mean600010mmerr = sem((geschs10[0],geschm10[0],geschl10[0]))
mean600010mmU = ufloat(mean600010mm,mean600010mmerr)
print(f"6000rpm 10mm:{mean600010mmU:.6} ")

mean650010mm = np.mean((geschs10[1],geschm10[1],geschl10[1]))
mean650010mmerr = sem((geschs10[1],geschm10[1],geschl10[1]))
mean650010mmU = ufloat(mean650010mm,mean650010mmerr)
print(f"6500rpm 10mm:{mean650010mmU:.6} ")

mean700010mm = np.mean((geschs10[2],geschm10[2],geschl10[2]))
mean700010mmerr = sem((geschs10[2],geschm10[2],geschl10[2]))
mean700010mmU = ufloat(mean700010mm,mean700010mmerr)
print(f"7000rpm 10mm:{mean700010mmU:.6} ")

mean750010mm = np.mean((geschs10[3],geschm10[3],geschl10[3]))
mean750010mmerr = sem((geschs10[3],geschm10[3],geschl10[3]))
mean750010mmU = ufloat(mean750010mm,mean750010mmerr)
print(f"7500rpm 10mm:{mean750010mmU:.6} ")

mean800010mm = np.mean((geschs10[4],geschm10[4],geschl10[4]))
mean800010mmerr = sem((geschs10[4],geschm10[4],geschl10[4]))
mean800010mmU = ufloat(mean800010mm,mean800010mmerr)
print(f"8000rpm 10mm:{mean800010mmU:.6} ")

######
print("######")
mean600016mm = np.mean((geschs16[0],geschm16[0],geschl16[0]))
mean600016mmerr = sem((geschs16[0],geschm16[0],geschl16[0]))
mean600016mmU = ufloat(mean600016mm,mean600016mmerr)
print(f"6000rpm 16mm:{mean600016mmU:.6} ")

mean650016mm = np.mean((geschs16[1],geschm16[1],geschl16[1]))
mean650016mmerr = sem((geschs16[1],geschm16[1],geschl16[1]))
mean650016mmU = ufloat(mean650016mm,mean650016mmerr)
print(f"6500rpm 16mm:{mean650016mmU:.6} ")

mean700016mm = np.mean((geschs16[2],geschm16[2],geschl16[2]))
mean700016mmerr = sem((geschs16[2],geschm16[2],geschl16[2]))
mean700016mmU = ufloat(mean700016mm,mean700016mmerr)
print(f"7000rpm 16mm:{mean700016mmU:.6} ")

mean750016mm = np.mean((geschs16[3],geschm16[3],geschl16[3]))
mean750016mmerr = sem((geschs16[3],geschm16[3],geschl16[3]))
mean750016mmU = ufloat(mean750016mm,mean750016mmerr)
print(f"7500rpm 16mm:{mean750016mmU:.6} ")

mean800016mm = np.mean((geschs16[4],geschm16[4],geschl16[4]))
mean800016mmerr = sem((geschs16[4],geschm16[4],geschl16[4]))
mean800016mmU = ufloat(mean800016mm,mean800016mmerr)
print(f"8000rpm 16mm:{mean800016mmU:.6} ")