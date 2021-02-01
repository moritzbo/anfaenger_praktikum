import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp



#ZINK

theta, N = np.genfromtxt("data/Zink.txt", unpack=True)

plt.plot(theta, N, "bx", label="Zählraten bei Zink")
plt.grid()
plt.xlabel(r'$\theta[\textdegree]$')
plt.ylabel(r'$N[\si{{\text{Imp}}\per\second}]$')
plt.legend(loc="lower right")
plt.savefig("build/plotzink.pdf")
plt.clf()

#Gallium

theta, N = np.genfromtxt("data/Gallium.txt", unpack=True)

plt.plot(theta, N, "bx", label="Zählraten bei Gallium")
plt.grid()
plt.xlabel(r'$\theta[\textdegree]$')
plt.ylabel(r'$N[\si{{\text{Imp}}\per\second}]$')
plt.legend(loc="lower right")
plt.savefig("build/plotgallium.pdf")
plt.clf()

#Brom

theta, N = np.genfromtxt("data/Brom.txt", unpack=True)

plt.plot(theta, N, "bx", label="Zählraten bei Brom")
plt.grid()
plt.xlabel(r'$\theta[\textdegree]$')
plt.ylabel(r'$N[\si{{\text{Imp}}\per\second}]$')
plt.legend(loc="lower right")
plt.savefig("build/plotbrom.pdf")
plt.clf()

#Rubidium

theta, N = np.genfromtxt("data/Rubidium.txt", unpack=True)

plt.plot(theta, N, "bx", label="Zählraten bei Rubidium")
plt.grid()
plt.xlabel(r'$\theta[\textdegree]$')
plt.ylabel(r'$N[\si{{\text{Imp}}\per\second}]$')
plt.legend(loc="lower right")
plt.savefig("build/plotrubidium.pdf")
plt.clf()

#Strontium

theta, N = np.genfromtxt("data/Strontium.txt", unpack=True)

plt.plot(theta, N, "bx", label="Zählraten bei Strontium")
plt.grid()
plt.xlabel(r'$\theta[\textdegree]$')
plt.ylabel(r'$N[\si{{\text{Imp}}\per\second}]$')
plt.legend(loc="lower right")
plt.savefig("build/plotstrontium.pdf")
plt.clf()

#Zirkonium  

theta, N = np.genfromtxt("data/Zirkonium.txt", unpack=True)

plt.plot(theta, N, "bx", label="Zählraten bei Zirkonium")
plt.grid()
plt.xlabel(r'$\theta[\textdegree]$')
plt.ylabel(r'$N[\si{{\text{Imp}}\per\second}]$')
plt.legend(loc="lower right")
plt.savefig("build/plotzirkonium.pdf")
plt.clf()

