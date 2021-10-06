'''
Lista 2 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino

'''

import numpy as np

#import matplotlib.pyplot as plt

''' 
Calcule a matriz Q
para laminas com theta = 30o, 45o e 60o.
'''
A1 = [20, 0.7, 0]
A2 = [0.7, 2, 0]
A3 = [0,0,0.7]
Q = [A1, A2, A3]

def  calc_T(theta):
    # Calcula a matriz de transformação
    theta = theta*np.pi/180
    m = np.cos(theta)
    n = np.sin(theta)
    T = np.array([[m**2,n**2,2*m*n],
         [n**2,  m**2,  -2*m*n],
        [-m*n,  m*n , m**2-n**2]])
    return T
def  calc_Qbar(Q,theta):
    # Entre  com theta em graus
    T = calc_T(theta)
    Qbar1 = Q@(np.transpose(np.linalg.inv(T)))
    Qbar = (np.linalg.inv(T))@(Qbar1)
    #Qbar = np.linalg.inv(T)@(Q@(np.transpose(np.linalg.inv(T))))
    return Qbar

print('theta = 30º:')

calc_T(30)
print(calc_Qbar(Q,30))

print('theta = 45º:')

calc_T(45)
print(calc_Qbar(Q,45))

print('theta = 60º:')

calc_T(60)
print(calc_Qbar(Q,60))