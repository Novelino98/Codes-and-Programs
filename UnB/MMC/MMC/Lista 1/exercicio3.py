'''
Lista 1 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino
'''
'''
# Exercício 3

Calcule a razão entre as tensões nas fibras e na matriz e a razão entre as tensões na fibra e
no compósito para um compósito unidirecional com fração volumétrica Vf = 10%, 25%,
50% e 75%. Assuma que o compósito é carregado na direção das fibras e que Ef = 400
GPa e Em = 3; 2 GPa.
'''
# Fração volumétrica de fibra
Vf = [0.1, 0.25, 0.5, 0.75]       #caso 1


# Modulo de elasticidade da fibra (f) e matriz (m)
Ef = 400    #GPa
Em = 3.2    #GPa

''' Resolução '''
Vm=[]
for i in Vf:
    Vm_posicao = 1 - i
    Vm.append(Vm_posicao)


El=[]
for j, k in enumerate(Vf) and enumerate(Vm):
    El_posicao = (Ef*Vf[j]) + (Em*Vm[j])
    El.append(El_posicao)

Rfc=[]
Rfm = []
R_E = Ef/Em
for b in range(0,4):
    Rfc_posicao = R_E / (R_E + (Vm[b]/Vf[b]))
    Rfc.append(Rfc_posicao)
    Rfc[b] = round(Rfc[b],2)     #arredondamento
    #Razao entre fibra e matriz
    Rfm_posicao = Ef*Vf[b]/(Em*Vm[b])
    Rfm.append(Rfm_posicao)
    Rfm[b] = round(Rfm[b], 2)  # arredondamento

print('Para Vf = 0.1, 0.25, 0.5, 0.75 respectivamente:')
print(f'Módulo de elasticidade = {El}')
print(f'Razão de carga entre fibra e compósito = {Rfc}')
print(f'Razão de tensão entre fibra e o compósito = {Rfm}')

