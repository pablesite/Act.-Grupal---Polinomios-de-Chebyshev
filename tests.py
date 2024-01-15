from scipy import linalg
import numpy as np
import math
import matplotlib.pyplot as plt

def my_sin(x):
    return math.sin(x)




# Inicialización de variables (11 nodos)
start = -5; stop = 5; nPoints = 11;
step = (stop - start + 1)/nPoints;


# Obtención de nodos
# Array de valores de la x
x = np.arange(start, stop + 1, step) 
# Array de las imágenes de la función (f(x) = sin(x))
my_sin_vec = np.vectorize(my_sin)
f = my_sin_vec(x)


plt.plot(x, f)


import numpy.polynomial.chebyshev as cheb

raices = cheb.chebroots(f)

from scipy.interpolate import barycentric_interpolate






x1 = np.linspace(min(x), max(x), num=100)

y = barycentric_interpolate(x, f, x1)
plt.plot(x, f, "o", label="observation")
plt.plot(x1, y, label="barycentric interpolation")
plt.legend()
plt.show()