import numpy as np
import matplotlib.pyplot as plt

d, N, Fehler_N = np.genfromtxt("python/messungen4.txt", unpack=True)

plt.figure(figsize=(8.0,4.96))
plt.errorbar(d, N + Fehler_N, xerr =0, yerr = Fehler_N, fmt='kx')
plt.xlabel(r"$d$[cm]")
plt.ylabel(r"$N$")
plt.title(r'$d$-$N$ Diagramm (lin-log)')
plt.yscale("log")
plt.grid()
plt.tight_layout()


plt.savefig("build/plot5.pdf")