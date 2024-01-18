""" Algoritmos de interpolación """

from scipy.interpolate import barycentric_interpolate
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

def interp_bar(x_vec, y_n_points, x):
    """ Funcion que calcula el polinomio interpolador baricentrico """
    y_bar = [[[0] * 100 for i in range(len(y_n_points[0]))] for j in range(len(x_vec))]
    for i in range(len(x_vec)):
        for j in range(len(y_n_points[0])):
            y_bar[i][j] = barycentric_interpolate(x_vec[i], y_n_points[i][j], x)
    return y_bar

def interp_lag(x_vec, y_n_points, x):
    """ Funcion que calcula el polinomio interpolador de Lagrange """
    y_lag = [[[0] * 100 for i in range(len(y_n_points[0]))] for j in range(len(x_vec))]
    for i in range(len(x_vec)):
        for j in range(len(y_n_points[0])):
            # Calcular el polinomio interpolante de Lagrange
            p_l = lagrange(x_vec[i], y_n_points[i][j])
            # Evaluar el polinomio interpolante en los puntos x1
            y_lag[i][j] = p_l(x)
    return y_lag



def muestra_interpolacion(x, f_n, y_n):
    """ Funcion que muestra los plots de la obtencion de los nodos """
    fig, ax = plt.subplots(len(y_n), len(y_n[0]))
    for i in range(len(y_n)):
        for j in range(len(y_n[0])):
            ax[i, j].plot(x, y_n[i][j])
            ax[i, j].plot(x, f_n[j])   
    plt.legend()
    plt.show()