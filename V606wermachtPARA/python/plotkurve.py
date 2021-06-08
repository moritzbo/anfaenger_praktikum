import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem
import scipy.constants as const
import uncertainties.unumpy as unp

f, U= np.genfromtxt("daten/kurve.txt", unpack=True)

U = U/10

plt.plot(f,
        U,
        "bx",
        label="Spannungsmesswerte",
        linewidth=1.5)

plt.xlabel(r"$f$ / $\si{\hertz}$")
plt.ylabel(r"$U_{\text{A}}$ / $\si{\volt}$")

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("build/kurve1.pdf")

plt.clf()

plt.plot(f,
        U,
        "bx",
        label="Spannungsmesswerte",
        linewidth=1.5)

plt.xlabel(r"$f$ / $\si{\hertz}$")
plt.ylabel(r"$U_{\text{A}}$/$U_{\text{E}}$")

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("build/kurve2.pdf")