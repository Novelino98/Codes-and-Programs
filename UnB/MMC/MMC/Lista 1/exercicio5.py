'''
Lista 1 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino
'''
'''
Exercício 5
Considerando Ef = 400 GPa e Em = 3, 2 GPa e Vf variando entre 0 e 1, plote, em
um mesmo gráfico, o módulo de elasticiade longitudinal EL e o módulo de elasticidade
transversal ET . Para ET , considere a abordagem simplificada e a equação de Halpin-Tsai.
Nas equações de Halpin-Tsai,assumir Eta igual a 0, 0.1, 0.5, 0.7, 1, e 10.
'''

""" Resolução"""
Ef = 400  #GPa
Em = 3.2  #GPa
epsi = [0, 0.1, 0.5, 0.7, 1, 10]

El = []
Et = []
Vf=[]
for Vf_p in range(1,10,1):
    El_posicao = Ef*Vf_p/10 + Em*(1-Vf_p/10)
    El.append(El_posicao)
    Vf.append(Vf_p/10)
Eta=[]
for i in epsi:
    Eta_p = i*((Ef / Em) - 1) / ((Ef / Em) + i)
    Eta_p = round(Eta_p,3) #arredondamento 3 casas decimais
    Eta.append(Eta_p)


def Halpin_tsai(Eta, Vf):
    Et = Em * ((1 + (Eta * Vf)) / (1 - (Eta * Vf)))  # Método analítico Halpin-Tsai
    return Et

Et_linha = []
Eta_matriz=[]

for i in range(len(Eta)):
    Ett = Eta[i]
    for j in range(len(Vf)):
        Vff = Vf[j]
        a=Halpin_tsai(Ett, Vff)
        a = round(a, 3)  # arrendodamento 3 casas decimais
        Et_linha.append(a)
    Eta_matriz.append(Et_linha)
    Et_linha=[]


print(f'El= {El}')
print(f'Vf = {Vf}')
print(f'Eta = {Eta}')
print("A Matriz de valores para o módulo de Elaticidade transversal  [Eta x Vf] é:")
print(Eta_matriz)