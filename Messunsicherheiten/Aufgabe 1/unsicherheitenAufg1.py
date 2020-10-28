import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

r_innen = ufloat(10, 1)
r_außen = ufloat(15, 1)
h = ufloat(20, 1)

v = ufloat(200, 10)
t = 6
m = ufloat(0.005, 0.0001)
def VolumeCylinder(r_innen, r_außen, h):
    return np.pi * h *(r_außen**2 - r_innen**2)

def Strecke(v, t):
    return v*t

def Ekin(m, v):
    return 0.5 * m * v**2

print(VolumeCylinder(r_innen, r_außen, h))
print(Strecke(v,t))
print(Ekin(m, v))
