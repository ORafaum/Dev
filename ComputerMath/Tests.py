'Polinômio interpolador'
from scipy.interpolate import *
'Vértice da Párabola e Vetores'
import numpy as np
'Fórmula de Slovin'
from math import ceil

'Polinômio interpolador'
'''
x=[0,5,8]
y=[6,2,15]

p= lagrange(x,y)

print(p)'''

'''dados = [67.8,78.6,54.4,98.6,99.4,130.8,142.6,161.6,142.5,158.4]

desvio_padrao = np.std(dados)

print(desvio_padrao)'''


'Vértice da párabola'
'''a = 10
b = -150
c = 300
xv=-b/(2*a)
delta = b**2-4*a*c
yv=-delta/(4*a)
print(xv)
print(yv)'''

'Fórmula de Slovin'

'''N = 150000
e=0.02

n=ceil(N/(1+N*e**2))

print(n)'''

'Vetores'

'''u = np.array([[4,7,0,-8]])
v = np.array([[9,17,-12,21]])

w = u+v
print(w)'''

'''a = 7.0102e5
b = 2.1233e3
resultado = (a-b)'''

print(f'{0.00034500*10**4:.4f}')

'''ve = 12456.77
va = 12450
print(ve - va)'''