import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

theta, N = np.genfromtxt("../data/Emissionsspektrum.txt", unpack=True)

winkelfehler = 0.0017453292519943296


planck = const.physical_constants["Planck constant"][0]
print(planck)

light = const.physical_constants["speed of light in vacuum"][0]
print(light)

d = 201.4 * 10**(-12)

elem = const.physical_constants["elementary charge"][0]
print(elem)


winkelzink = np.deg2rad(18.9)
winkelgallium = np.deg2rad(18.1)
winkelbrom = np.deg2rad(14.0)
winkelrubidium = np.deg2rad(11.9)
winkelstrontium = np.deg2rad(11.3)
winkelzirkonium = np.deg2rad(10.2)


winkelzinkfehler =              ufloat(np.deg2rad(18.9), winkelfehler)
winkelgalliumfehler =           ufloat(np.deg2rad(18.1), winkelfehler)
winkelbromfehler =              ufloat(np.deg2rad(14.0), winkelfehler)
winkelrubidiumfehler =          ufloat(np.deg2rad(11.9), winkelfehler)
winkelstrontiumfehler =         ufloat(np.deg2rad(11.3), winkelfehler)
winkelzirkoniumfehler =         ufloat(np.deg2rad(10.2), winkelfehler)


Eabszink = planck * light / (2*d * unp.sin(winkelzinkfehler)) / elem
Eabsgallium = planck * light / (2*d * unp.sin(winkelgalliumfehler)) / elem
Eabsbrom = planck * light / (2*d * unp.sin(winkelbromfehler)) / elem
Eabsrubidium = planck * light / (2*d * unp.sin(winkelrubidiumfehler)) / elem
Eabsstrontium = planck * light / (2*d * unp.sin(winkelstrontiumfehler)) / elem
Eabszirkonium = planck * light / (2*d * unp.sin(winkelzirkoniumfehler)) / elem


print(F"Zink Energie ist: {Eabszink} in eV")
print(F"Gallium Energie ist: {Eabsgallium} in eV")
print(F"Brom Energie ist: {Eabsbrom} in eV")
print(F"Rubidium Energie ist: {Eabsrubidium} in eV")
print(F"Strontium Energie ist: {Eabsstrontium} in eV")
print(F"Zirkonium Energie ist: {Eabszirkonium} in eV")


ryddi = const.physical_constants["Rydberg constant times hc in eV"][0]

sommerfeld = const.physical_constants['fine-structure constant'][0]

print(sommerfeld)
print(ryddi)


#sigma = Z - unp.sqrt( (Ekabs/ryddi) - ((sommerfeld**(2) Z**(4))/4) )

Zzink = 30
Zgallium = 31
Zbrom = 35  
Zrubidium = 37
Zstrontium = 38
Zzirkonium = 40


sigmaZINK           =      Zzink - unp.sqrt( (Eabszink/ryddi) - ((sommerfeld**(2) *Zzink**(4))/4) )
sigmaGALLIUM        = Zgallium - unp.sqrt( (Eabsgallium/ryddi) - ((sommerfeld**(2) *Zgallium**(4))/4) )
sigmaBROM       = Zbrom - unp.sqrt( (Eabsbrom/ryddi) - ((sommerfeld**(2) *Zbrom**(4))/4) )
sigmaRUBIDIUM   = Zrubidium - unp.sqrt( (Eabsrubidium/ryddi) - ((sommerfeld**(2) *Zrubidium**(4))/4) )
sigmaSTRONTIUM = Zstrontium - unp.sqrt( (Eabsstrontium/ryddi) - ((sommerfeld**(2) *Zstrontium**(4))/4) )
sigmaZIRKONIUM = Zzirkonium - unp.sqrt( (Eabszirkonium/ryddi) - ((sommerfeld**(2) *Zzirkonium**(4))/4) )

