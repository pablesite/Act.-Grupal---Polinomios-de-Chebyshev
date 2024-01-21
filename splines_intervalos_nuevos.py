# -*- coding: utf-8 -*-

import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline 
import matplotlib.pyplot as plt
import time

# Nodos y valor real de las funciones
x_1=np.linspace(-1*np.pi, np.pi)
x_2=np.linspace(-4, 4)
x_3=np.linspace(-1, 1)
y_1=np.sin(x_1)
y_2=1/(1+25*(x_2**2))
y_3=np.exp(-20*x_3**2)

# Nodos e Interpolación para 11 nodos equiespaciados

start11_1=time.perf_counter_ns()
x11_1=np.linspace(-1*np.pi, np.pi,num=11)
y11_1=np.sin(x11_1)
sp11_1= InterpolatedUnivariateSpline(x11_1, y11_1)
end11_1 = time.perf_counter_ns()

start11_2=time.perf_counter_ns()
x11_2=np.linspace(-4, 4,num=11)
y11_2=1/(1+25*(x11_2**2))
sp11_2= InterpolatedUnivariateSpline(x11_2, y11_2)
end11_2 = time.perf_counter_ns()

start11_3=time.perf_counter_ns()
x11_3=np.linspace(-1, 1,num=11)
y11_3=np.exp(-20*x11_3**2)
sp11_3= InterpolatedUnivariateSpline(x11_3, y11_3)
end11_3 = time.perf_counter_ns()

# Nodos e Interpolación para 21 nodos equiespaciados

start21_1=time.perf_counter_ns()
x21_1=np.linspace(-1*np.pi, np.pi, num=21)
y21_1=np.sin(x21_1)
sp21_1= InterpolatedUnivariateSpline(x21_1, y21_1)
end21_1 = time.perf_counter_ns()

start21_2=time.perf_counter_ns()
x21_2=np.linspace(-4, 4, num=21)
y21_2=1/(1+25*(x21_2**2))
sp21_2= InterpolatedUnivariateSpline(x21_2, y21_2)
end21_2 = time.perf_counter_ns()

start21_3=time.perf_counter_ns()
x21_3=np.linspace(-1, 1, num=21)
y21_3=np.exp(-20*x21_3**2)
sp21_3= InterpolatedUnivariateSpline(x21_3, y21_3)
end21_3 = time.perf_counter_ns()


# Representación gráfica
figura, graficas=plt.subplots(2,3, constrained_layout = True)
    
graficas[0, 0].plot(x11_1, y11_1, 'o')
graficas[0, 0].plot(x_1, y_1, label='true')
graficas[0, 0].plot(x11_1, sp11_1(x11_1))
graficas[0, 0].set_title('Función 1. Nodos: 11')

graficas[1,0].plot(x21_1, y21_1, 'o')
graficas[1,0].plot(x_1, y_1, label='true')
graficas[1,0].plot(x21_1, sp21_1(x21_1))
graficas[1,0].set_title('Función 1. Nodos: 21')

graficas[0, 1].plot(x11_2, y11_2, 'o')
graficas[0, 1].plot(x_2, y_2, label='true')
graficas[0, 1].plot(x11_2, sp11_2(x11_2))
graficas[0, 1].set_title('Función 2. Nodos: 11')

graficas[1,1].plot(x21_2, y21_2, 'o')
graficas[1,1].plot(x_2, y_2, label='true')
graficas[1,1].plot(x21_2, sp21_2(x21_2))
graficas[1,1].set_title('Función 2. Nodos: 21')

graficas[0, 2].plot(x11_3, y11_3, 'o')
graficas[0, 2].plot(x_3, y_3, label='true')
graficas[0, 2].plot(x11_3, sp11_3(x11_3))
graficas[0, 2].set_title('Función 3. Nodos: 11')

graficas[1,2].plot(x21_3, y21_3, 'o')
graficas[1,2].plot(x_3, y_3, label='true')
graficas[1,2].plot(x21_3, sp21_3(x21_3))
graficas[1,2].set_title('Función 2. Nodos: 21')


# Tiempos de ejecución
print(f"Caso 1 interpolando con 11 nodos: {(end11_1 - start11_1)} ns")
print(f"Caso 1 interpolando con 21 nodos: {(end21_1 - start21_1)} ns")

print(f"Caso 2 interpolando con 11 nodos: {(end11_2 - start11_2)} ns")
print(f"Caso 2 interpolando con 21 nodos: {(end21_2 - start21_2)} ns")

print(f"Caso 3 interpolando con 11 nodos: {(end11_3 - start11_3)} ns")
print(f"Caso 3 interpolando con 21 nodos: {(end21_3 - start21_3)} ns")

# Errores de interpolación
error11_1= np.array(sp11_1)-y_1
