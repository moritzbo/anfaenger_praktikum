import numpy as np
import matplotlib.pyplot as plt

d, N, Fehler_N = np.genfromtxt("python/messungen4.txt", unpack=True)
plt.figure(figsize=(8.0,4.96))
plt.errorbar(d, N + Fehler_N, xerr =0, yerr = Fehler_N, fmt='.')
plt.xlabel(r"$d$[cm]")
plt.ylabel(r"$N$")
plt.title(r'$d$-$N$ Diagramm (lin-lin)')

plt.yticks(np.arange(0,8100, step=500))

plt.tight_layout()
plt.savefig("build/plot4.pdf")


