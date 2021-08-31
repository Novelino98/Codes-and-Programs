'''
Lista 1 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino

'''
import numpy as np

"""
Exercício 8
Em uma aplicação mais exigente, o módulo do material é aumentado para o dobro do
valor indicado no problema do exercício anterior, substituindo as fibras de vidro por fibras
de carbono. Calcule o comprimento das fibras de carbono necessárias se o material da
matriz e a fração do peso da fibra forem os mesmos do problema do exercício anterior.
Para fibras de carbono, tome Ef = 210 GPa, rho_f = 1,8 g/cm3 e df = 0.015 mm.
"""

W = 100  #g - gramas
Wf = 0.2*W
Wm = W-Wf

Ec = 14  #GPa  FIBRA DE CARBONO
Ef = 210   #GPa - mod. de elasticidade da fibra
Em = 3.5   #GPa - mod de elasticidade da matriz

rho_f = 1.8   #g/cm^3
rho_m = 1.4   #g/cm^3
rho_c = 1/((0.2/rho_f)+(0.8/rho_m))

Vf = Wf*rho_c/(rho_f*W)
Vm = Wm*rho_c/(rho_f*W)

d_f = 0.015  #mm

#Halpin-Tsai
Epsi = 2  # fibras circulares
Eta = ((Ef/Em) - 1)/((Ef/Em)+ Epsi)

ET = Em*((1+Epsi*Eta*Vf)/(1-Eta*Vf))

# Para fibras orientadas aleatoriamente
EL = (Ec - ((5/8)*ET))*(8/3)
EL = round(EL,3)

El_i = []
def equacao(l):
    Eta_L = ((Ef/Em)-1)/((Ef/Em)+2*(l/d_f))
    El_i = Em*((1+(2*(l/d_f)*Eta_L*Vf))/(1-(Eta_L*Vf)))
    return El_i


for l in np.arange(0.00001, 1.5 , 0.000001):    #esse intervalo de variação foi obtido iterativamente
    El_i=equacao(l)
    El_i=round(El_i,3)
    if El_i == EL:
        l = round(l,4)
        print(f' O comprimento mínimo da FIBRA DE CARBONO necessário para apresenta o módulo de tração de 14 GPa é de {l} mm.')
        break