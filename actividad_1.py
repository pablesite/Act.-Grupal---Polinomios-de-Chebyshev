# -*- coding: utf-8 -*-
""" Codigo main para obtener los resultados de la Actividad 1"""

import math
import time
from scipy import linalg
import matplotlib.pyplot as plt

import numpy as np
from obtencion_nodos import obtencion_nodos_eq, obtencion_nodos_cheb, muestra_nodos
from helpers import vectorize_functions, obtain_f_n


""" Definicion de las funciones originales """
def my_func1(x):
    return math.sin(x)

def my_func2(x):
    return 1/(1 + 25*x**2)

def my_func3(x):
    return math.exp(-20*x**2)

# Inicialización de variables
start = -5; stop = 5; n_points_vec = (11, 21); # Dinámico
# Obtención del vector x, con alto muestreo para ver la función original.
x = np.linspace(start, stop, num=100)
# Obtención de las f(x) de cada una de las funciones. 
my_functions_vec = vectorize_functions((my_func1, my_func2, my_func3)) # Dinámico
f_n = obtain_f_n(my_functions_vec, x)


""" Obtencion de nodos """

### Nodos equispaciados
# Obtención de las x (x_eq_vec) para 11 y 21 puntos
x_eq_vec = obtencion_nodos_eq(start, stop, n_points_vec)
# Valores de las imágenes (f(x)) de las 3 funciones para 11 y 21 puntos
y_n_eq_points = [[0] * n_points_vec[i] for i in range(len(n_points_vec))]
for i in range(len(x_eq_vec)):
    y_n_eq_points[i] = obtain_f_n(my_functions_vec, x_eq_vec[i])
# Representación de las gráficas
muestra_nodos(x, f_n, x_eq_vec, y_n_eq_points)

### Nodos de Chebyshev
# Obtención de las x (x_cheb_vec) para 11 y 21 puntos
x_cheb_vec = obtencion_nodos_cheb(start, stop, n_points_vec)
# Valores de las imágenes (f(x)) de las 3 funciones para 11 y 21 puntos
y_n_cheb_points = [[0] * n_points_vec[i] for i in range(len(n_points_vec))]
for i in range(len(x_cheb_vec)):
    y_n_cheb_points[i] = obtain_f_n(my_functions_vec, x_cheb_vec[i])
# Representación de la gráfica
muestra_nodos(x, f_n, x_cheb_vec, y_n_cheb_points)


""" Algoritmos de interpolación """

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




""" Cálculo de errores """


""" Cálculo de tiempos """








