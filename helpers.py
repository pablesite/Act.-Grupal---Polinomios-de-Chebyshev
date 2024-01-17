# -*- coding: utf-8 -*-
""" Funciones auxiliares """

import numpy as np

def vectorize_functions(functions):
    my_functions_vec = [0] * len(functions)
    i = 0
    for function in functions:
        my_functions_vec[i] = np.vectorize(function)
        i = i + 1
    return my_functions_vec

def obtain_f_n (my_functions_vec, x):
    f_n = [0] * len(my_functions_vec)
    i = 0
    for my_function_vec in my_functions_vec:
        f_n[i] = my_function_vec(x)
        i = i + 1
    return f_n