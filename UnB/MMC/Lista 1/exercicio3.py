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

Rc=[]
R_rhof = []
R_E = Ef/Em
for b in range(0,3):
    Rc_posicao = R_E / (R_E + (Vm[b]/Vf[b]))
    Rc.append(Rc_posicao)
    Rc[b] = round(Rc[b],2)     #arredondamento
    #Razao de tensão utilizando o modulo de elasticidade. Verificar posteriormente
    R_rhof_posicao = Ef/(El[b])
    R_rhof.append(R_rhof_posicao)
    R_rhof[b] = round(R_rhof[b], 2)  # arredondamento

print(El)
print(Rc)
print(R_rhof)

