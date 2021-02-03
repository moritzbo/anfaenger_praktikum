import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

winkelfehler = 0.0017453292519943296


planck = const.physical_constants["Planck constant"][0]
print(planck)

light = const.physical_constants["speed of light in vacuum"][0]
print(light)

d = 201.4 * 10**(-12)

elem = const.physical_constants["elementary charge"][0]
print(elem)

ryddi = const.physical_constants["Rydberg constant times hc in eV"][0]

sommerfeld = const.physical_constants['fine-structure constant'][0]

Zzink = 30
Zgallium = 31
Zbrom = 35  
Zrubidium = 37
Zstrontium = 38
Zzirkonium = 40


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



sigmaZINK           =      Zzink - unp.sqrt( (Eabszink/ryddi) - ((sommerfeld**(2) *Zzink**(4))/4) )
sigmaGALLIUM        = Zgallium - unp.sqrt( (Eabsgallium/ryddi) - ((sommerfeld**(2) *Zgallium**(4))/4) )
sigmaBROM       = Zbrom - unp.sqrt( (Eabsbrom/ryddi) - ((sommerfeld**(2) *Zbrom**(4))/4) )
sigmaRUBIDIUM   = Zrubidium - unp.sqrt( (Eabsrubidium/ryddi) - ((sommerfeld**(2) *Zrubidium**(4))/4) )
sigmaSTRONTIUM = Zstrontium - unp.sqrt( (Eabsstrontium/ryddi) - ((sommerfeld**(2) *Zstrontium**(4))/4) )
sigmaZIRKONIUM = Zzirkonium - unp.sqrt( (Eabszirkonium/ryddi) - ((sommerfeld**(2) *Zzirkonium**(4))/4) )

z = [30-unp.nominal_values(sigmaZINK), 31-unp.nominal_values(sigmaGALLIUM), 35-unp.nominal_values(sigmaBROM), 37-unp.nominal_values(sigmaRUBIDIUM), 38-unp.nominal_values(sigmaSTRONTIUM), 40-unp.nominal_values(sigmaZIRKONIUM)]


Eabszinknom= unp.nominal_values(Eabszink)
Eabsgalliumnom= unp.nominal_values(Eabsgallium)
Eabsbromnom= unp.nominal_values(Eabsbrom)
Eabsrubidiumnom= unp.nominal_values(Eabsrubidium)
Eabsstrontiumnom= unp.nominal_values(Eabsstrontium)
Eabszirkoniumnom= unp.nominal_values(Eabszirkonium)



print(Eabszinknom)

E = [Eabszinknom**(1/2), Eabsgalliumnom**(1/2), Eabsbromnom**(1/2), Eabsrubidiumnom**(1/2), Eabsstrontiumnom**(1/2), Eabszirkoniumnom**(1/2)]


print(F"Energie: Eabszink: {Eabszink}")
print(F"Energie: Eabsgallium: {Eabsgallium}")
print(F"Energie: Eabsbrom: {Eabsbrom}")
print(F"Energie: Eabsrubidium: {Eabsrubidium}")
print(F"Energie: Eabsstrontium: {Eabsstrontium}")
print(F"Energie: Eabszirkonium: {Eabszirkonium}")



params, covar_matrix = np.polyfit(z, E, deg= 1, cov=True)

errors = np.sqrt(np.diag(covar_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.2f} ± {error:.2f}')


x=np.linspace(25, 40)

plt.plot(x, params[0]*x + params[1], "k-", label="Ausgleichgerade")


plt.plot(z, E, "bx", label="Messwerte")
plt.legend()
plt.grid()
plt.xlabel(r'$Z-\sigma$')
plt.ylabel(r'$\sqrt{E_{k\text{,abs}}}[\si{\electronvolt}]')


plt.savefig("build/plotmoseley.pdf")