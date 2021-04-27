import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import unumpy
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

#FEHLER AUF ALLE REFERENZTEILE R2,C2,L2 = +- 0.2 %
# Rx = R2 * (R3/R4)


#RECHNUNG WHEATSTONE
#R_21gem = 332
#R_21fehler = R_21gem * 0.002
#R_21gesamt = ufloat(R_21gem, R_21fehler)
#
#R_22gem = 664
#R_22fehler = R_22gem * 0.002
#R_22gesamt = ufloat(R_22gem, R_22fehler)
#
#R_31 = 416
#R_41 = 584
#
#R_32 = 260
#R_42 = 740
#
#R_ver_1gem = R_31/R_41
#R_ver_1fehler = R_ver_1gem * 0.005
#R_ver_1gesamt = ufloat(R_ver_1gem, R_ver_1fehler)
#
#R_ver_2gem  = R_32/R_42
#R_ver_2fehler = R_ver_2gem * 0.005
#R_ver_2gesamt = ufloat(R_ver_2gem, R_ver_2fehler)
#
#Rx1 = R_21gesamt * R_ver_1gesamt
#Rx2 = R_22gesamt * R_ver_2gesamt
#
#print(Rx1)
#print(Rx2)
#
#
#R_mittelwert_hand = (Rx1 + Rx2)/2
#
#print(R_mittelwert_hand)

#---------------------------------------------------------------------------------------

#FEHLER AUF ALLE REFERENZTEILE R2,C2,L2 = +- 0.2 %
# Rx = R2 * (R3/R4)
# Cx = C2 * (R4/R3)
#C2gem = 399 
#C2fehler = C2gem * 0.002
#C2gesamt = ufloat(C2gem, C2fehler)
#
#R2gem = 493
#R2fehler = R2gem * 0.03
#R2gesamt = ufloat(R2gem, R2fehler)
#
#R_3 = 477
#R_4 = 523
#
#R_ver_gem = R_3/R_4
#R_ver_fehler = R_ver_gem * 0.005
#R_ver_gesamt = ufloat(R_ver_gem, R_ver_fehler)
#
#Rx = R2gesamt * R_ver_gesamt
#Cx = C2gesamt * 1/(R_ver_gesamt)
#
#print(f"{Rx:.1f}")
#print(f"{Cx:.1f}")
#Rx = 449.6+/-13.7
#Cx = 437.5+/-2.4

#---------------------------------------------------------------------------------------

#FEHLER AUF ALLE REFERENZTEILE R2,C2,L2 = +- 0.2 %
# Rx = R2 * (R3/R4)
# Lx = L2 * (R3/R4)

#L2gem = 27.5 
#L2fehler = L2gem * 0.002
#L2gesamt = ufloat(L2gem, L2fehler)
#
#R2gem = 49
#R2fehler = R2gem * 0.03
#R2gesamt = ufloat(R2gem, R2fehler)
#
#R_3 = 581
#R_4 = 419
#
#R_ver_gem = R_3/R_4
#R_ver_fehler = R_ver_gem * 0.005
#R_ver_gesamt = ufloat(R_ver_gem, R_ver_fehler)
#
#Rx = R2gesamt * R_ver_gesamt
#Lx = L2gesamt * R_ver_gesamt
#print(f"{Rx:.1f}")
#print(f"{Lx:.1f}")
#Rx = 67.9+/-2.1
#Lx = 38.1+/-0.2

#---------------------------------------------------------------------------------------

#FEHLER AUF ALLE REFERENZTEILE R2,C2,L2 = +- 0.2 %
# Rx = R2 * (R3/R4)
# Lx = R2 * R3 * C4
#
#C4gem = 399 
#C4fehler = C4gem * 0.002
#C4gesamt = ufloat(C4gem, C4fehler)
#
#R2gem = 1000
#R2fehler = R2gem * 0.002
#R2gesamt = ufloat(R2gem, R2fehler)
#
#R_3 = 89
#R_3fehler = R_3 * 0.03
#R_3ges = ufloat(R_3, R_3fehler)
#
#R_4 = 811
#R_4fehler = R_4 * 0.03
#R_4ges = ufloat(R_4, R_4fehler)
#
#R_ver_ges = R_3ges/R_4ges
#
#Rx = R2gesamt * R_ver_ges
#Lx = R2gesamt * R_3ges * C4gesamt * (10)**(-6)
#
#print(f"{Rx:.1f}")
#print(f"{Lx:.1f}")
#Rx = 109.7+/-4.7
#Lx = 35.5+/-1.1 [milli Henry]
