# -*- coding: utf-8 -*-

""" Obtencion de nodos (11 y 21, equispaciados y de Chebysheb)"""

import numpy as np
import numpy.polynomial.chebyshev as cheb
import matplotlib.pyplot as plt

def obtencion_nodos_eq(start, stop, n_points_vec):
    """ Funcion que obtiene los nodos equispaciados en un dominio para diferentes numero de puntos """
    step_vec = [0] * len(n_points_vec)
    x_eq_vec = [[0] * n_points_vec[i] for i in range(len(n_points_vec))]
    i = 0
    for n_points in n_points_vec:
        step_vec[i] = (stop - start)/(n_points - 1)
        x_eq_vec[i] = np.arange(start, stop + step_vec[i], step_vec[i])
        i = i + 1
    return x_eq_vec

def obtencion_nodos_cheb(start, stop, n_points_vec):
    """ Funcion que obtiene los nodos equispaciados en un dominio para diferentes numero de puntos """
    coeffs_cheb = [0] * len(n_points_vec)
    T_n = [[0] * n_points_vec[i] for i in range(len(n_points_vec))]
    x_cheb_vec = [[0] * n_points_vec[i] for i in range(len(n_points_vec))]
    i = 0
    for n_points in n_points_vec:
        coeffs_cheb[i] = [0]*n_points_vec[i] + [1]
        T_n[i] = cheb.Chebyshev(coeffs_cheb[i], [start, stop])
        x_cheb_vec[i] = T_n[i].roots()
        i = i + 1
    return x_cheb_vec

def muestra_nodos(x, f_n, x_eq_vec, y_n_eq_points):
    """ Función que muestra los plots de la obtención de los nodos """
    fig, ax = plt.subplots(len(x_eq_vec), len(y_n_eq_points[0]))
    for i in range(len(x_eq_vec)):
        for j in range(len(y_n_eq_points[0])):
            ax[i, j].plot(x_eq_vec[i], y_n_eq_points[i][j], "o")
            ax[i, j].plot(x, f_n[j])   
    plt.legend()
    plt.show()