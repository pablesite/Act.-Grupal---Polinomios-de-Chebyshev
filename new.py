import numpy as np
import matplotlib.pyplot as plt

def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = \
                (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef


def newton_poly(coef, x_data, x):
    '''
    evaluate the newton polynomial
    at x
    '''
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p


def my_func2(x):
    return 1 / (1 + 25 * x**2)

# Puntos de interpolación
start = -5
stop = 5
nPoints = 11
x = np.linspace(start, stop, nPoints)
y = my_func2(x)


# get the divided difference coef
a_s = divided_diff(x, y)[0, :]

# evaluate on new data points
# Puntos para la representación gráfica
x1 = np.linspace(min(x), max(x), num=100)
y_new = newton_poly(a_s, x, x1)

plt.plot(x, y, '-')
plt.plot(x1, y_new)
plt.show()