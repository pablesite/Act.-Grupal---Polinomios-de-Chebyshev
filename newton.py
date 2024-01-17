import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math
import time
# Definir la función a interpolar
def my_func2(x):
    return 1 / (1 + 25 * x**2)

def my_func1(x):
    return math.sin(x)

# Puntos de interpolación
start = -5
stop = 5
nPoints = 12
x_values = np.linspace(start, stop, nPoints)
y_values = my_func2(x_values)

# Puntos para la representación gráfica
x1 = np.linspace(min(x_values), max(x_values), num=100)

def newton_interpolation(x_values, y_values):
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


# Construir el polinomio interpolante
interpolation_polynomial = newton_interpolation(x_values, y_values)
# Crear una función lambda a partir del polinomio
interp_func = sp.lambdify('x', interpolation_polynomial, 'numpy')
#Evaluar
y_eval = interp_func(x1)

print(time.time())

# Imprimir el polinomio simplificado
print("Polinomio de Interpolación Simplificado:")
print(interpolation_polynomial)

# Evaluación del polinomio en los puntos de representación gráfica
plt.plot(x1, my_func2(x1), '-', label='Función Original')
plt.plot(x1, y_eval, '-', label='Newton Interpolación')
plt.legend()
plt.show()


#Error

pol = y_eval
f=my_func2(x1)
error = pol-f
error_abs = np.linalg.norm(error)

print(error_abs)