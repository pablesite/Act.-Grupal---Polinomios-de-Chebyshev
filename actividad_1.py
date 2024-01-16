""" Código main para obtener los resultados de la Actividad 1"""

import math
import time
from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt


""" Definición de funciones """

def my_func1(x):
    return math.sin(x)

def my_func2(x):
    return 1/(1 + 25*x**2)

def my_func3(x):
    return math.exp(-20*x**2)


""" Obtención de nodos """

# Inicialización de variables
start = -5; stop = 5; nPoints_11 = 11; nPoints_21 = 21;

### Nodos equispaciados
# Valores de la x para 11 y 21 puntos
step_11 = (stop - start)/(nPoints_11 - 1)
step_21 = (stop - start)/(nPoints_21 - 1)
steps = (step_11, step_21)
x_eq_11 = np.arange(start, stop + steps[1], steps[0]) 
x_eq_21 = np.arange(start, stop + steps[1], steps[1]) 

# Valores de las imágenes de las funciones
my_func1_vec = np.vectorize(my_func1)
my_func2_vec = np.vectorize(my_func2)
my_func3_vec = np.vectorize(my_func3)
y_1_eq_11 = my_func1_vec(x_eq_11)
y_2_eq_11 = my_func2_vec(x_eq_11)
y_3_eq_11 = my_func3_vec(x_eq_11)

y_1_eq_21 = my_func1_vec(x_eq_21)
y_2_eq_21 = my_func2_vec(x_eq_21)
y_3_eq_21 = my_func3_vec(x_eq_21)

fig, ax = plt.subplots(2, 3)

x = np.linspace(start, stop, num=100)
f_1 = my_func1_vec(x)
f_2 = my_func2_vec(x)
f_3 = my_func3_vec(x)

ax[0, 0].plot(x_eq_11, y_1_eq_11, "o")
ax[0, 0].plot(x, f_1)
ax[0, 1].plot(x_eq_11, y_2_eq_11, "o")
ax[0, 1].plot(x, f_2)
ax[0, 2].plot(x_eq_11, y_3_eq_11, "o")
ax[0, 2].plot(x, f_3)
ax[1, 0].plot(x_eq_21, y_1_eq_21, "o")
ax[1, 0].plot(x, f_1)
ax[1, 1].plot(x_eq_21, y_2_eq_21, "o")
ax[1, 1].plot(x, f_2)
ax[1, 2].plot(x_eq_21, y_3_eq_21, "o")
ax[1, 2].plot(x, f_3)
plt.legend()
plt.show()



# Nodos de Chebyshev
import numpy.polynomial.chebyshev as cheb
coeffs_cheb = [0]*11 + [1]
T11 = cheb.Chebyshev(coeffs_cheb, [-5, 5])
xp_ch = T11.roots()

#FALTA PLOT


""" Algoritmos de interpolación """


""" Cálculo de errores """


""" Cálculo de tiempos """






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