print(F"Abschirmkonstante für ZINK: {sigmaZINK}")
print(F"Abschirmkonstante für GALLIUM: {sigmaGALLIUM}")
print(F"Abschirmkonstante für BROM: {sigmaBROM}")
print(F"Abschirmkonstante für RUBIDIUM: {sigmaRUBIDIUM}")
print(F"Abschirmkonstante für STRONTIUM: {sigmaSTRONTIUM}")
print(F"Abschirmkonstante für ZIRKONIUM: {sigmaZIRKONIUM}")








        
Elitzink=                         9.67* 10**3  *elem
Elitgermanium=                    10.38* 10**3   *elem
Elitbrom=                       13.48* 10**3   *elem
Elitrubidium=                    15.21* 10**3   *elem
Elitstrontium=                    16.11* 10**3   *elem
Elitzirkonium =                    18.01* 10**3   *elem




winkellitzink=            np.arcsin( (planck * light)/(2* d * Elitzink) )    
winkellitgermanium=       np.arcsin( (planck * light)/(2* d * Elitgermanium))
winkellitbrom=            np.arcsin( (planck * light)/(2* d * Elitbrom) )
winkellitrubidium=        np.arcsin( (planck * light)/(2* d * Elitrubidium) )
winkellitstrontium=       np.arcsin( (planck * light)/(2* d * Elitstrontium) )   
winkellitzirkonium =      np.arcsin( (planck * light)/(2* d * Elitzirkonium) )


winkellitzink2 = np.rad2deg(winkellitzink)
winkellitgermanium2 = np.rad2deg(winkellitgermanium)
winkellitbrom2 = np.rad2deg(winkellitbrom)
winkellitrubidium2 = np.rad2deg(winkellitrubidium)
winkellitstrontium2 = np.rad2deg(winkellitstrontium)
winkellitzirkonium2 = np.rad2deg(winkellitzirkonium)


print(F"WINKEL für ZINK: {winkellitzink2}")
print(F"WINKEL für GALLIUM: {winkellitgermanium2}")
print(F"WINKEL für BROM: {winkellitbrom2}")
print(F"WINKEL für RUBIDIUM: {winkellitrubidium2}")
print(F"WINKEL für STRONTIUM: {winkellitstrontium2}")
print(F"WINKEL für ZIRKONIUM: {winkellitzirkonium2}")



Elitzink=                         9.67* 10**3  
Elitgermanium=                    10.38* 10**3   
Elitbrom=                       13.48* 10**3   
Elitrubidium=                    15.21* 10**3   
Elitstrontium=                    16.11* 10**3   
Elitzirkonium =                    18.01* 10**3  



sigmaZINKlit = Zzink - np.sqrt( (Elitzink/ryddi) - ((sommerfeld**(2) *Zzink**(4))/4) )
sigmaGALLIUMlit = Zgallium - np.sqrt( (Elitgermanium/ryddi) - ((sommerfeld**(2) *Zgallium**(4))/4) )
sigmaBROMlit = Zbrom - np.sqrt( (Elitbrom/ryddi) - ((sommerfeld**(2) *Zbrom**(4))/4) )
sigmaRUBIDIUMlit = Zrubidium - np.sqrt( (Elitrubidium/ryddi) - ((sommerfeld**(2) *Zrubidium**(4))/4) )
sigmaSTRONTIUMlit = Zstrontium - np.sqrt( (Elitstrontium/ryddi) - ((sommerfeld**(2) *Zstrontium**(4))/4) )
sigmaZIRKONIUMlit = Zzirkonium - np.sqrt( (Elitzirkonium/ryddi) - ((sommerfeld**(2) *Zzirkonium**(4))/4) )

print(F"Abschirmkonstante für ZINK: {sigmaZINKlit}")
print(F"Abschirmkonstante für GALLIUM: {sigmaGALLIUMlit}")
print(F"Abschirmkonstante für BROM: {sigmaBROMlit}")
print(F"Abschirmkonstante für RUBIDIUM: {sigmaRUBIDIUMlit}")
print(F"Abschirmkonstante für STRONTIUM: {sigmaSTRONTIUMlit}")
print(F"Abschirmkonstante für ZIRKONIUM: {sigmaZIRKONIUMlit}")


