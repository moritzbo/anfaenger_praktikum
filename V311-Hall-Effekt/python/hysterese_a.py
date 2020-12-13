import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
from scipy.stats import sem


# define the true objective function
def objective(x, a, b, c, d, e, f, g, h, i):
    return a * x + b * x**2 + c * x**3 + d * c**4 + e * x**5 + f * x**6 +g * x**7 + h * x**8 +i


x, y = np.genfromtxt("Daten/daten_magnet_z.txt", unpack = True)

#curve_fit
popt, _ = curve_fit(objective, x, y, maxfev=5000000)

a, b, c, d, e, f, g, h, i = popt
print('y = %.5f * x + %.5f' % (a, b), flush = True)


plt.scatter(x, y)
#plt.scatter(A_messung1, mT_messung1)

# define a sequence of inputs between the smallest and largest known inputs
#leider rigged, deshalb  manuell
#x_line = np.arange(min(x), max(x), 1)
x_line = np.arange(min(x), max(x), 0.001)
y_line = objective(x_line, a, b, c, d, e, f, g, h, i)

# create a line plot for the mapping function
plt.plot(x_line, y_line, '--', color='red')

plt.xlim(0,7)
plt.ylim(0,1800)




#plt.show()
