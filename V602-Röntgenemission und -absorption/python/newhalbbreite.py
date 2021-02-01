import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

theta, N = np.genfromtxt("../data/Emissionsspektrum.txt", unpack=True)

winkelfehler = 0.0017453292519943296

halbintalpha = 5050/2

halbintbeta = 1599/2

print(halbintalpha)
print(halbintbeta)

planck = const.physical_constants["Planck constant"][0]
print(planck)

light = const.physical_constants["speed of light in vacuum"][0]
print(light)

d = 201.4 * 10**(-12)

elem = const.physical_constants["elementary charge"][0]
print(elem)

alphamain = ufloat(0.39269908169872414, winkelfehler)
betamain = ufloat(0.35255650890285456, winkelfehler)

Ealpha = planck * light / (2*d * unp.sin(alphamain)) / elem
Ebeta = planck * light / (2*d * unp.sin(betamain)) / elem

print(f"{Ealpha:.0f}")
print(F"{Ebeta:.0f}")

alphaleft = ufloat(0.3501130479500625, winkelfehler)
alpharight = ufloat(0.3586651612848347, winkelfehler)
betaleft = ufloat(0.3900810878207327, winkelfehler)
betaright = ufloat(0.3988077340807043, winkelfehler)



alphaleft2 = ufloat(20.06, 0.1)
alpharight2 = ufloat(20.55, 0.1)
betaleft2 = ufloat(22.35, 0.1)
betaright2 = ufloat(22.85, 0.1)



halbbeta = betaright2 - betaleft2
halbalpha = alpharight2 - alphaleft2
print(f"Halbwert BETA: {halbbeta:.2f}")
print(f"Halbwert ALPHA: {halbalpha:.2f}")



Ealphalinks = planck * light / (2*d * unp.sin(alphaleft)) / elem
Ealpharechts = planck * light / (2*d * unp.sin(alpharight)) / elem

Ebetalinks = planck * light / (2*d * unp.sin(betaleft)) / elem
Ebetarechts = planck * light / (2*d * unp.sin(betaright)) / elem


print(f"alpha links {Ealphalinks:.0f}")
print(f"alpha rechts {Ealpharechts:.0f}")
print(f"beta links {Ebetalinks:.0f}")
print(f"beta rechts {Ebetarechts:.0f}")

deltaalpha = Ealphalinks - Ealpharechts
deltabeta = Ebetalinks - Ebetarechts

print(f"delta alpha {deltaalpha:.0f}")
print(f"delta beta {deltabeta:.0f}")

Aalpha = Ealpha / deltaalpha
Abeta = Ebeta / deltabeta

print(F"Auflöse alpha {Aalpha:.2f}")
print(F"Auflöse beta {Abeta:.2f}")

ryddi = const.physical_constants["Rydberg constant times hc in eV"][0]

#sigma1 = 29 - ((8987.96)/(13.6057))**(1/2)




ZKupfer = 29

Ekabs = (8987.96)

sigma1 = ZKupfer - unp.sqrt( Ekabs/ryddi)
sigma2 = ZKupfer - 2* unp.sqrt((ryddi* (ZKupfer-sigma1)**2 - Ealpha)/(ryddi))
sigma3 = ZKupfer - 2* unp.sqrt((ryddi* (ZKupfer-sigma1)**2 - Ebeta)/(ryddi))


print(F"SIGMA1 ist: {sigma1:.3f}")
print(F"SIGMA2 ist: {sigma2:.3f}")
print(F"SIGMA3 ist: {sigma3:.3f}")
print(ryddi)


test = (planck * light * np.cos(0.3586651612848347) * (winkelfehler)) / (2*d* (np.sin(0.3586651612848347))**(2)  *elem )
print(test)