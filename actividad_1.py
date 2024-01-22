""" Codigo main para obtener los resultados de la Actividad 1"""
import math
import numpy as np

from obtencion_nodos import vectorize_functions, obtain_f_n, obtencion_nodos_eq, obtencion_nodos_cheb, muestra_nodos
from interpolacion import interp_bar, interp_lag, interp_new, interp_spl, error, muestra_interpolacion


""" Definicion de las funciones originales """
def my_func1(x):
    return math.sin(x)

def my_func2(x):
    return 1/(1 + 25*x**2)

def my_func3(x):
    return math.exp(-20*x**2)

### Inicializacion de variables.

# 1 intervalo [start, stop] para cada función.
start = [-np.pi, -4, -1]
stop  = [ np.pi,  4,  1]

# Se pueden indicar tantos números de nodos como se quiera.
n_points_vec = (11, 21) 

# Obtencion del vector x, con alto muestreo para ver la funcion original.
x = [0] * len(start)
for i in range(len(start)):
    x[i] = np.linspace(start[i], stop[i], num=1000)

# Obtencion de las f(x) de cada una de las funciones. 
my_functions_vec = vectorize_functions((my_func1, my_func2, my_func3))
f_n = obtain_f_n(my_functions_vec, x)


""" Obtencion de nodos """
### Nodos equispaciados
# Obtencion de las x (x_eq_vec) para 11 y 21 puntos
x_eq_vec = obtencion_nodos_eq(start, stop, n_points_vec)
# Valores de las imagenes (f(x)) de las 3 funciones para 11 y 21 puntos
y_n_eq_points = [[0] * n_points_vec[i] for i in range(len(n_points_vec))]
#y_n_eq_points = [[[0] * len(x[0]) for i in range(len(f_n))] for j in range(len(n_points_vec))]


for i in range(len(x_eq_vec)):
    y_n_eq_points[i] = obtain_f_n(my_functions_vec, x_eq_vec[i])
# Representacion de las graficas
muestra_nodos(x, f_n, x_eq_vec, y_n_eq_points, "Nodos Equispaciados")

### Nodos de Chebyshev
# Obtencion de las x (x_cheb_vec) para 11 y 21 puntos
x_cheb_vec = obtencion_nodos_cheb(start, stop, n_points_vec)
# Valores de las imagenes (f(x)) de las 3 funciones para 11 y 21 puntos
y_n_cheb_points = [[0] * n_points_vec[i] for i in range(len(n_points_vec))]
for i in range(len(x_cheb_vec)):
    y_n_cheb_points[i] = obtain_f_n(my_functions_vec, x_cheb_vec[i])
# Representacion de la grafica
muestra_nodos(x, f_n, x_cheb_vec, y_n_cheb_points, "Nodos de Chebyshev")


""" Algoritmos de interpolacion """

### Barycentric

# Con nodos equispaciados
y_n_eq_bar, tiemps_n_eq_bar = interp_bar(x_eq_vec, y_n_eq_points, x)
error_n_eq_bar = error(y_n_eq_bar, f_n)
muestra_interpolacion(x, f_n, y_n_eq_bar,  "Interpolación baricéntrica, nodos equispaciados.")
    
# Con nodos Chebyshev
y_n_cheb_bar, tiemps_n_cheb_bar = interp_bar(x_cheb_vec, y_n_cheb_points, x)
error_n_cheb_bar = error(y_n_cheb_bar, f_n)
muestra_interpolacion(x, f_n, y_n_cheb_bar, "Interpolación baricéntrica, nodos de Chebyshev.")


### Lagrange

# Con nodos equispaciados
y_n_eq_lag, tiemps_n_eq_lag = interp_lag(x_eq_vec, y_n_eq_points, x)
error_n_eq_lag = error(y_n_eq_lag, f_n)
muestra_interpolacion(x, f_n, y_n_eq_lag, "Interpolación de Lagrange, nodos equispaciados.")
    
# Con nodos Chebyshev
y_n_cheb_lag, tiemps_n_cheb_lag = interp_lag(x_cheb_vec, y_n_cheb_points, x)
error_n_cheb_lag = error(y_n_cheb_lag, f_n)
muestra_interpolacion(x, f_n, y_n_cheb_lag, "Interpolación de Lagrange, nodos de Chebyshev.")


### Newton

# Con nodos equispaciados
y_n_eq_new, tiemps_n_eq_new = interp_new(x_eq_vec, y_n_eq_points, x)
error_n_eq_new = error(y_n_eq_new, f_n)
muestra_interpolacion(x, f_n, y_n_eq_new, "Interpolación de Newton, nodos equispaciados.")

# Con nodos Chebyshev
y_n_cheb_new, tiemps_n_cheb_new = interp_new(x_cheb_vec, y_n_cheb_points, x)
error_n_cheb_new = error(y_n_cheb_new, f_n)
muestra_interpolacion(x, f_n, y_n_cheb_new, "Interpolación de Newton, nodos de Chebyshev.")



### Splines

y_n_eq_spl, tiemps_n_eq_spl = interp_spl(x_eq_vec, y_n_eq_points, x)
error_n_eq_spl = error(y_n_eq_spl, f_n)
muestra_interpolacion(x, f_n, y_n_eq_spl, "Interpolación con Splines.")