prozentZINKenergie = 100- 100 * (Eabszink/Elitzink)
prozentGALLIUMenergie =100- 100 * (Eabsgallium/Elitgermanium)
prozentBROMenergie = 100-  100 * (Eabsbrom/Elitbrom)
prozentRUBIDIUMenergie = 100- 100 * (Eabsrubidium/Elitrubidium)
prozentSTRONTIUMenergie = 100- 100 * (Eabsstrontium/Elitstrontium)
prozentZIRKONIUMenergie = 100- 100 * (Eabszirkonium/Elitzirkonium)

print(F"PROZENT für ZINK: {prozentZINKenergie}")
print(F"PROZENT für GALLIUM: {prozentGALLIUMenergie}")
print(F"PROZENT für BROM: {prozentBROMenergie}")
print(F"PROZENT für RUBIDIUM: {prozentRUBIDIUMenergie}")
print(F"PROZENT für STRONTIUM: {prozentSTRONTIUMenergie}")
print(F"PROZENT für ZIRKONIUM: {prozentZIRKONIUMenergie}")

winkelzink = 18.9
winkelgallium = 18.1
winkelbrom = 14.0
winkelrubidium = 11.9
winkelstrontium = 11.3
winkelzirkonium = 10.2

winkelzink3         =               ufloat(winkelzink,0.1)
winkelgallium3   =            ufloat(winkelgallium,0.1)
winkelbrom3         =               ufloat(winkelbrom,0.1)
winkelrubidium3     =           ufloat(winkelrubidium,0.1)
winkelstrontium3 =          ufloat(winkelstrontium,0.1)
winkelzirkonium3 =          ufloat(winkelzirkonium,0.1)




prozentZINKwinkel = 100- 100 *           (winkelzink3      / winkellitzink2      )
prozentGALLIUMwinkel =100- 100 *         (winkelgallium3   / winkellitgermanium2         )
prozentBROMwinkel = 100-  100 *          (winkelbrom3      / winkellitbrom2      )
prozentRUBIDIUMwinkel = 100- 100 *       (winkelrubidium3  / winkellitrubidium2          )
prozentSTRONTIUMwinkel = 100- 100 *      (winkelstrontium3 / winkellitstrontium2     )
prozentZIRKONIUMwinkel = 100- 100 *      (winkelzirkonium3 / winkellitzirkonium2     )

print("LEER WICHTIG")

print(F"PROZENT für ZINK: {prozentZINKwinkel}")
print(F"PROZENT für GALLIUM: {prozentGALLIUMwinkel}")
print(F"PROZENT für BROM: {prozentBROMwinkel}")
print(F"PROZENT für RUBIDIUM: {prozentRUBIDIUMwinkel}")
print(F"PROZENT für STRONTIUM: {prozentSTRONTIUMwinkel}")
print(F"PROZENT für ZIRKONIUM: {prozentZIRKONIUMwinkel}")

print("LEER WICHTIG")

prozentZINKsigma = 100- 100 *           (sigmaZINK       / sigmaZINKlit)
prozentGALLIUMsigma =100- 100 *         (sigmaGALLIUM    / sigmaGALLIUMlit        )
prozentBROMsigma = 100-  100 *          (sigmaBROM       / sigmaBROMlit)
prozentRUBIDIUMsigma = 100- 100 *       (sigmaRUBIDIUM   / sigmaRUBIDIUMlit        )
prozentSTRONTIUMsigma = 100- 100 *      (sigmaSTRONTIUM  / sigmaSTRONTIUMlit    )
prozentZIRKONIUMsigma = 100- 100 *      (sigmaZIRKONIUM  / sigmaZIRKONIUMlit    )

print(F"PROZENT für ZINK: {prozentZINKsigma}")
print(F"PROZENT für GALLIUM: {prozentGALLIUMsigma}")
print(F"PROZENT für BROM: {prozentBROMsigma}")
print(F"PROZENT für RUBIDIUM: {prozentRUBIDIUMsigma}")
print(F"PROZENT für STRONTIUM: {prozentSTRONTIUMsigma}")
print(F"PROZENT für ZIRKONIUM: {prozentZIRKONIUMsigma}")
