from scipy import linalg
import numpy as np
import math
import matplotlib.pyplot as plt
import time

def my_sin(x):
    return math.sin(x)

def my_func2(x):
    return 1/(1 + 25*x**2)


# Inicialización de variables (11 nodos)
start = -5; stop = 5; nPoints = 11;
step = (stop - start + 1)/nPoints;

# Obtención de nodos
# Array de valores de la x
x = np.arange(start, stop + 1, step) 

my_sin_vec = np.vectorize(my_sin)
my_func2_vec = np.vectorize(my_func2)
#f = my_sin_vec(x)
f = my_func2_vec(x)

plt.plot(x, f)

# Con nodos equispaciados
from scipy.interpolate import barycentric_interpolate

x1 = np.linspace(min(x), max(x), num=100)

y = barycentric_interpolate(x, f, x1)
y_ref = my_sin_vec(x1)
y_ref = my_func2_vec(x1)
plt.plot(x, f, "o", label="observation")
plt.plot(x1, y, label="barycentric interpolation")
plt.plot(x1, y_ref, label="my_func2")
plt.legend()
plt.show()


# Con nodos de Chebyshev
import numpy.polynomial.chebyshev as cheb

coeffs_cheb = [0]*11 + [1]
T11 = cheb.Chebyshev(coeffs_cheb, [-5, 5])
xp_ch = T11.roots()
#raices = cheb.chebroots(f)
y = barycentric_interpolate(xp_ch, f, x1)
#y_ref = my_sin_vec(x1)
y_ref = my_func2_vec(x1)
plt.plot(xp_ch, f, "o", label="observation")
plt.plot(x1, y, label="barycentric interpolation")
plt.plot(x1, y_ref, label="my_func2")
plt.legend()
plt.show()


#Lagrange

#Lagrange
from scipy.interpolate import lagrange

# Lagrange Interpolation
f = my_func2_vec(x)  # Función a utilizar
y_ref = my_func2_vec(x1)

# Calcular el polinomio interpolante de Lagrange
polynomial = lagrange(x, f)

# Evaluar el polinomio interpolante en los puntos x1
y = polynomial(x1)

plt.plot(x, f, "o", label="Observaciones")
plt.plot(x1, y, label="Lagrange Interpolation")
plt.plot(x1, y_ref, label="my_func2")
plt.legend()
plt.show()


