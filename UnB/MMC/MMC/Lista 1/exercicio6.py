import matplotlib.pyplot as plt
import numpy as np

'''
Lista 1 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino

'''
"""
Exercício 6

Um compósito é fabricado com fibras de vidro (diâmetro = 0,03 mm) em uma matriz
de resina epóxi. Todas as fibras estão alinhadas paralelamente à direção da aplicação da
carga. A fração volumétrica de fibras é de 40%. Suponha que a matriz se comporte como
um material plástico rígido com um limite de escoamento de 28 MPa e que Ef = 70 GPa
e Em = 3,5 GPa. Supondo que a resistência à tração das fibras seja de 1,4 GPa, calcule
o comprimento crítico da fibra. Construa um gráfico de resistência do compósito versus
comprimento da fibra para comprimentos de fibra entre 0,1 lc e 100 lc.
"""

d_fibra = 0.03  #mm  - diâmetro da fibra

Vm = 0.4   #fração volumétrica de fibra de vidro
Vf = 1-Vm

Ef = 70   #GPa - módulo de elasticidade da fibra
Em = 3.5  #GPa  - Módulo de elasticidade da matriz
Ec = Ef*Vf + Em*Vm
sigma_f = 1400  #MPa - resistencia a tracao das fibras
sigma_m = 28  #MPa - Limite de escoamento do compósito

sigma_c = sigma_f*Vf + sigma_m*Vm

sigma_max = (Ef/Ec)*sigma_c
Tau_y = sigma_m/2

lc = sigma_f*d_fibra/(2*Tau_y)

print(f' O comprimento crítico da fibra é de {lc} mm.')
sigma_comp = []
lt =[]

for l in np.arange (0.1, 1, 0.1):
    sigma_comp_i = (Tau_y*(l*lc)/(d_fibra)*Vf + sigma_m*Vm)/1000
    sigma_comp.append(sigma_comp_i)
    lt.append(l)

for l in np.arange (1,100,0.1):
    sigma_comp_j = (sigma_f*(1-(lc/(2*l*lc))*Vf+sigma_m*Vm))/1000
    sigma_comp.append(sigma_comp_j)
    lt.append(l)

plt.plot(lt, sigma_comp)

plt.xlabel('lc')
plt.ylabel('sigma_composito (GPa)')
plt.title('Resistência do compósito x comprimento da fibra')
plt.show()



