import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

d, N, F = np.genfromtxt("messungen4.txt", unpack=True)

def absorptionsgesetz(d, A, μ): 
    return A * np.exp(-μ*d)

params, covariance_matrix = curve_fit(absorptionsgesetz, d, N)
uncertainties = np.sqrt(np.diag(covariance_matrix))


for name, value, uncertainty in zip('Aμ', params, uncertainties): 
    print(f'{name} = {value:.3f} ± {uncertainty:.3f}')