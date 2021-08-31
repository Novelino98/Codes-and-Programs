'''
Lista 1 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino

'''
import numpy as np

"""
Exercício 7
O material usado em uma engrenagens de transmissão de um automóvel é um nylon
moldado por injeção 6,6, contendo 20% em peso de fibras de vidro picado orientadas
aleatoriamente. 
Calcular o comprimento das fibras de vidro para que o material compósito
apresente um módulo de tração de 7 GPa, sendo que Ef = 70 GPa, Em = 3.5 GPa, rho_f=
2.5 g/cm3, rho_m= 1.4 g/cm3, and df = 20 micro_m.
"""

W = 100  #g - gramas
Wf = 0.2*W
Wm = W-Wf

Ec = 7  #GPa
Ef = 70   #GPa - mod. de elasticidade da fibra
Em = 3.5   #GPa - mod de elasticidade da matriz

rho_f = 2.5   #g/cm^3
rho_m = 1.4   #g/cm^3
rho_c = 1/((0.2/rho_f)+(0.8/rho_m))

Vf = Wf*rho_c/(rho_f*W)
Vm = Wm*rho_c/(rho_f*W)

d_f = 0.02  #mm

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


for l in np.arange(0.00001, 2 , 0.000001):    #esse intervalo de variação foi obtido iterativamente
    El_i=equacao(l)
    El_i=round(El_i,3)
    if El_i == EL:
        l = round(l,4)
        print(f' O comprimento mínimo da fibra de vidro necessário para apresenta o módulo de tração de 7 GPa é de {l} mm.')
        break
