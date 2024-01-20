""" Algoritmos de interpolación """

from scipy.interpolate import barycentric_interpolate
from scipy.interpolate import lagrange
import sympy as sp

import matplotlib.pyplot as plt
import time


def newton_interpolation(x_values, y_values):
    """ Funcion que calcula el polinomio interpolador de Newton """
    n = len(x_values)
    x = sp.symbols('x')
    f = [y_values[i] for i in range(n)]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            f[i] = (f[i] - f[i - 1]) / (x_values[i]-x_values[i - j])

    polynomial = f[-1]
    for i in range(n - 2, -1, -1):
        polynomial = polynomial * (x-x_values[i])+f[i]

    return sp.simplify(polynomial)


def interp_bar(x_vec, y_n_points, x):
    """ Funcion que calcula el polinomio interpolador baricentrico para todos los casos de puntos e imagenes. """
    y_bar = [[[0] * len(x) for i in range(len(y_n_points[0]))] for j in range(len(x_vec))]
    p_b = [[[0] * len(x) for i in range(len(y_n_points[0]))] for j in range(len(x_vec))]
    for i in range(len(x_vec)):
        for j in range(len(y_n_points[0])):
            y_bar[i][j] = barycentric_interpolate(x_vec[i], y_n_points[i][j], x)
    return y_bar,p_b

def interp_lag(x_vec, y_n_points, x):
    """ Funcion que calcula el polinomio interpolador de Lagrange para todos los casos de puntos e imagenes."""
    y_lag = [[[0] * len(x) for i in range(len(y_n_points[0]))] for j in range(len(x_vec))]
    p_l = [[[0] * len(x) for i in range(len(y_n_points[0]))] for j in range(len(x_vec))]
    for i in range(len(x_vec)):
        for j in range(len(y_n_points[0])):
            # Calcular el polinomio interpolante de Lagrange
            p_l[i][j] = lagrange(x_vec[i], y_n_points[i][j])
            # Evaluar el polinomio interpolante en los puntos x1
            y_lag[i][j] = p_l[i][j](x)
    return y_lag, p_l

def interp_new(x_vec, y_n_points, x):
    """ Funcion que calcula el polinomio interpolador de Newton para todos los casos de puntos e imagenes."""
    y_new = [[[0] * len(x) for i in range(len(y_n_points[0]))] for j in range(len(x_vec))]
    tiempos = [[0] * len(y_n_points[0]) for i in range(len(x_vec))]
    for i in range(len(x_vec)):
        for j in range(len(y_n_points[0])):  
            inicio_tiempo = time.time()
            
            # Construir el polinomio interpolante
            p_new = newton_interpolation(x_vec[i], y_n_points[i][j])
            # Crear una función lambda a partir del polinomio
            interp_func = sp.lambdify('x', p_new, 'numpy')
            #Evaluar
            y_new[i][j] = interp_func(x)
            
            fin_tiempo = time.time()
            tiempos[i][j] = fin_tiempo - inicio_tiempo
            print(f"La interp de new tardó {tiempos[i][j]:.2f} segundos en ejecutarse.")
    return y_new, tiempos


def muestra_interpolacion(x, f_n, y_n, title):
    """ Funcion que muestra los plots de la obtencion de los nodos """
    fig, ax = plt.subplots(len(y_n), len(y_n[0]))
    fig.subplots_adjust(hspace=0.2, wspace=0.2)
    fig.set_size_inches(16,10)
    for i in range(len(y_n)):
        for j in range(len(y_n[0])):
            ax[i, j].plot(x, f_n[j]) 
            ax[i, j].plot(x, y_n[i][j])
            ax[i, j].tick_params(labelsize=12)
            if i == 0:
                ax[i, j].set_title("Función " + str(j + 1) + ". Nodos: 11.", fontsize=12)
            elif i == 1:
                ax[i, j].set_title("Función " + str(j + 1) + ". Nodos: 21.", fontsize=12)
    
    fig.suptitle(title, fontsize = 22)
    plt.show()
    