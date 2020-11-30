import numpy as np

g = [60, 80, 100, 110, 120, 125]
b= [285, 142, 117, 85, 86, 82]
summe = 0
for weite, brenn in zip(g,b):
    f = (weite * brenn) / (weite + brenn)
    summe = summe + f
    print(f'Für g={weite} und b={brenn} folgt f={f:.2f}')
print(summe)