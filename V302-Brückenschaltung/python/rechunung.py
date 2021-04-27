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
R_21gem = 332
R_21fehler = R_21gem * 0.002
R_21gesamt = ufloat(R_21gem, R_21fehler)

R_22gem = 664
R_22fehler = R_22gem * 0.002
R_22gesamt = ufloat(R_22gem, R_22fehler)

R_31 = 416
R_41 = 584

R_32 = 260
R_42 = 740

R_ver_1gem = R_31/R_41
R_ver_1fehler = R_ver_1gem * 0.005
R_ver_1gesamt = ufloat(R_ver_1gem, R_ver_1fehler)

R_ver_2gem  = R_32/R_42
R_ver_2fehler = R_ver_2gem * 0.005
R_ver_2gesamt = ufloat(R_ver_2gem, R_ver_2fehler)

Rx1 = R_21gesamt * R_ver_1gesamt
Rx2 = R_22gesamt * R_ver_2gesamt

print(Rx1)
print(Rx2)


R_mittelwert_hand = (Rx1 + Rx2)/2

print(R_mittelwert_hand)