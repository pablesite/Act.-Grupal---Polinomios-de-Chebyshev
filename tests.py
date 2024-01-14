from scipy import linalg
import numpy as np
import math
import matplotlib.pyplot as plt

def my_sin(x):
    return math.sin(x)

start = -5
stop = 5
nPoints = 11
step = (stop - start + 1)/nPoints # 
x = np.arange(start, stop + 1, step)
my_sin_vec = np.vectorize(my_sin)
f = my_sin_vec(x)

plt.plot(x, f)