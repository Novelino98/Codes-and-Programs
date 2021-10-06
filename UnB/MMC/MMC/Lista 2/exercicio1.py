'''
Lista 2 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino

'''

import numpy as np
#import matplotlib.pyplot as plt

''' 
Exercício 1 - Calcule as matrizes de rigidez Q e de fleexibilidade S para a lamina unidirecional com as seguintes 
constantes elasticas: EL = 20 GPa, ET = 2 GPa, GLT = 0,7 GPa e LT = 0,35.
'''

EL = 20  #GPa
ET = 2  #GPa
GLT = 0.7  #GPa
nuLT = 0.35

# MATRIZ RIGIDEZ Q
def calc_Q(EL,ET,GLT,nuLT):
    nuTL = nuLT*ET/EL# Coeficiente de Poisson secundário
    Q11 = EL/(1-nuLT*nuTL)
    Q22 = ET/(1-nuLT*nuTL)
    Q66 = GLT
    Q16 = 0
    Q26 = 0
    Q12 = nuTL*EL/(1-nuLT*nuTL)
    Q = np.array([[Q11, Q12, Q16],
         [Q12, Q22, Q26],
         [Q16, Q26, Q66]])
    return  Q

print('A matriz de rigidez Q é dada por:')
print(calc_Q(EL,ET,GLT,nuLT))

def calc_S(EL,ET,GLT,nuLT):
    nuTL = nuLT*ET/EL# Coeficiente de Poisson secundário
    S11 = 1/EL
    S22 = 1/ET
    S66 = 1/GLT
    S16 = 0
    S26 = 0
    S12 = -nuLT/(ET)
    S = np.array([[S11, S12, S16],
         [S12, S22, S26],
         [S16, S26, S66]])
    return  S
print('A matriz de flexibilidade S é dada por:')
print(calc_S(EL,ET,GLT,nuLT))